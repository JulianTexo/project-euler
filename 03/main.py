NUMBER = 600851475143

def primes_sieve2(limit):
    primes = [True] * limit                          # Initialize the primality list
    primes[0] = primes[1] = False

    for (i, isprime) in enumerate(primes):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                primes[n] = False
    return primes

def check_prime(number) -> bool:
    for x in range(2, int(number / 2)):
        if number%x == 0:
            return False
    return True

def find_biggest_prime():
    prime_factors = []
    number = int(NUMBER)
    primes = primes_sieve2(int(number / 2))
    for x in range(1, int(number / 2)):
        if x%2 == 0:
            continue
        if number%x == 0:
            if x in primes:
                prime_factors.append(x)
    print(max(prime_factors))

if __name__ == "__main__":
    find_biggest_prime()