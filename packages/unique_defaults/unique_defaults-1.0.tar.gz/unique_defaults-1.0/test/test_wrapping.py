from functools import wraps
from inspect import signature

from unique_defaults import unique_builtins


def test_wraps():
    @unique_builtins
    def test(a: object):
        """test doc"""

    assert test.__name__ == "test"
    assert test.__module__ == "test_wrapping"
    assert test.__qualname__ == "test_wraps.<locals>.test"
    assert test.__annotations__ == {"a": object}
    assert test.__doc__ == "test doc"


def test_inspect():
    def test(a, b, c={}, *args, d=set(), **kwargs):
        return a, b, c, d

    mutated_test = unique_builtins(test)

    assert signature(test) == signature(mutated_test)


def test_decorator():
    def decorator(func):
        return func

    @decorator
    @unique_builtins
    def test(a=[]):
        return a

    assert test() is not test()

    @unique_builtins
    @decorator
    def test2(a=[]):
        return a

    assert test2() is not test2()


def test_decorator_generator():
    def decorator_generator(_kwarg=[]):
        def _outer(func):
            def _inner(*args, **kwargs):
                return func(*args, **kwargs), _kwarg

            return _inner

        return _outer

    @decorator_generator()
    @unique_builtins
    def test(a=[]):
        return a

    result1 = test()
    result2 = test()
    assert result1[0] is not result2[0]
    assert result1[1] is result2[1]

    @unique_builtins
    @decorator_generator()
    def test2(a=[]):
        return a

    result1 = test()
    result2 = test()
    assert result1[0] is not result2[0]
    assert result1[1] is result2[1]
