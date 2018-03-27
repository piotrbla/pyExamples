from timeit import timeit

import time


def find_super_primes(a, b):
    sieve = [True for _ in range(b + 1)]
    sieve[0:1] = [False, False]
    for start in range(2, b + 1):
        if sieve[start]:
            for i in range(2 * start, b + 1, start):
                sieve[i] = False
    primes = []
    m = max(2, a)
    for i in range(m, b):
        if sieve[i]:
            is_super = True
            for c in str(i):
                if c in ['0', '1', '4', '6', '8', '9']:
                    is_super = False
                    break
            if is_super:
                primes.append(i)
    print(primes[0:10])
    print(primes[-10:])
    return len(primes)


def get_sieve():
    if hasattr(get_sieve, 'count'):
        return get_sieve.lazy_sieve
    last = 7777778
    sieve = [True for _ in range(last)]
    sieve[0:1] = [False, False]
    for start in range(2, last):
        if sieve[start]:
            for i in range(2 * start, last, start):
                sieve[i] = False
    get_sieve.count = 1
    get_sieve.lazy_sieve = sieve
    return sieve


def get_total_primes(a, b):
    sieve = get_sieve()

    last = min(7777778, b + 1)
    primes = []
    m = max(2, a)
    last -= 1
    for i in range(m, last):
        if sieve[i]:
            is_super = True
            for c in str(i):
                if c in ['0', '1', '4', '6', '8', '9']:
                    is_super = False
                    break
            if is_super:
                primes.append(i)
    return len(primes)
    # print(primes[0:10])
    # print(primes[-10:])


# print(find_super_primes(10, 10**7))
# print(find_super_primes(27796, 9897328))

start_time = time.time()
print(get_total_primes(27796, 9897328))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(get_total_primes(27796, 9897329))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(get_total_primes(27796, 9897330))
print("--- %s seconds ---" % (time.time() - start_time))
# print(find_super_primes(500, 600))
