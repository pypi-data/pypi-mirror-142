"""Replace a function's default values with objects unique to each function call"""

import inspect
from collections import namedtuple
from collections.abc import Iterable
from copy import copy
from functools import wraps

_replacement = namedtuple("_replacement", "position name")

def unique_defaults(intercept):
    """Replace any default parameter value of the types or of the names
    given with a new copy of the object on each function call

    :param intercept: One or more types that are looked for in the
        function signature for replacement OR one or more strings of
        parameter names for replacement
    :return: Wrapper function
    """
    if not isinstance(intercept, Iterable) or isinstance(intercept, str):
        intercept = (intercept,)
    else:
        intercept = tuple(intercept)
    if len(intercept) < 1:
        raise TypeError("Must provide at least one type or name")
    if isinstance(intercept[0], str):
        should_intercept = lambda p: p.name in intercept
    else:
        should_intercept = lambda p: isinstance(p.default, intercept)

    def capture_defaults(func):
        base_func = inspect.unwrap(func)
        defaults_to_replace = {}
        kwdefaults_to_replace = []
        defaults_idx = 0
        for defaults_ids, param in enumerate(inspect.signature(base_func).parameters.values()):
            if param.default is not param.empty:
                if param.kind is param.KEYWORD_ONLY:
                    if should_intercept(param):
                        kwdefaults_to_replace.append(param)
                else:
                    if should_intercept(param):
                        defaults_to_replace[defaults_idx] = param
                    defaults_idx += 1

        @wraps(func)
        def inner(*args, **kwargs):
            func_defaults = list(base_func.__defaults__ or [])
            for idx, replace in defaults_to_replace.items():
                func_defaults[idx] = copy(replace.default)
                base_func.__defaults__ = tuple(func_defaults)
            func_kwdefaults = list(base_func.__kwdefaults__ or [])
            for replace in kwdefaults_to_replace:
                base_func.__kwdefaults__[replace.name] = copy(replace.default)
            return func(*args, **kwargs)

        return inner

    return capture_defaults


unique_bytearrays = unique_defaults(bytearray)
unique_bytearrays.__doc__ = "Replace any default bytearrays with new copies on each function call"
unique_dicts = unique_defaults(dict)
unique_dicts.__doc__ = "Replace any default dicts with new copies on each function call"
unique_lists = unique_defaults(list)
unique_lists.__doc__ = "Replace any default lists with new copies on each function call"
unique_sets = unique_defaults(set)
unique_sets.__doc__ = "Replace any default sets with new copies on each function call"
unique_builtins = unique_defaults((bytearray, dict, list, set))
unique_builtins.__doc__ = "Replace any default bytearrays, dicts, lists, or sets with new copies on each function call"
