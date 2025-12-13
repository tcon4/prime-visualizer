"""
Prime Number Visualizer & Analyzer
A project to explore prime numbers through computation and visualization

Author: [Troy Conley]
Started: [01.11.2025]
"""

# Check variable names, okay to reuse

import math
from typing import Any
import matplotlib.pyplot as plt
import numpy as np


# ============================================================================
# PHASE 1: CORE PRIME FUNCTIONS
# ============================================================================

def is_prime(n: int) -> bool: #COMPLETE
    """
    Check if a number is prime using trial division.
    Args:
        n: Integer to check
    Returns:
        Boolean: True if prime, False otherwise
    """

    # Loop to check divisibility of n by each number up to it's square root, adds count of factors
    for num in range(2, (int(n ** 0.5) + 1)):
        if n % num == 0:
            return False

    return True


def sieve_of_eratosthenes(limit: int) -> list[Any]: #COMPLETE
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
    prime_nums = []
    for p in range(2, limit + 1):
        if prime[p]:
            prime_nums.append(p)
    
    return prime_nums


def prime_factorization(n): #COMPLETE
    """
    Find the prime factorization of n.
    Args:
        n: Integer to factorize
    Returns:
        List with all prime factors of n
    """
    
    factors = []
    
    # Check for factor of 2
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Check odd factors from 3 onwards
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 2
    
    # If n is still greater than 1, it's a prime factor
    if n > 1:
        factors.append(n)
    
    return factors


# ============================================================================
# PHASE 2: VISUALIZATION FUNCTIONS
# ============================================================================

def plot_prime_distribution(limit: int): #COMPLETE
    """
    Visualize the distribution of primes up to limit.
    
    Shows both the actual count and the Prime Number Theorem approximation:
    π(x) ≈ x / ln(x)
    """

    # Call Sieve from above and establish plot lists
    primes = sieve_of_eratosthenes(limit)

    x = list(range(1, limit + 1))
    y = []

    # Check number of primes less than or equal to number plotted on x-axis
    for num in x:
        count = 0
        for prime in primes:
            if prime <= num:   
                count += 1
        y.append(count)
        
    # Sieve Plot
    plt.plot(x,y, marker = "o", color = "blue", label = "Prime Numbers")

    # Calculate PNT approximation
    y2 = []
    
    for num in x:
        if math.log(num) > 0:
            approx = num / (math.log(num) - 1)
            y2.append(approx)
        else:
            y2.append(0)

    # PNT Plot
    plt.plot(x,y2, marker = "o", color = "red", label = "PNT Approx")
    
    plt.xlabel('n')
    plt.ylabel('Number of primes ≤ n')
    plt.title(f'Prime Distribution up to {limit}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


def ulam_spiral(size: int): #COMPLETE
    """
    Create an Ulam Spiral visualization.
    
    The Ulam spiral reveals interesting diagonal patterns in prime distribution.
    Numbers are arranged in a spiral, with primes highlighted.
    
    Args:
        size: Size of the spiral (size x size grid)
    """
    # Define grid and it's size
    grid = np.zeros((size, size))

    # Find the center, and we're starting with 1
    x = size // 2
    y = size // 2
    num = 1
    
    # Directional values
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    #Fill out the rest of the spiral grid
    step_size = 1
    dir_index = 0
    while num <= size * size:
        for step in range(step_size):
            if is_prime(num):
                grid[x][y] = 1
            else:
                grid [x][y] = 0

            num += 1
        
            x += directions[dir_index][0]
            y += directions[dir_index][1]
        
        dir_index = np.mod((dir_index + 1), 4)
        if dir_index % 2 == 0:
            step_size += 1

    #Ulam Plot
    plt.imshow(grid, cmap='binary', interpolation='nearest')
    plt.title('Ulam Spiral')
    plt.show()


def plot_prime_gaps(limit: int): #COMPLETE
    """
    Visualize gaps between consecutive primes.
    
    Args:
        limit: Upper bound for prime generation
    """
    # Two lists to be used
    primes = sieve_of_eratosthenes(limit)
    gaps = []

    # Calculate the gap between each prime, and add it to the list
    for i in range(len(primes) - 1):
        gap = primes[i + 1] - primes[i]
        gaps.append(gap)

    # Prime Gap Plot
    x = list(range(1, len(gaps) +1)) 
    y = gaps
    
    plt.plot(x,y, marker = "o", color = "green", label = "Gaps")
    
    plt.xlabel('Prime index')
    plt.ylabel('Gap to next prime')
    plt.title(f'Prime Gaps up to {limit}')
    plt.grid(True, alpha=0.3)
    plt.show()


# ============================================================================
# PHASE 3: ADVANCED FEATURES
# ============================================================================

def find_twin_primes(limit: int) -> list:
    """
    Find all twin primes up to limit.
    Twin primes are pairs (p, p+2) where both are prime.
    Examples: (3,5), (5,7), (11,13), (17,19)...
    
    Args:
        limit: Upper bound
    
    Returns:
        List of tuples containing twin prime pairs
    """
    # Initialize a list for the twins
    list_twin_primes = []
    # And another for the Sieve
    sieve = sieve_of_eratosthenes(limit)

    # Loop through the sieve list, checking for neighboring primes (prime + 2 = another prime)
    for prime in sieve:
        if prime + 2 in sieve:
            list_twin_primes.append((prime, prime + 2))

    return list_twin_primes


def goldbach_conjecture_test(even_number: int):
    """
    Test Goldbach's conjecture for even number n.
    Conjecture: Every even integer > 2 can be expressed as sum of two primes.
    Args:
        even_number: Even integer to test
    Returns:
        List of tuples (p, q) where p + q = n and both are prime
    """
    # Initialize lists
    sieve = sieve_of_eratosthenes(even_number)
    goldbach_conjecture_list = []

    # And the loop to determine partner primes and add to Conjecture list
    for prime in sieve:
        if prime > even_number // 2:
            break
        partner_prime = even_number - prime
        if partner_prime in sieve:
            goldbach_conjecture_list.append((prime, partner_prime))

    return goldbach_conjecture_list


def find_mersenne_primes(limit: int) -> list:
    """
    Find Mersenne primes (primes of form 2^p - 1) up to limit.
    Args:
        limit: Check all primes p up to this limit
    Returns:
        List of tuples: (p, 2^p - 1) for Mersenne primes found
    """

    # Warning about size limit
    if limit > 30:
        print(f"⚠️ WARNING: Testing Mersenne primes beyond p=30 can be slow!")

    # Initialize the lists
    primes = sieve_of_eratosthenes(limit)
    mersenne_primes = []

    # Loop through primes generated from Sieve to check which are Mersenne Primes
    for prime in primes:
        mersenne = 2 ** prime - 1
        if is_prime(mersenne):
            mersenne_primes.append((prime, mersenne))

    return mersenne_primes


def find_prime_constellations(limit):
    """
    Find prime constellations, categorized by exclusivity.

    Args:
        limit: Upper bound
        pattern: Type of constellation
            - "triplet": (p, p+2, p+6) or (p, p+4, p+6)
            - "quadruplet": (p, p+2, p+6, p+8)
            - "quintuplet": (p, p+2, p+6, p+8, p+12)

    Returns:
        List of tuples containing constellation patterns
    """

    sieve = sieve_of_eratosthenes(limit)

    triplets = []
    quadruplets = []
    quintuplets = []

    for prime in sieve:

        if (prime + 2) in sieve and (prime + 6) in sieve and (prime + 8) in sieve and (prime + 12) in sieve:
            quintuplets.append((prime, prime + 2, prime + 6, prime + 8, prime + 12))

        elif (prime + 2) in sieve and (prime + 6 in sieve) and (prime + 8) in sieve:
            quadruplets.append((prime, prime + 2, prime + 6, prime + 8))

        elif (prime + 2) in sieve and (prime + 6) in sieve:
            triplets.append((prime, prime + 2, prime + 6))
        elif (prime + 4) in sieve and (prime + 6) in sieve:
            triplets.append((prime, prime + 4, prime + 6))

    return {
        'triplets': triplets,
        'quadruplets': quadruplets,
        'quintuplets': quintuplets
    }


# ============================================================================
# PERFORMANCE TESTING
# ============================================================================

def benchmark_algorithms(limit):
    """
    Compare performance of different prime-finding methods.

    Use time.time() to measure execution time of:
    - Trial division for each number
    - Sieve of Eratosthenes
    - NumPy optimized version (if you implement one)
    """
    import time

    print("=" * 50)
    print(f"BENCHMARKING: Finding all primes up to {limit:,}")
    print("=" * 50)

    start = time.time()
    primes_trial = []
    for number in range(2, limit + 1):
        if is_prime(number):
            primes_trial.append(number)
    time_trial = time.time() - start

    start = time.time()
    sieve_trial = sieve_of_eratosthenes(limit)
    time_sieve = time.time() - start

    speedup = time_trial / time_sieve

    print(f"✅ Trial Division: {time_trial:.4f} seconds ({len(primes_trial)} primes)")
    print(f"✅ Sieve Method:   {time_sieve:.4f} seconds ({len(sieve_trial)} primes)")

    return f"\n🚀 Sieve is {speedup:.1f}x faster!\n"


# ============================================================================
# MAIN EXECUTION & TESTING
# ============================================================================

def main():
    """
    Main function to test your implementations.
    Uncomment sections as you complete them!
    """
    
    #print("Prime Number Visualizer & Analyzer")
    #print("=" * 50)
    
    #Test Phase 1
    #print("\n--- Testing is_prime ---")
    #test_numbers = [2, 3, 4, 17, 25, 97, 100]
    #for num in test_numbers:
        #print(f"{num}: {is_prime(num)}")
    
    #print("\n--- Testing sieve_of_eratosthenes ---")
    #primes = sieve_of_eratosthenes(50)
    #print(f"Primes up to 50: {primes}")
    
    #print("\n--- Testing prime_factorization ---")
    #test_factors = [12, 100, 97, 256]
    #for num in test_factors:
        #print(f"{num}: {prime_factorization(num)}")
    
    # Test Phase 2
    #print("\n--- Generating visualizations ---")
    #plot_prime_distribution(1000)
    #plot_prime_gaps(1000)
    #ulam_spiral(201)
    
    # Test Phase 3
    #print("\n--- Testing Twin Primes ---")
    #twins = find_twin_primes(100)
    #print(f"Twin primes up to 100: {twins}")

    #print("\n--- Testing Goldbach's conjecture ---")
    #print(f"200: {goldbach_conjecture_test(200)}")
    #test_even = [10, 32, 42, 100]
    #for even_number in test_even:
        #pairs = goldbach_conjecture_test(even_number)
        #print(f"{even_number} = {pairs[0][0]} + {pairs[0][1]}")

    print("\n--- Testing Mersenne Primes ---")
    mersenne_primes = find_mersenne_primes(20)
    print(f"Mersenne primes up to 20: {mersenne_primes}")

    #print("\n--- Benchmark Trial Division vs. Sieve of Eratosthenes ---")
    #print(benchmark_algorithms(1000000))


    result = find_prime_constellations(1500)
    print("\n" + "=" * 60)
    print("PRIME CONSTELLATIONS UP TO 1500")
    print("=" * 60)
    print(f"\n🌟 Quintuplets ({len(result['quintuplets'])} found - rarest!):")
    for q in result['quintuplets']:
        print(f"   {q}")
    print(f"\n⭐ Quadruplets ({len(result['quadruplets'])} found - not in quintuplets):")
    for q in result['quadruplets']:
        print(f"   {q}")
    print(f"\n✨ Triplets ({len(result['triplets'])} found - standalone only):")
    for t in result['triplets']:
        print(f"   {t}")
    print("=" * 60)


if __name__ == "__main__":
    main()


# ============================================================================
# EXTENSION IDEAS (After completing the above)
# ============================================================================

"""
1. Prime number race: Compare primes ≡ 1 (mod 4) vs ≡ 3 (mod 4)
2. Prime spirals with different patterns
3. Animated visualization of the Sieve of Eratosthenes
4. Web interface using Streamlit or Flask
5. Compare your implementations with sympy.isprime() for validation
6. Hardy-Littlewood constants visualization
"""
