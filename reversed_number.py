def check(number):
    reversed_number = ''
    for c in reversed(str(number)):
        if c == '1':
            reversed_number += '1'
        elif c == '6':
            reversed_number += '9'
        elif c == '9':
            reversed_number += '6'
        elif c == '0':
            reversed_number += '0'
        elif c == '8':
            reversed_number += '8'
        else:
            return False
    return reversed_number == str(number)


def solve(a, b):
    count = 0
    for x in range(a, b):
        if check(x):
            count += 1
    return count


print(solve(0, 10), 3)
print(solve(10, 100), 4)
print(solve(100, 1000), 12)
print(solve(1000, 10000), 20)
print(solve(10000, 15000), 6)
print(solve(15000, 20000), 9)
print(solve(60000, 70000), 15)
print(solve(60000, 130000), 55)
