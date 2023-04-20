import random

def shifr():

    file = open("opentext.txt", "r")
    text = file.read().lower()
    text = text.replace(" ", "")
    file.close()

    print("Введите длину ключу, моноциклической перестановки = ", end = '')
    n = int(input())
    n_list = [i for i in range(n)]
    random.shuffle(n_list)
    print(f'Выводим порядок {n_list}')

    file = open("key.txt", "w")
    for i in n_list:
        file.write(str(i))
        file.write(' ')
    file.close()

    blocks = [text[i:i + n] for i in range(0, len(text), n)]
    count_blocks = len(blocks) - 1

    if len(blocks[count_blocks]) < n:
        blocks[count_blocks] = blocks[count_blocks] + ' ' * (n - len(blocks[count_blocks]))

    new_blocks = []


    shifr_text = ""
    for i in blocks:
        str_help = ''
        for j in n_list:
             str_help += i[j]
        new_blocks.append(str_help)
        shifr_text += str_help
    print(f'Выводим новые блоки {new_blocks}')
    print(f'Выводим шифртекст {shifr_text}')

    file = open("shifrtext.txt", "w")

    file.write(shifr_text)

    file.close()


def deshifr():

    file = open("key.txt", "r")
    n_list = list(map(int, file.read().split()))
    file.close()

    n = len(n_list)

    file = open("shifrtext.txt", "r")
    shifrtext = file.read()
    file.close()

    blocks = [shifrtext[i:i + n] for i in range(0, len(shifrtext), n)]

    # help_massiv = [1] * 3
    # print(help_massiv)

    deshifr_text = ''

    print(blocks)

    for i in blocks:
        str_help = ''
        help_massiv = [1] * len(n_list)
        k = 0
        for j in n_list:
            help_massiv[j] = i[k]
            k += 1
        for j in help_massiv:
            str_help += str(j)
        deshifr_text += str_help

    file = open("deshifrtext.txt", "w")
    file.write(deshifr_text)
    file.close()

shifr()
deshifr()

