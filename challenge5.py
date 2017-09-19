import binascii


def code_to_oblivion(text, xor_key):

    res = []
    #some python tutorial on xoring
    for i in range(len(text)):
        res.append(text[i] ^ xor_key[i % len(xor_key)])
    return bytes(res)

A = input().strip()
B = input().strip()
print(str(binascii.hexlify(code_to_oblivion(bytes(B, encoding="ascii"), bytes(A, encoding="ascii"))))[2:-1])
