import random

def index_of_coincidence(sequence1, sequence2, alphabet):
    # вычисляем индекс совпадения (индексацию начинаем с 1)

    matches = 0
    for i in range(100):
        if sequence1[i] == sequence2[i]:
            matches += 1

    index_of_coincidence = matches / 100

    frequency1 = {char: 0 for char in alphabet}
    for char in sequence1:
        frequency1[char] += 1

    frequency2 = {char: 0 for char in alphabet}
    for char in sequence2:
        frequency2[char] += 1

    middle_index = 0
    for i in alphabet:
        index_char = frequency1[i] / 100 * frequency2[i] / 100
        middle_index += index_char

    return index_of_coincidence, middle_index


# Считываем английский алфавит из файла
with open('english_alphabet.txt', 'r') as f:
    english_alphabet = f.read().strip()

# Считываем ключ из файла
with open('key.txt', 'r') as f:
    key = f.read().strip()

# Генерируем случайную строку из 100 английских букв
plaintext = ''.join(random.choices(english_alphabet, k = 100))

# Шифруем строку с помощью шифра Виженера
ciphertext = ''
for i in range(len(plaintext)):
    pi = english_alphabet.index(plaintext[i])
    ki = english_alphabet.index(key[i % len(key)])
    ci = (pi + ki) % len(english_alphabet)
    ciphertext += english_alphabet[ci]

# Генерируем 15 случайных сдвигов для строки
shifts = []
for j in range(16):
    shift = j
    shifted_plaintext = plaintext[shift:] + plaintext[:shift]
    shifts.append(shift)

    # Шифруем сдвинутую строку с помощью шифра Виженера
    shifted_ciphertext = ''
    for i in range(len(shifted_plaintext)):
        pi = english_alphabet.index(shifted_plaintext[i])
        ki = english_alphabet.index(key[i % len(key)])
        ci = (pi + ki) % len(english_alphabet)
        shifted_ciphertext += english_alphabet[ci]

    index, middle_index = index_of_coincidence(plaintext, shifted_ciphertext, english_alphabet)
    print(f"Сдвиг = {j}")
    print(f"Индекс совпадения шифрограммы и исходного текста = {index}")
    print(f"Средний индекс совпадения  = {middle_index}")


# Сохраняем сдвиги в файл
with open('shifts.txt', 'w') as f:
    for shift in shifts:
        f.write(str(shift) + '\n')