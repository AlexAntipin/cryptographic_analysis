# открытие файла с текстом
with open("text.txt", "r") as f:
    text = f.read()

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