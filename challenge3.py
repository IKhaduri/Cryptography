import string
import binascii

cur_max_score = -10000000
cur_best_choice = ""


def xor_two(c, b):
    res = []
#stackoverflow
    for i in binascii.unhexlify(c):
        res.append(chr(b ^ i))
    return ''.join(res)


def check(text, sym):
    dexor = xor_two(text, sym)
    # stackoverflow suggestion
    if not (all([TT in string.printable for TT in dexor])):
        return False, False
    return True, dexor

#wikipedia
freq_map = {'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253,
            'e': 12.702,
            'f': 2.228,
            'g': 2.015,
            'h': 6.094,
            'i': 6.966,
            'j': 0.153,
            'k': 0.772,
            'l': 4.025,
            'm': 2.406,
            'n': 6.749,
            'o': 7.507,
            'p': 1.929,
            'q': 0.095,
            'r': 5.987,
            's': 6.327,
            't': 9.056,
            'u': 2.758,
            'v': 0.978,
            'w': 2.360,
            'x': 0.150,
            'y': 1.974,
            'z': 0.074}


def getScore(text):
    sc = 0
    for i in text:
        if i in freq_map:
            sc += freq_map[i]
    return sc


a = str(input()).strip()
for i in range(0, 256):
    T, P = check(a, i)
    if T:
        score = getScore(P)
        if score > cur_max_score:
            cur_best_choice = P
            cur_max_score = score
print(cur_best_choice)