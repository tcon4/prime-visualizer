def sieve_of_eratosthenes(limit: int) -> int: #COMPLETE
    """
    Generate all prime numbers up to limit using the Sieve of Eratosthenes.
    
    Args:
        limit: Upper bound for prime generation
    
    Returns:
        List of all primes up to limit
    """
   
    #Create a boolean list to track prime status of numbers
    prime = [True] * (limit + 1)
    
    # Sieve of Eratosthenes algorithm
    p = 2
    while p * p <= limit:
        if prime[p]:
            
            # Mark all multiples of p as non-prime
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1

    # Collect all prime numbers
    res = []
    for p in range(2, limit + 1):
        if prime[p]:
            res.append(p)
    
    return res

print("\n--- Testing sieve_of_eratosthenes ---")
primes = sieve_of_eratosthenes(50)
print(f"Primes up to 50: {primes}")

