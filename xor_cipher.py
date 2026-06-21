text = input("Enter Plain Text: ").upper()

key = 5
cipher = ""

print("\nCharacter\tASCII\tXOR 5\tNew ASCII\tNew Char") #COLUMNS

for ch in text:
    ascii_value = ord(ch)
    new_ascii = ascii_value ^ key
    new_char = chr(new_ascii)

    cipher += new_char

    print(ch, "\t\t", ascii_value, "\t", ascii_value, "^5\t", new_ascii, "\t\t", new_char)

print("\nCipher Text:", cipher)

plain = ""

for ch in cipher:
    plain += chr(ord(ch) ^ key)

print("Decrypted Text:", plain) #(A XOR B) XOR B = A