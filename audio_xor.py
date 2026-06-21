# Linear Congruential Generator (LCG) based Audio Encryption & Decryption

filename = input("Enter Audio File Name: ")

# Read original audio file
with open(filename, "rb") as file:
    data = bytearray(file.read())

initial_key = 123

# --------------------------------------------------
# LCG KEY GENERATION TABLE
# --------------------------------------------------

print("\nLCG KEY GENERATION")
print("=" * 65)
print("| Step        | Calculation                 | Generated Key |")
print("-" * 65)

key = initial_key
print(f"| Initial Key | Given                       | {key:<13} |")

for i in range(1, 6):
    prev = key
    key = (key * 17 + 29) % 256

    calc = f"(17*{prev}+29)%256"
    print(f"| K{i:<10}| {calc:<27} | {key:<13} |")

print("=" * 65)

# --------------------------------------------------
# ENCRYPTION TABLE
# --------------------------------------------------

print("\n" + "=" * 80)
print("                         AUDIO ENCRYPTION TABLE")
print("=" * 80)
print("| Byte No | Original Byte | LCG Key | XOR Operation | Encrypted Byte |")
print("-" * 80)

key = initial_key

for i in range(min(10, len(data))):
    original = data[i]

    key = (key * 17 + 29) % 256
    encrypted = original ^ key

    xor_text = f"{original}^{key}"

    print(f"| {i+1:<7} | {original:<13} | {key:<7} | {xor_text:<13} | {encrypted:<14} |")

print("=" * 80)

# --------------------------------------------------
# ENCRYPTION
# --------------------------------------------------

key = initial_key

for i in range(len(data)):
    key = (key * 17 + 29) % 256
    data[i] ^= key

with open("encrypted_audio.mp3", "wb") as file:
    file.write(data)

print("\nAudio Encrypted Successfully!")

# --------------------------------------------------
# DECRYPTION DISPLAY TABLE
# --------------------------------------------------

with open("encrypted_audio.mp3", "rb") as file:
    encrypted_data = bytearray(file.read())

print("\n" + "=" * 80)
print("                         AUDIO DECRYPTION TABLE")
print("=" * 80)
print("| Byte No | Encrypted Byte | LCG Key | XOR Operation | Original Byte |")
print("-" * 80)

key = initial_key

for i in range(min(10, len(encrypted_data))):
    encrypted = encrypted_data[i]

    key = (key * 17 + 29) % 256
    decrypted = encrypted ^ key

    xor_text = f"{encrypted}^{key}"

    print(f"| {i+1:<7} | {encrypted:<14} | {key:<7} | {xor_text:<13} | {decrypted:<13} |")

print("=" * 80)

# --------------------------------------------------
# DECRYPTION
# --------------------------------------------------

key = initial_key

for i in range(len(encrypted_data)):
    key = (key * 17 + 29) % 256
    encrypted_data[i] ^= key

with open("decrypted_audio.mp3", "wb") as file:
    file.write(encrypted_data)

print("\nAudio Decrypted Successfully!")