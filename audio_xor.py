key = 50

filename = input("Enter Audio File Name: ")

with open(filename, "rb") as file:
    data = bytearray(file.read())

print("\nByte\tOriginal\tEncrypted\tDecrypted")

for i in range(min(10, len(data))):

    original = data[i]

    encrypted = original ^ key

    decrypted = encrypted ^ key

    print(i + 1, "\t", original, "\t\t", encrypted, "\t\t", decrypted)

# Encryption
for i in range(len(data)):
    data[i] = data[i] ^ key

with open("encrypted_audio.mp3", "wb") as file:
    file.write(data)

print("\nAudio Encrypted Successfully!")

# Decryption
for i in range(len(data)):
    data[i] = data[i] ^ key

with open("decrypted_audio.mp3", "wb") as file:
    file.write(data)

print("Audio Decrypted Successfully!")