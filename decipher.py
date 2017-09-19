from oracle import *
import string
import sys


def get_padding():
    for I in xrange(0, 15):
        prev_block[I] += 1
        bla = [X for Y in blocks[:-2] for X in Y]
        bla.extend(list(prev_block))
        bla.extend(list(blocks[-1]))
        if not Oracle_Send(bla, block_cnt):
            result = 16 - I
            break
    return result

if len(sys.argv) < 2:
    print "Usage: python sample.py <filename>"
    sys.exit(-1)

f = open(sys.argv[1])
data = f.read()
f.close()

c = [(int(data[i:i + 2], 16)) for i in range(0, len(data), 2)]
block_cnt = len(c) / 16
blocks = [c[i * 16:(i + 1) * 16] for i in range(0, block_cnt)]
tmp_blocks = [c[i * 16:(i + 1) * 16] for i in range(0, block_cnt)]
IV = list(blocks[0])
guesses = list([32])
guesses.extend([i for i in range(97, 123)])
guesses.extend([i for i in range(65, 91)])
guesses.extend([i for i in range(48, 58)])
for i in string.punctuation:
    if ord(i) not in guesses:
        guesses.append(ord(i))
for i in range(0, 256):
    if i not in guesses:
        guesses.append(i)
Oracle_Connect()
answer = [0 for _ in range(20 * (block_cnt - 1) + 7)]
for i in range(0, block_cnt - 2):
    c0 = list(blocks[i])
    for j in range(16, 0, -1):
        pad = 16 - j + 1
        for guess in guesses:
            tmp = list(c0)
            for k in range(16 - pad, len(tmp)):
                tmp[k] ^= pad ^ answer[i * 16 + k]
            tmp[16 - pad] ^= guess
            res = list([x for y in blocks[:i] for x in y])
            res.extend(list(tmp))
            res.extend(list(blocks[i + 1]))
            if Oracle_Send(res, len(res) / 16) == 1:
                print "correct guess   ", (guess, chr(guess))
                answer[i * 16 + j - 1] = guess
                break
prev_block = list(blocks[-2])
pad = get_padding()

last_block = [0]*(16-pad)
last_block.extend(pad * [pad])
for i in xrange(16 - pad - 1, -1, -1):
    prev_block = [y ^ last_block[x] ^ (16 - i) for x, y in enumerate(list(blocks[-2]))]
    for j in guesses:
        prev_block[i] = j
        tmp = [x for y in blocks[:-2] for x in y]
        tmp.extend(prev_block)
        tmp.extend(blocks[-1])
        if Oracle_Send(tmp, block_cnt) == 1:
            last_block[i] = (16 - i) ^ j ^ blocks[-2][i]
            print "correct guess   ", (last_block[i], chr(last_block[i]))
            break

msg = "".join([chr(i) for i in last_block if i > 16])

Oracle_Disconnect()
print "".join(x for x in list(map(chr, answer[:(block_cnt - 2) * 16]))) + msg
