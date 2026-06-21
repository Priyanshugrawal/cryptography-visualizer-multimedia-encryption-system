# ==========================================================
# AES VISUALIZER (FINAL FIXED VERSION)
# ==========================================================

plaintext = input("Enter 16-character Plain Text : ")
key = input("Enter 16-character Key        : ")

if len(plaintext) != 16 or len(key) != 16:
    print("AES-128 requires exactly 16 characters.")
    exit()

# ==========================================================
# STEP 1 : STATE MATRIX (STORE AS INTEGER FROM START)
# ==========================================================

print("\n========== STEP 1 : STATE MATRIX ==========")
# matrix value will be stored in a ascii values
state = [[ord(ch) for ch in plaintext[i:i+4]] for i in range(0, 16, 4)]

for row in state:
    print(row)

# ==========================================================
# STEP 2 : KEY EXPANSION
# ==========================================================

print("\n========== STEP 2 : KEY EXPANSION ==========")

round_key = [ord(c) for c in key]

print("Original Key :", key)

# simple key shift
round_key = [(x + 1) % 256 for x in round_key]

print("Round Key (numeric):", round_key)

# ==========================================================
# 10 ROUNDS AES
# ==========================================================

for round_no in range(10):

    print(f"\n\n================ ROUND {round_no+1} ================")

    # ==========================================================
    # SUBBYTES (simple demo: XOR with 0x1F)
    # ==========================================================
    print("\n========== STEP 3 : SUBBYTES ==========")

    for i in range(4):
        for j in range(4):
            state[i][j] = state[i][j] ^ 0x1F #hexadecimal value for demonstration xoe with 31
            print(state[i][j], end=" ")
        print()

    # ==========================================================
    # SHIFTROWS
    # ==========================================================
    print("\n========== STEP 4 : SHIFTROWS ==========")

    for i in range(4):
        state[i] = state[i][i:] + state[i][:i]

    for row in state:
        print(row)

    # ==========================================================
    # MIXCOLUMNS (XOR based simplified)
    # ==========================================================
    if round_no != 9:

        print("\n========== STEP 5 : MIXCOLUMNS ==========")

        for col in range(4):

            column = [state[row][col] for row in range(4)]

            mixed = [
                column[0] ^ column[1],
                column[1] ^ column[2],
                column[2] ^ column[3],
                column[3] ^ column[0]
            ]

            for row in range(4):
                state[row][col] = mixed[row]

            print(f"Column {col+1}:", mixed)

    # ==========================================================
    # ADDROUNDKEY
    # ==========================================================
    print("\n========== STEP 6 : ADDROUNDKEY ==========")

    k = 0

    for i in range(4):
        for j in range(4):

            state[i][j] = state[i][j] ^ round_key[k]

            print(state[i][j], end=" ")
            k += 1

        print()

# ==========================================================
# FINAL OUTPUT
# ==========================================================

print("\n========== FINAL CIPHER ==========")

cipher_hex = "".join([format(state[i][j], '02x') for i in range(4) for j in range(4)])
print("Cipher Text (Hex):", cipher_hex)
print("\nAES Completed Successfully.")