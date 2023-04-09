import random

# Создаем алфавит символов
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+={}[]|\:;"<>,.?/~` '

# Генерируем две случайные последовательности длиной 100 символов
sequence1 = ''.join(random.choice(alphabet) for _ in range(100))
sequence2 = ''.join(random.choice(alphabet) for _ in range(100))

# Вычисляем индекс совпадения
index = 0
for i in range(100):
    if sequence1[i] == sequence2[i]:
        index += 1

index /= 100


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


# Выводим результаты
print('Первая последовательность:', sequence1)
print('Вторая последовательность:', sequence2)
print('Индекс совпадения:', index)
print(f'Средний индекст совпадения: {middle_index}')