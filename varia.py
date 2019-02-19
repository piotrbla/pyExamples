import pytest


def foo_tested(a, b):
    return a + b


def main():
    print(foo_tested(1, 2))


if __name__ == '__main__':
    main()
