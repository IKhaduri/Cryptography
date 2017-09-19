import string
import binascii
#same comments apply as to previous challenges
def xor_two(c, b):
    res = []
    for j in binascii.unhexlify(c):
        res.append(chr(b ^ j))
    return ''.join(res)


def check(text, sym):
    xor_str = xor_two(text, sym)
    if not (all([TT in string.printable for TT in xor_str])):
        return False, False

    return True, xor_str


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

word_list = set(["the", "and", "start", "have", "begin", "end", "hello", "summer", "about", "which", "who",
                     "whom", "where", "there", "here", "now", "never", "captain", "your", "could", "mine", "her",
                     "with", "his", "that", "how", "why", "make", "like", "can", "help", "dislike",
                     "hate", "from", "like", "time", "any", "these", "come", "think", "but", "point", "when",
                     "absolutely",
                     "because", "cause", "hell", "heaven", "paradise", "rick", "morty", "quick", "nimble", "honest",
                     "dumb"," a "," the "," in "])


def get_score(text):
    sc = 0
    for j in text:
        if j in freq_map:
            sc += freq_map[j]
    return sc


def decode_hex(a):
    cur_max_score = -10000000
    cur_best_choice = ""
    xor_key_choice = ''
    for i in range(0, 256):
        t, p = check(a, i)
        if t:
            score = get_score(p)
            if score > cur_max_score:
                cur_best_choice = p
                xor_key_choice = i
                cur_max_score = score
    return cur_best_choice, xor_key_choice


def code_to_oblivion(text, xor_key):
    res = []
    for i in range(len(text)):
        res.append(text[i] ^ xor_key[i % len(xor_key)])
    return bytes(res)


def xor_with_key(a, b):

    return str((code_to_oblivion(bytes(b, encoding="ascii"), bytes(a, encoding="ascii"))))[2:-1]


def getScore(text):
    sc = 0
    for i in text:
        if i in freq_map:
            sc += freq_map[i]
    for word in word_list:
        if word in text.lower():
            sc += len(word) * 0.3
    return sc


s = input().strip()
text = binascii.a2b_base64(s)
reses = []

for key in range(3, 30):
    arr = []
    for i in range(0, len(text), key):
        arr.append(text[i:i+key])
    arr2 = [bytearray() for _ in range(0, max(map(len, arr)))]

    for q, p in enumerate(text):
        arr2[q % key].append(p)
    keys = ""
    for arrs in arr2:
        var = ''.join(list(map(chr, arrs)))
        try:
            keys += chr(decode_hex(binascii.hexlify(bytes(var,encoding="ascii")))[1])
        except:
            keys = "*"
    if keys[0] != "*":
        result = xor_with_key(keys, text.decode("ascii"))
        reses.append((result, get_score(result)))
cur = -100
for i, j in reses:
    if j > cur:
        pasuxi = i
        cur = j
print(pasuxi)
