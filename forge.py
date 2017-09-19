from oracle import *
import sys

if len(sys.argv) < 2:
    print "Usage: python sample.py <filename>"
    sys.exit(-1)

f = open(sys.argv[1])
data = f.read()
f.close()


# stackoverflow
def sxor(s1, s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


Oracle_Connect()


asd = Mac(data[:32], 32)
for i in xrange(2, len(data)/16, 2):
    tmp = sxor(str(asd), data[i*16:i*16+16])
    X = tmp + data[(i+1)*16:(i+1)*16+16]
    asd = Mac(X, len(X))

ret = Vrfy(data, len(data), asd)
print asd
print "encoded in hex: ",str(asd).encode('hex')
if ret == 1:
    print "Message verified successfully!"

else:
    print "Message verification failed."

Oracle_Disconnect()
