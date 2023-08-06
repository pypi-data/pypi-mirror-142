"""positional only arguments are a SyntaxError in python <= 3.7"""
from inspect import signature
from unique_defaults import unique_builtins

def test_posonly():
    @unique_builtins
    def test(a=[], /, b=[]):
        return a, b

    result1 = test()
    result2 = test()
    assert result1[0] is not result2[0]
    assert result1[0] == result2[0]
    assert result1[1] is not result2[1]
    assert result1[1] == result2[1]


def test_posonly_and_kwargonly():
    @unique_builtins
    def test(a=[], /, b={}, *, c=[]):
        return a, b, c

    result1 = test()
    result2 = test()
    assert result1[0] is not result2[0]
    assert result1[0] == result2[0]
    assert result1[1] is not result2[1]
    assert result1[1] == result2[1]
    assert result1[2] is not result2[2]
    assert result1[2] == result2[2]


def test_inspect():
    def test(a, /, b, c={}, *args, d=set(), **kwargs):
        return a, b, c, d

    mutated_test = unique_builtins(test)

    assert signature(test) == signature(mutated_test)
