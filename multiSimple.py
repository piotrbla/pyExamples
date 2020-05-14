from random import randint

STATE_GOOD = 1
STATE_BAD = 2


def save(state, m1, m2, entry):
    from datetime import datetime
    now = datetime.now()
    with open('log.txt', 'at') as f:
        f.write(now.strftime("%d/%m/%Y %H:%M:%S") + '\n')
        if state == STATE_BAD:
            f.write("BAD: ")
        else:
            f.write("OK: ")
        f.write(str(m1) + '*' + str(m2) + '=' + str(m1 * m2) + ' ->' + str(entry) + '\n')


z = 1
counter = 1
while z != 0:
    x = 10
    y = 10
    while x > 5 and y > 5:
        x = randint(2, 10)
        y = randint(2, 10)
    print('Zadanie numer: ', counter)
    print(x, 'razy', y)
    while True:
        try:
            z = int(input('Podaj wynik:'))
            break
        except:
            pass
    if z == 0:
        break
    if z == x * y:
        print('Dobrze')
        print()
        save(STATE_GOOD, x, y, z)
    else:
        print('Źle')
        print()
        save(STATE_BAD, x, y, z)
    counter += 1
    if counter > 10:
        counter = 1
