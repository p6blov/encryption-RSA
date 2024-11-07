import sympy
import numpy as np
import random
from sympy import isprime

def generate_large_prime(bits):
    while True:
        prime_candidate = random.getrandbits(bits)
        if isprime(prime_candidate):
            return prime_candidate


p = generate_large_prime(512)
q = generate_large_prime(512)
print("p")
print(8437323994044612961629258804816015484066901951130771528114808888507925344946942337902312080777043389552957096620748041792980652567167091025467551661788411)
print("q")
print(888587182230552164246818311266842288128885594996071074462158716013975554994886154145144292644609899630863403300658300375809594374399546722045910330677659
)

def find_mod_inverse(a, m):
    if np.gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

print(find_mod_inverse(p, q))