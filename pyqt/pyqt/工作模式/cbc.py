from random import randint

from pyqt.s_aes import encrypt, decrypt


def generate_iv():
    """生成16位的初始向量"""
    return randint(0, 0xFFFF)

def encrypt_cbc(plaintext, key):
    """使用CBC模式加密明文消息"""
    iv = generate_iv()  # 生成初始向量
    ciphertext = []
    previous_block = iv

    for block in plaintext:
        # CBC模式加密操作
        block = block ^ previous_block  # 异或当前明文块与前一个密文块
        encrypted_block = encrypt(block, key)  # 使用S-AES加密当前块
        ciphertext.append(encrypted_block)
        previous_block = encrypted_block

    return iv, ciphertext

def decrypt_cbc(ciphertext, key, iv):
    """使用CBC模式解密密文消息"""
    plaintext = []
    previous_block = iv

    for block in ciphertext:
        # CBC模式解密操作
        decrypted_block = decrypt(block, key)  # 使用S-AES解密当前密文块
        decrypted_block = decrypted_block ^ previous_block  # 异或解密结果与前一个密文块
        plaintext.append(decrypted_block)
        previous_block = block

    return plaintext

if __name__=="__main__":
    plaintext = [0x1234, 0x5678, 0x9ABC, 0xDEF0]  # 明文消息
    key = 0b11001100110011  # 密钥
    print("原文:",[hex(block) for block in plaintext])

    print("密钥:",bin(key))
    # 加密
    iv, ciphertext = encrypt_cbc(plaintext, key)
    print("初始向量:", hex(iv))
    print("密文消息:", [hex(block) for block in ciphertext])
    decrypted_plaintext = decrypt_cbc(ciphertext, key, iv)
    print("解密后的明文消息:", [hex(block) for block in decrypted_plaintext])
    ciphertext[0] +=1
    ciphertext[1] +=1
    ciphertext[2] +=1
    ciphertext[3] +=1

    print("修改密文:",[hex(block) for block in ciphertext])

    # 解密
    decrypted_plaintext = decrypt_cbc(ciphertext, key, iv)
    print("解密后的明文消息:", [hex(block) for block in decrypted_plaintext])