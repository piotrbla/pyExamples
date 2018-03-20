N = int(input())
min_value = 9999.0
second_min = 9999.0
students = []
for i in range(N):
    name = input()
    grade = float(input())
    students.append([name, grade])
    if grade < min_value:
        second_min = min_value
        min_value = grade
    if grade < second_min:
        if grade > min_value:
            second_min = grade
seconders = sorted([x[0] for x in students if x[1] == second_min])

for student in seconders:
    print(student)


def a():
    return 1


def b():
    return 2


def c():
    return 3


def aa():
    return a() + b()


foo = aa()