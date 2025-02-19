import sys

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for start in range(2, int(limit ** 0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, limit + 1, start):
                is_prime[multiple] = False
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes, is_prime

def find_four_primes(N, primes, is_prime):
    prime_set = set(primes)
    
    # Guardamos las sumas de todos los pares de primos
    sum_pairs = {}
    for i in range(len(primes)):
        p1 = primes[i]
        if p1 > N: break
        for j in range(i, len(primes)):
            p2 = primes[j]
            pair_sum = p1 + p2
            if pair_sum < N:
                if pair_sum not in sum_pairs:
                    sum_pairs[pair_sum] = []
                sum_pairs[pair_sum].append((p1, p2))

    # Buscamos la suma de cuatro primos
    for pair_sum, pairs in sum_pairs.items():
        p3 = N - pair_sum
        if p3 >= pair_sum and is_prime[p3]:
            for p1, p2 in pairs:
                p4 = N - (p1 + p2 + p3)
                if p4 >= p3 and is_prime[p4]:
                    return p1, p2, p3, p4
    
    return None

limit = 10000000
primes, is_prime = sieve_of_eratosthenes(limit)

input_lines = sys.stdin.read().strip().splitlines()

for line in input_lines:
    N = int(line)
    result = find_four_primes(N, primes, is_prime)
    if result:
        print(" ".join(map(str, result)))
    else:
        print("Impossible.")
