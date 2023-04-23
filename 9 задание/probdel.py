from itertools import combinations_with_replacement


def create_base():

    #Считываем файл с простыми множителям
    with open("base_simple_multiplier.txt", "r") as f:
        numbers = list(map(int, f.read().split()))
        print(numbers)

    print("Введите параметр t = ", end = '')
    t = int(input())

    answer = combinations_with_replacement(numbers, t)
    dict_mult = {}

    for i in numbers:
        dict_mult[i] = [i]

    for i in answer:
        mult = 1
        for j in i:
            mult *= j
        dict_mult[mult] = i

    print(dict_mult)

    sorted_dict_mult = sorted(dict_mult.items(), reverse = True)

    print(sorted_dict_mult)

    #Записываем Наши множители
    # with open("base.txt", "w") as f:

    return sorted_dict_mult

def method_probn_del(sorted_dict_mult):
    print("Введите число = ", end = '')
    n = int(input())
    mnog = []
    for i in sorted_dict_mult:
        while n % i[0] == 0:
            for j in i[1]:
                mnog.append(j)

            n /=  i[0]
    mnog.sort()
    for i in mnog:
        print(i, end = " ")

p = create_base()
method_probn_del(p)

