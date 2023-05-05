import sympy
import random
import math



def step_1():
    print('Введите длину простых чисел p и q = ', end = '')
    n_len = int(input())

    n_left = 10 ** (n_len - 1)
    n_right = 10 ** n_len

    p = random.randint(n_left, n_right)
    while not sympy.isprime(p):
        p = random.randint(n_left, n_right)

    q = random.randint(n_left, n_right)
    while not sympy.isprime(q):
        q = random.randint(n_left, n_right)

    f = open('Простые числа.txt', 'w')
    f.write(str(p) + ' ' + str(q))
    f.close()


    n = p * q
    fi_n = (p - 1) * (q - 1)

    # Вычисление e
    e = random.randint(1, fi_n)
    while math.gcd(e, fi_n) != 1:
        e = random.randint(1, fi_n)


    #Вычисление d
    d = pow(e, -1, fi_n)

    f = open('Открытый ключ.txt', 'w')
    f.write(str(n) + ' ' + str(e))
    f.close()

    with open("Закрытый ключ.txt", "w") as f:
        f.write(str(d))

    with open("fi_n.txt", "w") as f:
        f.write(str(fi_n))

    with open("n.txt", "w") as f:
        f.write(str(n))

def step_2():

    fi_n, n, p, q = 0, 0, 0, 0


    with open("fi_n.txt", "r") as f:
        fi_n = int(f.read())

    with open("n.txt", "r") as f:
        n = int(f.read())

    with open('Простые числа.txt', 'r') as f:
        p, q = f.read().split()

    p = int(p); q = int(q)

    #Решаем квадратное уравнение
    a = 1
    b = -1 * (n - fi_n + 1)
    c = n

    # вычисляем дискриминант
    discreminant = b ** 2 - 4 * a * c

    # проверяем, есть ли корни уравнения
    if discreminant < 0:
        print("Корней нет")
    elif discreminant == 0:
        x = -b / (2 * a)
        print("Уравнение имеет один корень: x =", x)
    else:
        x1 = (-b + math.sqrt(discreminant)) / (2 * a)
        x2 = (-b - math.sqrt(discreminant)) / (2 * a)
        print("Уравнение имеет два корня: x1 =", x1, "и x2 =", x2)

def step_3():

    f = open('Открытый ключ.txt', 'r')
    n, e = f.read().split()
    n = int(n); e = int(e)
    f.close()
    d = ''
    with open("Закрытый ключ.txt", "r") as f:
        d = int(f.read())
    print(d)

    #1 подшаг
    number = e * d - 1
    print(number)
    f = 0
    while number % 2 == 0:
        number /= 2
        f += 1
    number = int(number)
    s = number

    #2 подшаг
    while True:
        a = random.randint(2, n - 2)
        u = pow(a, s, n)
        v = pow(u, 2, n)

        #3 подшаг
        while v != 1:
            u = v
            v = pow(u, 2 , n)
            if u == -1:
                break
        else:
            p = math.gcd(u - 1, n)
            q = math.gcd(u + 1, n)
            print("Уравнение имеет два корня: x1 =", p, "и x2 =", q)
            break








def main():
    while True:
        opt = input('1 - Генерация параметров\n'
                    '2 - Разложение по значению функции эйлера\n'
                    '3 - Разложение по известным показателям\n'
                    '4 - Выход из программы\n')
        if opt == '1':
            step_1()
        elif opt == '2':
            step_2()
        elif opt == '3':
            step_3()
        elif opt == '4':
            exit()


if __name__ == '__main__':
    main()
