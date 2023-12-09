#<p>By listing the first six prime numbers: $2, 3, 5, 7, 11$, and $13$, we can see that the $6$th prime is $13$.</p>
#<p>What is the $10\,001$st prime number?</p>


def primes_sieve2(limit):
    primes = [True] * limit                          # Initialize the primality list
    primes[0] = primes[1] = False

    for (i, isprime) in enumerate(primes):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                primes[n] = False
    return primes

def get_nth_prime(nth):
    primes = primes_sieve2(999999)
    for x in range(nth-1):
        next(primes)
    return next(primes)


if __name__ == '__main__':
    print(get_nth_prime(10001))