import sys
from types import SimpleNamespace

import pytest

from unique_defaults import (
    unique_builtins, unique_bytearrays, unique_defaults, unique_dicts, unique_lists, unique_sets
)

@pytest.mark.parametrize(
    'wrapped', [
        pytest.param(unique_lists(lambda a=[], b=[1, 2]: (a, b)), id='unique_lists'),
        pytest.param(unique_dicts(lambda a={}, b={1: 'a', 2: 'b'}: (a, b)), id='unique_dicts'),
        pytest.param(unique_sets(lambda a=set(), b={1, 2}: (a, b)), id='unique_sets'),
        pytest.param(unique_bytearrays(lambda a=bytearray(), b=bytearray(b'ab'): (a, b)), id='unique_bytearrays'),
        pytest.param(unique_builtins(lambda a=bytearray(), b={}, c=[], d=set(): (a, b, c, d)), id='unique_builtins'),
        pytest.param(unique_defaults(SimpleNamespace)(lambda a=SimpleNamespace(): (a,)), id='custom_unique'),
    ]
)
def test_unique(wrapped):
    result1 = wrapped()
    result2 = wrapped()
    for first, second in zip(result1, result2):
        assert first == second
        assert first is not second


def test_passed_arguments():
    static = ['a', 'b']
    @unique_builtins
    def test(a=[]):
        return a

    assert test(None) is None
    assert test([1, 2]) == [1, 2]
    assert test(static) is static


def test_with_arg():
    @unique_builtins
    def test(a, b=[]):
        return b

    assert test(...) == test(...)
    assert test(...) is not test(...)


def test_with_kwarg():
    @unique_builtins
    def test(a='spam', b=[]):
        return b

    assert test() == test()
    assert test() is not test()


def test_several_mutable_defaults():
    @unique_builtins
    def test(a=[], b='spam', c=[], d=42, e={}):
        return a, c, e

    result1 = test()
    result2 = test()
    assert result1[0] == result2[0]
    assert result1[0] is not result2[0]
    assert result1[1] == result2[1]
    assert result1[1] is not result2[1]
    assert result1[2] == result2[2]
    assert result1[2] is not result2[2]


def test_kwargonly():
    @unique_builtins
    def test(a=[], *, b=[]):
        return a, b

    result1 = test()
    result2 = test()
    assert result1[0] is not result2[0]
    assert result1[0] == result2[0]
    assert result1[1] is not result2[1]
    assert result1[1] == result2[1]


def test_early_args():
    @unique_builtins
    def test(*args, b=[]):
        return b

    assert test() == test()
    assert test() is not test()


def test_late_args():
    @unique_builtins
    def test(b=[], *args):
        return b

    assert test() == test()
    assert test() is not test()


def test_kwargs():
    @unique_builtins
    def test(b=[], **kwargs):
        return b

    assert test() == test()
    assert test() is not test()


def test_does_not_apply():
    @unique_sets
    def test(a=[]):
        return a

    assert test() is test()


def test_some_do_not_apply():
    @unique_sets
    def test(a=[], b={1}):
        return a, b

    result1 = test()
    result2 = test()
    assert result1[0] is result2[0]
    assert result1[1] is not result2[1]
    assert result1[1] == result2[1]

def test_nested():
    @unique_sets
    @unique_lists
    @unique_defaults('foo')
    def test(a=[], b={}, c=set(), foo=SimpleNamespace()):
        return a, b, c, foo

    result1 = test()
    result2 = test()
    assert result1[0] is not result2[0]
    assert result1[0] == result2[0]
    assert result1[1] is result2[1]
    assert result1[2] is not result2[2]
    assert result1[2] == result2[2]
    assert result1[3] is not result2[3]
    assert result1[3] == result2[3]
