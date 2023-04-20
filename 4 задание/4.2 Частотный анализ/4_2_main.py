import collections

INPUT_FILE = "text.txt"
OUTPUT_FILE = "frequencies.txt"
ALPHABET_FILE = "alphabet.txt"

with open(INPUT_FILE, "r") as input_file:
    text = input_file.read()
    character_counts = collections.Counter(text)


total_characters = sum(character_counts.values())

character_frequencies = {char: count / total_characters for char, count in character_counts.items()}

sorted_characters = sorted(character_frequencies.items(), key=lambda x: x[1], reverse=True)

alphabet_text = [i[0] for i in sorted_characters]

with open(OUTPUT_FILE, "w") as output_file:
    for char, freq in sorted_characters:
        output_file.write(f"{char}: {freq:.4f}\n")


def encrypt_text(text):
    print("Введите сдвиг = ", end = "")
    shift = int(input())
    # Читаем алфавит из файла
    with open(ALPHABET_FILE, 'r', encoding='utf-8') as f:
        alphabet = f.read().strip()

    # Создаем таблицу подстановки
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    substitution_table = str.maketrans(alphabet, shifted_alphabet)

    # Применяем подстановку и записываем криптограмму в файл
    with open("cryptogramma.txt", 'w', encoding='utf-8') as f:
        encrypted_text = text.translate(substitution_table)
        f.write(encrypted_text)


def frequencies_cryptogramm():
    INPUT_FILE = "cryptogramma.txt"
    OUTPUT_FILE = "frequencies_cryptogramma.txt"
    ALPHABET_FILE = "alphabet.txt"

    with open(INPUT_FILE, "r") as input_file:
        text = input_file.read()
        character_counts = collections.Counter(text)

    total_characters = sum(character_counts.values())

    character_frequencies = {char: count / total_characters for char, count in character_counts.items()}

    sorted_characters = sorted(character_frequencies.items(), key=lambda x: x[1], reverse=True)



    with open(OUTPUT_FILE, "w") as output_file:
        for char, freq in sorted_characters:
            output_file.write(f"{char}: {freq:.4f}\n")

    alphabet_cryptogram = [i[0] for i in sorted_characters]
    return alphabet_cryptogram

def izoton_image(alphabet_text, alphabet_cryptogram):
    for i in range(len(alphabet_text)):
        print(f'{alphabet_text[i]} -> {alphabet_cryptogram[i]}')


def check_text_with_izoton(alphabet_text, alphabet_cryptogram):
    izoton_dict = {}
    for i in range(len(alphabet_text)):
        izoton_dict[alphabet_cryptogram[i]] = alphabet_text[i]


    with open('cryptogramma.txt', "r") as output_file:
            cryptogramma = output_file.read()

    izoton_crypto = ''
    for i in cryptogramma:
        izoton_crypto += izoton_dict[i]

    with open('text_with_izoton', "w") as output_file:
        output_file.write(izoton_crypto)


encrypt_text(text)
alphabet_cryptogram = frequencies_cryptogramm()
izoton_image(alphabet_text, alphabet_cryptogram)
check_text_with_izoton(alphabet_text, alphabet_cryptogram)

