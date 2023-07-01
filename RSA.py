from Crypto.Util.number import *
from flag import FLAG

p = getPrime(1024)
q = getPrime(1024)

e = 65537
n = p*q

m = bytes_to_long(FLAG)

c = pow(m, e, n)

print(f'{p + q = }')
print(f'{n = }')
print(f'{c = }')