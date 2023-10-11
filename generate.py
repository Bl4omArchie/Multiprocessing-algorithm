from random import randrange, getrandbits
from math import lcm, gcd
from Crypto.Util.number import inverse

from time import perf_counter
from contextlib import contextmanager
import multiprocessing as mp
from multiprocessing import Process

key_pairs = []
round = 4

@contextmanager
def timing(message):
    t = perf_counter()
    yield
    print ("*chrono> ", message, perf_counter()-t)


def isqrt (x):
    q = 1
    while q <= x: 
        q <<= 2                    # Equivalent to q *= 4, but using bitwise shift for better performance

    z, r = x, 0
    while q > 1:
        q >>= 2                    # Equivalent to q //= 4, but using bitwise shift for better performance
        t, r = z - r - q, r >> 1   # Equivalent to r //= 2, but using bitwise shift for better performance
        if t >= 0:
            z, r = t, r + q
    return r

def get_prime_factor(pBits, e):
    """ Generate a prime factor """ 
    i = 0
    candidate = 0

    while candidate == 0:
        while i < (5 * pBits):
            p = getrandbits(pBits)
            if p & 1 == 0:  #if the number is odd, add one
                p |= 1 

            if p >= (isqrt(2) << (pBits - 1)):
                if gcd(p-1, e) == 1:
                    candidate = miller_rabin(p, round)
                    break
            i += 1

    i = 0
    candidate = 0
    while candidate == 0:
        while i<5*pBits:
            q = getrandbits(pBits)
            if q & 1 == 0:
                q |= 1

            if (abs(p-q) > pow(2, (pBits//2)-100)) or (q >= (isqrt(2) << (pBits - 1))):
                if gcd(q-1, e) == 1:
                    candidate = miller_rabin(q, round)
                    break
            i += 1
    return p, q


def miller_rabin(p, r):
    s, d = 0, p - 1
    while d & 1 == 0:
        d >>= 1
        s += 1

    for _ in range(r):
        a = randrange(2, p - 2)
        x = pow(a, d, p)
        if x == 1 or x == p - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, p)
            if x == p - 1:
                break
        else:
            return 0

    return 1


def pair_wise_consistency_test(n, e, d):
    """ Check if the generated keypair can encrypt and decrypt correctly a plaintext m """
    m = randrange(1, n//2)
    return m == pow(m, e*d, n)

def generate(nBits, e=65537):
    if nBits < 2048:
        raise ValueError(("Incorrect key length. nBits must be equal or greater than 2048"))
    
    elif e%2 == 0 or not pow(2, 16) <= e <= pow(2, 256):
        raise ValueError("Incorrect puclic exponent. e must be odd and in the range [2^16, 2^256]")
    pBits = nBits//2
    
    p, q = get_prime_factor(pBits, e) 
    d = inverse(e, lcm(p-1, q-1))
    n = p*q

    if pair_wise_consistency_test(n, e, d) == 0:
        raise ValueError("Error, please retry. Consistency test failed")
    return n, e, d



def generate_n_keys(num_key, nBits):
    with timing(f"Generating {num_key} keys of {nBits} bits:"):
        for _ in range(num_key):
            key_pairs.append(generate(nBits))


def multi_proc_simulation(num_keys, num_proc, nBits):
    key_per_proc = num_keys//num_proc

    with timing(f"With {num_proc} processus:"):
        procs = []
        for _ in range(num_proc):
            proc = Process(target=generate_n_keys, args=(key_per_proc, nBits))
            procs.append(proc)
            proc.start()
        
        for proc in procs:
            proc.join()


if __name__ == "__main__":
    #multi processus 
    num_keys = 100
    num_proc = 5

    mp.set_start_method('spawn')
    multi_proc_simulation(num_keys, num_proc, 2048)