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

print(get_prime(1000))
