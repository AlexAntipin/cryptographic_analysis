import random

# Открыть файлы с алфавитом и открытым текстом
with open('alphabet.txt', 'r') as file:
    alphabet = file.read().rstrip()

with open('plaintext.txt', 'r') as file:
    plaintext = file.read().rstrip()

# Сгенерировать случайный сдвиг
shift = random.randint(1, len(alphabet)-1)

# Зашифровать текст
ciphertext = ''
for char in plaintext:
    if char in alphabet:
        index = (alphabet.index(char) + shift) % len(alphabet)
        ciphertext += alphabet[index]
    else:
        ciphertext += char

# Записать зашифрованный текст в файл
with open('ciphertext.txt', 'w') as file:
    file.write(ciphertext)

# Записать сдвиг в файл
with open('shift.txt', 'w') as file:
    file.write(str(shift))