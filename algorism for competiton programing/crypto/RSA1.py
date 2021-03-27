import Crypto.PublicKey.RSA as RSA


# 与えられたもの
N = 97139961312384239075080721131188244842051515305572003521287545456189235939577
E = 65537
C = 77361455127455996572404451221401510145575776233122006907198858022042920987316

# ./mesieve を使ってN=p*qのp,qを求める

p = 299681192390656691733849646142066664329
q = 324144336644773773047359441106332937713

# d = RSA.inverse(E, (p-1)*(q-1))
d = pow(E, -1, (p-1)*(q-1))
m = pow(C, d, N)

print(RSA.long_to_bytes(m))
