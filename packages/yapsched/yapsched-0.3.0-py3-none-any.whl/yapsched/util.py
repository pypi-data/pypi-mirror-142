# Copyright 2020 Software Factory Labs, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""A set of utility methods that are used by the YAP Scheduler."""

from functools import partial
import inspect
import logging
from typing import Any, Callable

logger = logging.getLogger(__name__)


def obj_to_ref(obj: Any) -> str:
    """Returns a string with the path to the given callable.

    Args:
        obj (Callable): An object, expected to be a callable method.

    Raises:
        ValueError: If the given object is a partial, lamda, or nested function.

    Returns:
        str: A `module:name` string path to the callable.
    """
    if isinstance(obj, partial):
        raise ValueError('Cannot create a reference to a partial()')

    name = get_callable_name(obj)
    if '<lambda>' in name:
        raise ValueError('Cannot create a reference to a lambda')
    if '<locals>' in name:
        raise ValueError('Cannot create a reference to a nested function')

    if inspect.ismethod(obj):
        if hasattr(obj, 'im_self') and obj.im_self:
            # bound method
            module = obj.im_self.__module__
        elif hasattr(obj, 'im_class') and obj.im_class:
            # unbound method
            module = obj.im_class.__module__
        else:
            module = obj.__module__
    else:
        module = obj.__module__
    return '%s:%s' % (module, name)


def ref_to_obj(ref: str) -> object:
    """Parses a reference path string to retrieve the object it points to.

    Args:
        ref (str): A string path to an object.

    Raises:
        TypeError: If the reference is not a string.
        ValueError: If it is not a valid reference string (not containg ':').
        LookupError: If the object's module could not be imported or its attribute could not
            be resolved.

    Returns:
        object: The object pointed to by `ref` string.
    """
    if not isinstance(ref, str):
        raise TypeError('References must be strings')
    if ':' not in ref:
        raise ValueError('Invalid reference')

    module_name, rest = ref.split(':', 1)
    try:
        obj = __import__(module_name, fromlist=[rest])
    except ImportError:
        raise LookupError('Error resolving reference %s: could not import module' % ref)

    try:
        for name in rest.split('.'):
            obj = getattr(obj, name)
        return obj
    except Exception:
        raise LookupError('Error resolving reference %s: error looking up object' % ref)


def get_callable_name(func: Callable) -> str:
    """Returns the best available display name for the given callable.

    Args:
        func (Callable): The function to get a name for.

    Raises:
        TypeError: If a name for the function wasn't able to be resolved.

    Returns:
        str: The best available display name for the given callable.
    """
    # the easy case (on Python 3.3+)
    if hasattr(func, '__qualname__'):
        return func.__qualname__

    # class methods, bound and unbound methods
    f_self = getattr(func, '__self__', None) or getattr(func, 'im_self', None)
    if f_self and hasattr(func, '__name__'):
        f_class = f_self if inspect.isclass(f_self) else f_self.__class__
    else:
        f_class = getattr(func, 'im_class', None)

    if f_class and hasattr(func, '__name__'):
        return '%s.%s' % (f_class.__name__, func.__name__)

    # class or class instance
    if hasattr(func, '__call__'):
        # class
        if hasattr(func, '__name__'):
            return func.__name__

        # instance of a class with a __call__ method
        return func.__class__.__name__

    raise TypeError('Unable to determine a name for %r -- maybe it is not a callable?' % func)


def get_class_logger(obj: Any) -> logging.Logger:
    """Returns the logger for the given object.

    Args:
        obj (object): An object to retrive its class logger for.

    Returns:
        logging.Logger: The object's class logger.
    """
    klass = list(filter(lambda m: m[0] == '__class__', inspect.getmembers(obj)))[0][1]
    cls_name = str(klass)[8:-2]
    return logging.getLogger(cls_name)
