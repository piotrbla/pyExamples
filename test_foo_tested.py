from unittest import TestCase
from varia import foo_tested


class TestFoo_tested(TestCase):
    def test_foo_tested(self):
        assert foo_tested(1, 2) == 3

    def test_foo_tested_big(self):
        assert foo_tested(19, 29) == 48

    def test_foo_tested_bigger(self):
        assert foo_tested(20, 29) == 49

    def test_foo_tested_biggest(self):
        assert foo_tested(21, 29) == 50
