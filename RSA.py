import math
import random


def is_prime(p):
    if p > 1:
        for i in range(2, math.isqrt(p)):
            if p % i == 0:
                return False
        return True
    else:
        return False


def get_prime(size):
    while True:
        p = random.randrange(size, 2 * size)
        if is_prime(p):
            return p


def lcm(a, b):
    return a * b // math.gcd(a, b)


def get_e(lambda_n):
    for e in range(2, lambda_n):
        if math.gcd(e, lambda_n) == 1:
            return e
    return False


def get_d(e, lambda_n):
    for d in range(2, lambda_n):
        if d * e % lambda_n == 1:
            return d
    return False


# Key generation done by Alice
# Step 1: Generate two distinct primes

size = 300
p = get_prime(size)
q = get_prime(size)
while True:
    if p == q:
        q = get_prime(size)
    else:
        break
print("Generated Primes:", p, q)

# Step 2: compute n = pq
n = p * q
print("Modules n:", n)

# Step 3:  Compute lambda(n) (lncm(n) = λ(n) = lcm(λ(p),λ(q)), λ(p)=p-1, lcm(a,b) = |ab|/gcd(a,b))
lambda_n = lcm(p - 1, q - 1)
print("Lambda n:", lambda_n)

# Step 4: Choose an integer e such that 1 < e < λ(n) and gcd(e, λ(n)) = 1; that is, e and λ(n) are coprime
e = get_e(lambda_n)
print("Public exponent :", e)

# Step 5: solve for d the equation d⋅e ≡ 1 (mod λ(n));
d = get_d(e, lambda_n)
print("Secret exponent :", d)

# Done with key generation
print("Public key (e,n)", e, n)
print("Secret key (d)", d)

# This is Bob wanting to send a message
m = 117
c = m**e % n
print("Bob sends",c)

# This is Alice decrypting the cipher
m = c**d % n
print("Alice message", m)
