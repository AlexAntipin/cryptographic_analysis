import random
import string

alphabet = string.ascii_lowercase  # алфавит на английском языке
# генерируем две последовательности из 100 символов
sequence1 = [random.choice(alphabet) for _ in range(100)]
sequence2 = [random.choice(alphabet) for _ in range(100)]

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


print(f"Первая последовательность: {''.join(sequence1)}")
print(f"Вторая последовательность: {''.join(sequence2)}")
print(f"Индекс совпадения: {index_of_coincidence}")
print(f'Средний индекст совпадения: {middle_index}')