# RSA001
<pre>
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
</pre>
Decrypt RSA cần các tham số: c(kết qủa), e, p, q
d = inverse(e, (p-1)(q-1))
m = pow(c, d, n)

Ta có p + q = x
n = p*q
=> (p-1)(q-1) = n - x + 1
Decrypt RSA:
<pre>

  from Crypto.Util.number import *
  e = 65537
  c = .........
  n = .........
  x = .........
  phi = n - x + 1
  d = inverse(e, phi)
  m = pow(c, d, n)
  m = hex(m)[2:]
  print(bytes.fromhex(m))
</pre>
