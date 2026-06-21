text = input("Enter Plain Text: ").upper()

cipher = ""

print("\nCharacter\tASCII\t+3\tNew ASCII\tNew Char") #COLUMNS

for ch in text:
    ascii_value = ord(ch)
    new_ascii = ascii_value + 3
    new_char = chr(new_ascii)

    cipher += new_char

    print(ch, "\t\t", ascii_value, "\t+3\t", new_ascii, "\t\t", new_char)

print("\nCipher Text:", cipher)

plain = ""

for ch in cipher:
    plain += chr(ord(ch) - 3)

print("Decrypted Text:", plain)