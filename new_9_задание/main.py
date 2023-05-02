from functools import reduce
from math import gcd


def create_database():
    t = int(input("Число простых сомножителей t = "))
    primes = list(map(int, open('primes_database.txt', 'r').read().split('\n')))
    mults = []
    i = 0
    while i < len(primes):
        if t > len(primes) - i:
            break
        mult = primes[i:i + t]
        mults.append(mult)
        i += t
    with open('mults_database.txt', 'w') as mults_db:
        for mult in mults:
            mults_db.write('{} = {}\n'.format(str(reduce(lambda x, y: x * y, mult)), "*".join(str(num) for num in mult)))
    print('База данных из произведений создана\n')


def division_method():
    n = int(input("Натуральное число n = "))
    mults_read = open('mults_database.txt', 'r').read().rstrip().split('\n')
    mults, dividers_dict = [], {}
    for i in range(len(mults_read)):
        mult, dividers = mults_read[i].split(' = ')
        mults.append(int(mult))
        dividers_dict[int(mult)] = list(map(int, dividers.split('*')))
    dividers, n_copy = [], n
    while True:
        flag = False
        for mult in mults:
            if gcd(n, mult) != 1:
                for divider in dividers_dict[mult]:
                    if n % divider == 0:
                        dividers.append(divider)
                        n //= divider
                        flag = True
                        break
            if flag:
                break
        if not flag:
            break
    if n > 1:
        dividers.append(n)
    print("{} = {}\n".format(n_copy, " * ".join(str(num) for num in dividers)))

    mul = 1
    for divider in dividers:
        mul *= divider
    assert mul == n_copy


def division():
    while True:
        cmd = int(input("1 Создать БД из произведений простых чисел\n2 Метод пробного деления\n\nВведите команду: "))
        if cmd == 1:
            create_database()
        elif cmd == 2:
            division_method()
        else:
            return


if __name__ == '__main__':
    division()
