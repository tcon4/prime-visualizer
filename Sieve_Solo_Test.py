import math

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



def plot_prime_distribution(limit):
    """
    Visualize the distribution of primes up to limit.
    
    Shows both the actual count and the Prime Number Theorem approximation:
    π(x) ≈ x / ln(x)
    
    TODO: Implement this function
    Steps:
    1. Generate primes up to limit
    2. Count cumulative primes at intervals
    3. Calculate PNT approximation
    4. Plot both on same graph
    """
    
    primes = sieve_of_eratosthenes(limit)

    x = list(range(1, limit + 1))
    y = []
    
    for num in x:
        count = 0
        for prime in primes:  # Look at each prime
            if prime <= num:   # Is this prime ≤ our current number?
                count += 1
            else:
                break
        y.append(count)

    # Calculate PNT approximation
    y2 = []

    for num in x:
        if math.log(num) > 0:
            approx = int(num / math.log(num))
            y2.append(approx)
        else:
            continue

    return y2, len(y2)
print("Primes: ", primes)

print(plot_prime_distribution(50))
