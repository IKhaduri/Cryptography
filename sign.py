from oracle import *
from helper import *

N = 119077393994976313358209514872004186781083638474007212865571534799455802984783764695504518716476645854434703350542987348935664430222174597252144205891641172082602942313168180100366024600206994820541840725743590501646516068078269875871068596540116450747659687492528762004294694507524718065820838211568885027869
e = 65537

Oracle_Connect()

msg = "Crypto is hard --- even schemes that look complex can be broken"
m = ascii_to_int(msg)

#wiki
def mod_inv(a,m,x,y):
    if m == 0:
        return x
    return mod_inv(m, a % m, y, x - y * (a / m))

def inv(a,m):
    return mod_inv(a, m, 1, 0)

a = 2
b = m * inv(2, N) % N

res = Sign(a) * Sign(b) * inv(Sign(1), N) % N

print "If 1 is printed, answer was found ", Verify(ascii_to_bin(msg), res)
print res
Oracle_Disconnect()
