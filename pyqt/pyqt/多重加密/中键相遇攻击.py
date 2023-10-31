from pyqt.s_aes import encrypt, decrypt

def middle_encrypt(ptext, key):
    ctext = encrypt(ptext, key)
    return ctext


def middle_decrypt(ctext, key):
    ptext = decrypt(ctext, key)
    return ptext

def meet_in_the_middle_attack(ciphertext1, plaintext1, ciphertext2, plaintext2):
    """
    中间相遇攻击
    """
    key_space = range(2**16)  # 16位密钥空间

    # 构建中间值字典
    intermediate_values = {}
    for k1 in key_space:
        intermediate1 = middle_encrypt(plaintext1, k1)
        intermediate_values[intermediate1] = k1

    # 在中间值字典中搜索匹配
    for k2 in key_space:
        intermediate2 = middle_decrypt(ciphertext2, k2)
        if intermediate2 in intermediate_values:
            k1 = intermediate_values[intermediate2]
            return k1

    return None

# 两对密文-明文对
ciphertext1 = 0x1234
plaintext1 = 0x5678
ciphertext2 = 0x9abc
plaintext2 = 0xdef0

# 执行中间相遇攻击
key = meet_in_the_middle_attack(ciphertext1, plaintext1, ciphertext2, plaintext2)

print("找到的密钥：", hex(key))