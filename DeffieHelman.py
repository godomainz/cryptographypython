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
        p = random.randrange(size, 2*size)
        if is_prime(p):
            return p


def is_generator(g, p):
    for i in range(1, p-1):
        if (g**i) % p == 1:
            return False
    return True


def get_generator(p):
    for g in range(2, p):
        if is_generator(g, p):
            return g

p = get_prime(1000)
g = get_generator(p)
print(g, p)