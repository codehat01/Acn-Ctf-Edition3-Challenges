def expand_key(plaintext, key):
    expanded_key = key
    while len(expanded_key) < len(plaintext):
        expanded_key += key
    return expanded_key[:len(plaintext)]

def xor_bytes(plaintext, expanded_key):
    return [ord(p) ^ ord(k) for p, k in zip(plaintext, expanded_key)]

def permute_byte(byte, permutation_table):
    permuted_byte = 0
    for i, pos in enumerate(permutation_table):
        permuted_byte |= ((byte >> (7 - pos)) & 0x01) << (7 - i)
    return permuted_byte

def permute_bytes(xor_result, permutation_table):
    return [permute_byte(byte, permutation_table) for byte in xor_result]

def encrypt(plaintext, key):
    expanded_key = expand_key(plaintext, key)
    xor_result = xor_bytes(plaintext, expanded_key)

    permutation_table = [2, 4, 1, 7, 3, 5, 0, 6]
    permuted_result = permute_bytes(xor_result, permutation_table)

    ciphertext = ''.join(format(byte, '02X') for byte in permuted_result)
    return ciphertext

# Example usage:
plaintext = ""
key = ""
ciphertext = encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")
