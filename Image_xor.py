from PIL import Image

# Load image
img = Image.open("images.jpg").convert("RGB")
pixels = img.load()

# Print image information
print("==============================================================")
print("               IMAGE INFORMATION")
print("==============================================================")
print(f"Image Width  : {img.width} pixels")
print(f"Image Height : {img.height} pixels")
print(f"Total Pixels : {img.width * img.height}")
print("==============================================================\n")

# Generate Fibonacci numbers modulo 256
fib = [1, 1]
total = img.width * img.height * 3 # 3 for R, G, B channels

for i in range(2, total):
    fib.append((fib[i - 1] + fib[i - 2]) % 256)

k = 0
count = 0
max_print = 10

print("===========================================================================")
print("Pixel\tOriginal RGB\t\tKeys Used\t\tEncrypted RGB")
print("===========================================================================")

for y in range(img.height):
    for x in range(img.width):

        # Original RGB values
        r, g, b = pixels[x, y]
        original = (r, g, b)

        # Fibonacci keys
        key_r = fib[k]
        r ^= key_r
        k += 1

        key_g = fib[k]
        g ^= key_g
        k += 1

        key_b = fib[k]
        b ^= key_b
        k += 1

        encrypted = (r, g, b)

        # Store encrypted pixel
        pixels[x, y] = encrypted

        # Print only first 10 pixels
        if count < max_print:
            print(
                f"({x},{y})\t{original}\t({key_r},{key_g},{key_b})\t{encrypted}"
            )
            count += 1

# Save encrypted image
img.save("encrypted3.png")

print("\n==============================================================")
print("Encryption Completed Successfully!")
print("Encrypted image saved as : encrypted3.png")
print("==============================================================")