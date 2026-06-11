import math

# ---------- Prime Check ----------
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

# ---------- Input p and q ----------
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))

if not is_prime(p) or not is_prime(q):
    print("Error! p and q must be prime numbers.")
    exit()

# ---------- Calculate n and phi(n) ----------
n = p * q
phi = (p - 1) * (q - 1)

print("\nn =", n)
print("phi(n) =", phi)

# ---------- Find valid e values ----------
print("\nPossible values of e:")

for i in range(2, phi):
    if math.gcd(i, phi) == 1:
        print(i, end=" ")

e = int(input("\n\nChoose e: "))

# ---------- Find d ----------

print("\nFinding d using:")
print(f"e × d ≡ 1 (mod {phi})")

d = 1

while True:

    result = (e * d) % phi

    print(f"({e} × {d}) mod {phi} = {result}")

    if result == 1:
        break

    d += 1

print("\nTherefore, d =", d)
print("only selecting the d value which always smallest positive number which lies between 1 and phi(n)")

# ---------- Keys ----------
print("\nPublic Key  =", (e, n))
print("Private Key =", (d, n))

# ---------- Encryption ----------
pt = int(input("\nEnter Plain Text: "))

ct = (pt ** e) % n

print("\nEncryption")
print(f"CT = {pt}^{e} mod {n}")
print("Cipher Text =", ct)

# ---------- Decryption ----------
decrypted_pt = (ct ** d) % n

print("\nDecryption")
print(f"PT = {ct}^{d} mod {n}")
print("Recovered Plain Text =", decrypted_pt)