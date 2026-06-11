# DES Structure Demonstration

plaintext = "1010101011001100110011001111000011110000111100001010101010101010"
key = "1111000011110000111100001111000011110000111100001111000011110000"

print("=" * 60)
print("DES ENCRYPTION PROCESS")
print("=" * 60)

# -----------------------------
# STEP 1 : PLAINTEXT
# -----------------------------
print("\nSTEP 1: PLAINTEXT")
print("Plaintext Length :", len(plaintext), "bits")

# -----------------------------
# STEP 2 : KEY
# -----------------------------
print("\nSTEP 2: KEY PROCESSING")
print("Entered Key Length :", len(key), "bits")
print("Parity Bits        : 8 bits")
print("Effective Key      : 56 bits")

#parity bits are ignored in this demonstration, so we will use the first 56 bits of the key
effective_key = ""

for i in range(64):

    if (i + 1) % 8 != 0:
        effective_key += key[i]

print("\nSTEP 2: EFFECTIVE KEY")
print("Effective Key Length :", len(effective_key), "bits")

# -----------------------------
# STEP 3 : SUBKEY GENERATION
# -----------------------------
print("\nSTEP 3: GENERATE 16 SUBKEYS")

subkeys = [] #empty list to hold the 16 subkeys

for i in range(16): 
    subkey = format(i + 1, '048b') 
    subkeys.append(subkey) #Adds the generated subkey into the list.

print("16 Subkeys Generated")
print("Each Subkey Length :", len(subkeys[0]), "bits")

# -----------------------------
# STEP 4 : INITIAL PERMUTATION
# -----------------------------
print("\nSTEP 4: INITIAL PERMUTATION (IP)")

ip = plaintext[::-1]  # simulated IP

print("64 bits rearranged")
print("Output Length :", len(ip), "bits")

# -----------------------------
# STEP 5 : SPLIT
# -----------------------------
L = ip[:32]
R = ip[32:]

print("\nSTEP 5: SPLIT")
#printing the length of l0 and r0
print("L0 Length :", len(L), "bits")
print("R0 Length :", len(R), "bits")

# ====================================================
# 16 ROUNDS
# ====================================================

for round_no in range(16):

    print("\n" + "=" * 60) #formating for better readability
    print(f"ROUND {round_no + 1}") #iteration upto 16 rounds
    print("=" * 60)

    print("\nInput:")
    print("L =", len(L), "bits")
    print("R =", len(R), "bits")

    # ---------------------------------
    # Expansion
    # ---------------------------------

    expanded_R = R + R[:16]

    print("\nExpansion (E-Box)")
    print("32 bits →", len(expanded_R), "bits")

    # ---------------------------------
    # XOR WITH SUBKEY
    # ---------------------------------

    xor_result = "" #empty string to hold the result of the XOR operation

    for a, b in zip(expanded_R, subkeys[round_no]):
        xor_result += str(int(a) ^ int(b))

    print("\nXOR with Subkey")
    print("48 bits XOR 48 bits")
    print("Output Length :", len(xor_result), "bits") #48 bits output from the XOR operation

    # ---------------------------------
    # S-BOX STAGE
    # ---------------------------------

    print("\nS-BOXES")

    sbox_output = ""

    for sbox in range(8):

        six_bits = xor_result[sbox*6:(sbox+1)*6]

        # Simulated S-Box Output
        four_bits = six_bits[:4]

        print(
            f"S{sbox+1}:",
            len(six_bits),
            "bits ->",
            len(four_bits),
            "bits"
        )

        sbox_output += four_bits

    print("Total Output :", len(sbox_output), "bits") # print the final output from the S-Box stage, which is 32 bits

    # ---------------------------------
    # P PERMUTATION
    # ---------------------------------

    permutation = sbox_output[::-1]

    print("\nP-Permutation")
    print("32 bits ->", len(permutation), "bits")

    # ---------------------------------
    # FEISTEL FUNCTION
    # ---------------------------------

    new_R = ""

    for a, b in zip(L, permutation):
        new_R += str(int(a) ^ int(b))

    print("\nFeistel Operation")
    print("L XOR F(R,K)")
    print("Output Length :", len(new_R), "bits")

    # ---------------------------------
    # SWAP
    # ---------------------------------

    new_L = R

    L = new_L
    R = new_R

    print("\nSwap")
    print("New L =", len(L), "bits")
    print("New R =", len(R), "bits")

# ====================================================
# AFTER ROUND 16
# ====================================================

print("\n" + "=" * 60)
print("AFTER ROUND 16")
print("=" * 60)

print("L16 =", len(L), "bits")
print("R16 =", len(R), "bits")

# DES combines R16 + L16
combined = R + L

print("\nCombine R16 + L16")
print("Length :", len(combined), "bits")

# ====================================================
# FINAL PERMUTATION
# ====================================================

ciphertext = combined[::-1]

print("\nFINAL PERMUTATION (FP)")
print("64 bits rearranged")

print("\nCiphertext Length :", len(ciphertext), "bits")

print("\nCIPHERTEXT:")
print(ciphertext)

print("\nDES ENCRYPTION COMPLETED")