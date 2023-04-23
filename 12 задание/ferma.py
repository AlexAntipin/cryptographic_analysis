import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def ferma():
    n = int(input())
    k = int(input())
    l = int(input())

    i = 1
    while True:
        s = int(math.sqrt(k * n)) + i
        if math.sqrt(s ** 2 - k * n) % 1 == 0:
            print(f'Проверка {math.sqrt(s ** 2 - k * n)}')
            t = int(math.sqrt(s ** 2 - k * n))
            #print(f'Выводим t {t}')
            #print(f'Выводим s {s}')
            p = math.gcd(k * n, s - t)
            #print(f'Выводим kn {k * n} и выводим s - t {s-t}')
            print(p)
            break
        i += 1
        if i % l == 0:
            #print("прошло l вычислений. Осуществить следующие l вычислений: Y/N")
            answwer = input()
            if answwer == "Y":
                continue
            else:
                break

ferma()