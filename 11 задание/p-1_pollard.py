import math
import random


# def primes(n):
#     primes_list = []  # создаем пустой список для хранения простых чисел
#     for num in range(2, n + 1):  # перебираем все числа от 2 до n
#         is_prime = True  # считаем, что число простое, пока не доказано обратное
#         for i in range(2, num):  # перебираем все числа от 2 до num-1
#             if num % i == 0:  # если число num делится на i без остатка
#                 is_prime = False  # то число num не является простым
#                 break  # выходим из цикла, так как уже доказали, что число num не простое
#         if is_prime:  # если число num оказалось простым
#             primes_list.append(num)  # добавляем его в список простых чисел
#     return primes_list  # возвращаем список простых чисел



def primes():
    primes_list = []
    with open("../9 задание/primes_database.txt", "r") as f:
        for line in f:
            number = int(line[:-1])
            primes_list.append(number)

    return primes_list[:-1]

def p_1_pollard():

    print("Введите нечетное n = ", end='')
    n = int(input())
    #print("Введите ограничение по базе с = ", end='')
    #c = int(input())

    #1 шаг алгоритма
    base = primes()

    #2 шаг алгоритма
    a = random.randint(2, n - 2)
    d = math.gcd(a, n)
    if d >= 2:
        p = d
        return p
    #3 шаг
    flag = True

    for i in range(len(base)):
        l = int(math.log(n) / math.log(base[i]))
        a = pow(a, base[i] ** l, n)
        d = math.gcd(a - 1, n)
        if d == 1 or d == n:
            flag = False
        else:
            p = d
            return p

    if not flag:
        print("Делитель не найден")



print(p_1_pollard())