import math

def Kaziski():

    # Cчитываем криптограмму
    with open('shifrtext.txt', 'r') as f:
        shift_text = f.read()

    shift_text = shift_text.replace(" ", "")

    #Сделаем проход по 3 грамма

    dict_three = {}

    for i in range(len(shift_text) - 2):
        trigram = shift_text[i:i + 4]
        if trigram not in dict_three:
            dict_three[trigram] = 1
        else:
            dict_three[trigram] += 1

    #Удаление из словаря всех триграм с количеством 1 и 2

    new_dict_three = {}

    for key in dict_three:
        if dict_three[key] != 1 and dict_three[key] != 2 and dict_three[key] != 3 and dict_three[key] != 4:
            new_dict_three[key] = dict_three[key]

    print(new_dict_three)

    #Ищем НОД

    for key in new_dict_three:
        new_dict_three[key] = []

    print(new_dict_three)

    for key in new_dict_three:
        for i in range(len(shift_text) - 2):
            trigram = shift_text[i:i + 4]
            if key == trigram:
                new_dict_three[key].append(i)
    print(new_dict_three)


    #Вычисляем расстояния
    rasst = {}

    for key in new_dict_three:
        rasst[key] = []
        for k in new_dict_three[key]:
            for j in new_dict_three[key]:
                help = abs(j - k)
                rasst[key].append(help)

    print(rasst)

    # nod = math.gcd(*rasst["vte"])
    # print(nod)
    # nod = math.gcd(*rasst["tei"])
    # print(nod)
    # nod = math.gcd(*rasst["mse"])
    # print(nod)
    # nod = math.gcd(*rasst["een"])
    # print(nod)
    # nod = math.gcd(*rasst["hee"])
    # print(nod)
    # nod = math.gcd(*rasst["eet"])
    # print(nod)
    # nod = math.gcd(*rasst["eir"])
    # print(nod)

    # nod = math.gcd(*rasst["steir"])
    # print(nod)
    # nod = math.gcd(*rasst["rvted"])
    # print(nod)
    # nod = math.gcd(*rasst["teirv"])
    # print(nod)

Kaziski()