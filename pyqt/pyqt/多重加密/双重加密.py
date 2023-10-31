from pyqt.s_aes import mult, intToVec, sub4NibList, shiftRow, addKey, sBox, w, vecToInt, sBoxI


def keyExp(key1, key2):


    def sub2Nib(b):

        return sBox[b >> 4] + (sBox[b & 0x0f] << 4)

    Rcon1, Rcon2 = 0b10000000, 0b00110000

    w[0] = (key1 & 0xff00) >> 8
    w[1] = key1 & 0x00ff
    w[2] = w[0] ^ Rcon1 ^ sub2Nib(w[1])
    w[3] = w[2] ^ w[1]

    w[4] = (key2 & 0xff00) >> 8
    w[5] = key2 & 0x00ff


def double_encrypt(ptext, key1, key2):


    keyExp(key1, key2)

    def mixCol(s):
        return [s[0] ^ mult(4, s[2]), s[1] ^ mult(4, s[3]),
                s[2] ^ mult(4, s[0]), s[3] ^ mult(4, s[1])]

    state = intToVec(((w[0] << 8) + w[1]) ^ ptext)
    state = sub4NibList(sBox, state)
    state = shiftRow(state)
    state = mixCol(state)

    # Double encryption
    state = addKey(intToVec((w[2] << 8) + w[3]), state)
    state = sub4NibList(sBox, state)
    state = shiftRow(state)
    state = mixCol(state)

    return vecToInt(addKey(intToVec((w[4] << 8) + w[5]), state))


def double_decrypt(ctext, key1, key2):


    keyExp(key1, key2)

    def iMixCol(s):
        return [mult(9, s[0]) ^ mult(2, s[2]), mult(9, s[1]) ^ mult(2, s[3]),
                mult(9, s[2]) ^ mult(2, s[0]), mult(9, s[3]) ^ mult(2, s[1])]

    state = intToVec(ctext)


    state = addKey(intToVec((w[4] << 8) + w[5]), state)
    state = iMixCol(state)
    state = shiftRow(state)
    state = sub4NibList(sBoxI, state)

    state = addKey(intToVec((w[2] << 8) + w[3]), state)
    state = iMixCol(state)
    state = shiftRow(state)
    state = sub4NibList(sBoxI, state)

    state = addKey(intToVec((w[0] << 8) + w[1]), state)

    return vecToInt(state)

if __name__=="__main__":
    plaintext = 0x1234
    key1 = 0x5678
    key2 = 0x9abc

    ciphertext = double_encrypt(plaintext, key1, key2)
    decryptedtext = double_decrypt(ciphertext, key1, key2)

    print("原文:", hex(plaintext))
    print("密钥:",key1,key2)
    print("密文:", hex(ciphertext))
    print("解密:", hex(decryptedtext))