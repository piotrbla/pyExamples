import unittest.mock as mock


def say_hello():
    name = input("What is your name? ")
    return "Hello " + name


def test_say_hello():
    with mock.patch('builtins.input', return_value='dbw'):
        assert say_hello() == 'Hello dbw'

    with mock.patch('builtins.input', side_effect=['dbw', 'uki']):
        assert say_hello() == 'Hello dbw'
        assert say_hello() == 'Hello uki'
