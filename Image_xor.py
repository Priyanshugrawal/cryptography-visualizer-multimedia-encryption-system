from PIL import Image

filename = input("Enter Image Name: ")

img = Image.open(filename)

key = 50

pixels = img.load()

print("\nPixel\tOriginal\tEncrypted")

count = 0

for x in range(img.width):
    for y in range(img.height):

        r, g, b = pixels[x, y]

        if count < 5:
            print(count + 1, "\t", (r, g, b), end="")

        r = r ^ key
        g = g ^ key
        b = b ^ key

        pixels[x, y] = (r, g, b)

        if count < 5:
            print("\t", (r, g, b))

        count += 1

img.save("output.jpg")

print("\nImage Processed Successfully!")