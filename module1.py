# from module3 import weirdfun
# import module2
from unittest.test.test_case import Test


def high_and_low(numbers):
    splitted = [int(x) for x in numbers.split()]
    return str(max(splitted)) + " " + str(min(splitted))


# high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")
assert (high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") == "542 -214")
