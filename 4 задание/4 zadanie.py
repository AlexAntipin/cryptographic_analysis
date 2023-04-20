ALPHABET_FILE = "alphabet.txt"
SHIFT_FILE = "shift.txt"
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"

# Load the alphabet from the file
with open(ALPHABET_FILE, "r") as f:
    alphabet = f.readline().strip()

# Load the shift from the file
with open(SHIFT_FILE, "r") as f:
    shift = int(f.readline())

# Create a dictionary to map each letter to its shifted position
shifted_alphabet = {}
for i in range(len(alphabet)):
    shifted_position = (i + shift) % len(alphabet)
    shifted_letter = alphabet[shifted_position]
    shifted_alphabet[alphabet[i]] = shifted_letter

# Read the input file and encrypt the text using the shifted alphabet
with open(INPUT_FILE, "r") as input_file:
    plaintext = input_file.read().strip()
    ciphertext = ""
    for letter in plaintext:
        if letter in alphabet:
            ciphertext += shifted_alphabet[letter]
        else:
            ciphertext += letter

# Write the ciphertext to the output file
with open(OUTPUT_FILE, "w") as output_file:
    output_file.write(ciphertext)