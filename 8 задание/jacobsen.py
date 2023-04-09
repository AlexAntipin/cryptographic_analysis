import random
import math

with open("text.txt", "r") as f:
    text = f.read()

def bigram_freq_mantrix(text):

    # открытие файла с символами алфавита
    with open("english_alphabet.txt", "r") as f:
        alphabet = f.read().strip()

    # создание словаря для хранения частот биграмм
    freq = {}
    for c1 in alphabet:
        for c2 in alphabet:
            freq[c1+c2] = 0

    # вычисление частот биграмм
    for i in range(len(text)-1):
        if text[i] in alphabet and text[i+1] in alphabet:
            freq[text[i]+text[i+1]] += 1

    # вычисление общего количества биграмм
    total = sum(freq.values())

    # нормализация частот биграмм
    for bigram in freq:
        freq[bigram] /= total

    # вывод эталонной матрицы частот биграмм
    print("     ", end = " ")
    for c1 in alphabet:
        print(c1, end="        ")
    print()

    for c1 in alphabet:
        print(c1, end = " ")
        for c2 in alphabet:
            print("{:.6f}".format(freq[c1+c2]), end=" ")
        print()
    return freq


def shifr_vigener():

    # Считываем английский алфавит из файла
    with open('english_alphabet.txt', 'r') as f:
        english_alphabet = f.read().strip()

    # Считываем ключ из файла
    with open('key.txt', 'r') as f:
        key = f.read().strip()

    # Считываем открытый текст
    with open('text.txt', 'r') as f:
        text = f.read().strip().lower()

    print(text)

    # Генерируем случайную строку из 100 английских букв
    # plaintext = ''.join(random.choices(english_alphabet, k=100))

    plaintext = text

    # Шифруем строку с помощью шифра Виженера
    ciphertext = ''
    for i in range(len(plaintext)):
        pi = english_alphabet.index(plaintext[i])
        ki = english_alphabet.index(key[i % len(key)])
        ci = (pi + ki) % len(english_alphabet)
        ciphertext += english_alphabet[ci]

    # Сохраняем сдвиги в файл
    with open('chiper_text.txt', 'w') as f:
        f.write(ciphertext)

    return ciphertext

def vigenere_decrypt(ciphertext, key, alphabet):
    plaintext = ""
    key_len = len(key)
    key_idx = 0
    for c in ciphertext:
        if c.isalpha():
            c = c.lower()
            k = key[key_idx % key_len].lower()
            p = alphabet[(alphabet.index(c) - alphabet.index(k)) % len(alphabet)]
            plaintext += p.lower()
            key_idx += 1
        else:
            plaintext += c
    return plaintext

def jacobsen():

    #Считываем длину ключа
    with open('period_key.txt', 'r') as f:
        period = int(f.read())

    # Считываем английский алфавит из файла
    with open('english_alphabet.txt', 'r') as f:
        english_alphabet = f.read().strip()

        # Сохраняем сдвиги в файл
    with open('chiper_text.txt', 'r') as f:
        chiper_text = f.read()


    #1 шаг алгоритма, подбираем экспериментальный ключ
    test_key = [random.choice(english_alphabet) for _ in range(period)]

    print(test_key)


    #2 шаг алгоритма, расшифровыываем нашим тестовым ключом

    test_decrypt = vigenere_decrypt(chiper_text, test_key, english_alphabet)

    print(test_decrypt)

    #3 шаг алгоритма, матрица частот биграмм в новом текст, полученным на 2 шаге

    new_freq = bigram_freq_mantrix(test_decrypt)
    freq = bigram_freq_mantrix(text)
    print(new_freq)
    print(freq)


    #4 шаг Вычисляем значение целевой функции
    w_full = 0
    for key in freq:
        w_full += abs(new_freq[key] - freq[key])
    print(f'Выводим значение целочисленной функции = {w_full}')

freq = bigram_freq_mantrix(text)
shifr_vigener()
jacobsen()
print(freq)