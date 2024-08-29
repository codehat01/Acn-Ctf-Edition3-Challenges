from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

key = RSA.generate(2048)
public_key = key.publickey().export_key()
private_key = key.export_key()

def encrypt_rsa(plaintext, public_key):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    return binascii.hexlify(cipher.encrypt(plaintext.encode())).decode()

plaintext = "Your message here"
ciphertext = encrypt_rsa(plaintext, public_key)

print(f"{public_key.decode()}\n{ciphertext}")
