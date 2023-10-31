from s_aes import encrypt
from s_aes import decrypt

def encrypt_ansii(plaintext ,key):
    # Convert plaintext to a 16-bit value
    plaintext_value = (ord(plaintext[0]) << 8) + ord(plaintext[1])

    ciphertext = encrypt(plaintext_value, key)
    ciphertext_byte1 = chr((ciphertext >> 8) & 0xFF)
    ciphertext_byte2 = chr(ciphertext & 0xFF)

    return ciphertext_byte1 + ciphertext_byte2


def decrypt_ansii(ciphertext,key):
    ciphertext_value = (ord(ciphertext[0]) << 8) + ord(ciphertext[1])
    decrypted_plaintext_value = decrypt(ciphertext_value, key)
    decrypted_plaintext = chr(decrypted_plaintext_value >> 8) + chr(decrypted_plaintext_value & 0xFF)
    return decrypted_plaintext
    pass
if __name__=="__main__":
    plaintext = "ab"
    key = 0x3c2d
    print("明文:",plaintext)
    print("密钥:",key)
    ciphertext = encrypt_ansii(plaintext, key)
    print("扩展加密密文:", ciphertext)
    decrypted_plaintext_value = decrypt_ansii(ciphertext, key)
    print("扩展加密解密:", decrypted_plaintext_value)