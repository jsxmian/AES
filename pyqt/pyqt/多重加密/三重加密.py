from pyqt.s_aes import mult, intToVec, sub4NibList, shiftRow, addKey, sBox, w, vecToInt, sBoxI, decrypt, encrypt


def triple_encrypt(ptext, key):

    k1 = key >> 32
    k2 = (key >> 16) & 0xFFFF
    k3 = key & 0xFFFF
    ctext = encrypt(ptext, k1)
    ctext = encrypt(ctext, k2)
    ctext = encrypt(ctext, k3)
    return ctext


def triple_decrypt(ctext, key):


    k1 = key >> 32
    k2 = (key >> 16) & 0xFFFF
    k3 = key & 0xFFFF
    ptext = decrypt(ctext, k3)
    ptext = decrypt(ptext, k2)
    ptext = decrypt(ptext, k1)

    return ptext

if __name__=="__main__":
    # 三个密钥
    key1 = 0b1100110011001100
    key2 = 0b0101010101010101
    key3 = 0b1111000011110000
    key = (key1 << 32) | (key2 << 16) | key3
    # 明文
    plaintext = 0b1010101010101010
    # 加密
    ciphertext = triple_encrypt(plaintext, key)
    # 解密
    decrypted_text = triple_decrypt(ciphertext, key)

    # 输出结果
    print("原文:", bin(plaintext)[2:].zfill(16))
    print("48位密钥:",bin(key))
    print("密文:", bin(ciphertext)[2:].zfill(16))
    print("解密:", bin(decrypted_text)[2:].zfill(16))