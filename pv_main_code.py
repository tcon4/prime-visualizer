"""
Prime Number Visualizer & Analyzer
A project to explore prime numbers through computation and visualization

Author: [Troy Conley]
Started: [01.11.2025]
"""

# Check variable names, okay to reuse

import math
from typing import Any
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
# ============================================================================
# PHASE 1: CORE PRIME FUNCTIONS
# ============================================================================

def is_prime(number: int) -> bool:
    """
    Check if a number is prime using trial division.
    Args:
        number: Integer to check
    Returns:
        Boolean: True if prime, False otherwise
    """

    # Loop to check divisibility of n by each number up to it's square root, adds count of factors
    for num in range(2, (int(number ** 0.5) + 1)):
        if number % num == 0:
            return False

    return True


def sieve_of_eratosthenes(limit: int) -> list[int]:
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
    prime_numbers = []
    for p in range(2, limit + 1):
        if prime[p]:
            prime_numbers.append(p)
    
    return prime_numbers


def prime_factorization(number: int) -> list[int]:
    """
    Find the prime factorization of a number.
    Args:
        number: Integer to factorize
    Returns:
        List with all prime factors of the number
    """
    
    factors = []
    
    # Check for factor of 2
    while number % 2 == 0:
        factors.append(2)
        number = number // 2
    
    # Check odd factors from 3 onwards
    i = 3
    while i * i <= number:
        while number % i == 0:
            factors.append(i)
            number = number // i
        i += 2
    
    # If the number is still greater than 1, it's a prime factor
    if number > 1:
        factors.append(number)
    
    return factors


# ============================================================================
# PHASE 2: VISUALIZATION FUNCTIONS
# ============================================================================

def plot_prime_distribution(limit: int):
    """
    Visualize the distribution of primes up to limit.
    
    Shows both the actual count and the Prime Number Theorem approximation:
    π(x) ≈ x / ln(x)

    Args:
        List of primes via Sieve of Eratosthenes
        Count of primes less than or equal to provided limit
    Returns:
        Line graph including PNT predicted number of primes vs actual count
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


def ulam_spiral(size: int):
    """
    Create an Ulam Spiral visualization.
    
    The Ulam spiral reveals interesting diagonal patterns in prime distribution.
    Numbers are arranged in a spiral, with primes highlighted.
    
    Args:
        Size of the spiral (size x size grid)
    Returns:
        Grid of prime numbers spiraling out from center
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


def plot_prime_gaps(limit: int):
    """
    Visualize gaps between consecutive primes. Goes with Twins and Constellations below!
    Args:
        limit: Upper bound for prime generation
    Returns:
        Line graph showing gaps between consecutive primes
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


def animate_sieve(limit):
    """
    Animated Sieve of Eratosthenes to illustrate how the primes are calculated
    Args:
        limit: The upper bound of primes to be calculated
    Returns:
        Short animation of a grid with size based on the input limit
        Turns multiples red (not prime) and unique primes green
    """
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.animation import FuncAnimation

    grid_size = int(np.sqrt(limit - 1)) + 1

    # Automatically assign sizing based on limit
    if limit <= 100:
        figsize = (10, 10)
        fontsize = 12
        interval = 1000
    elif limit <= 500:
        figsize = (12, 12)
        fontsize = 8
        interval = 800
    elif limit <= 2000:
        figsize = (12, 12)
        fontsize = 6
        interval = 500
    else:  # Very large grids
        figsize = (14, 14)
        fontsize = 5
        interval = 300

    # Set the size of the figure
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    ax.set_aspect('equal')
    ax.axis('off')

    # Form the initial grid of numbers in gray boxes
    numbers = []
    for num in range(2, limit + 1):
        row = (num - 2) // grid_size
        col = (num - 2) % grid_size
        text = ax.text(col + 0.5, grid_size - row - 0.5, str(num),
                       ha="center", va="center", fontsize=fontsize,
                       bbox=dict(boxstyle="square", facecolor="lightgray"))
        numbers.append(text)

    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    # And of course, need to determine which numbers are prime
    primes_list = sieve_of_eratosthenes(int(np.sqrt(limit)))

    def update(frame_num):
        # FINAL FRAME - color all remaining primes green!
        if frame_num >= len(primes_list):
            for num in range(2, limit + 1):
                if is_prime[num]:
                    idx = num - 2
                    if 0 <= idx < len(numbers):
                        numbers[idx].get_bbox_patch().set_facecolor("lightgreen")

            return

        p = primes_list[frame_num]

        # Mark multiples
        for multiple in range(p * p, limit + 1, p):
            is_prime[multiple] = False
            idx = multiple - 2
            if 0 <= idx < len(numbers):
                numbers[idx].get_bbox_patch().set_facecolor("lightcoral")

        # Color prime green
        idx = p - 2
        if 0 <= idx < len(numbers):
            numbers[idx].get_bbox_patch().set_facecolor("lightgreen")

    plt.title(f"Sieve of Eratosthenes: {limit}")

    anim = FuncAnimation(fig, update, frames=len(primes_list) + 1,
                         interval=interval, repeat=False)

    plt.show()
    return anim


# ============================================================================
# PHASE 3: ADVANCED FEATURES
# ============================================================================

def find_twin_primes(limit: int) -> list:
    """
    Find all twin primes up to limit.
    Twin primes are pairs (p, p+2) where both are prime.
    Examples: (3,5), (5,7), (11,13), (17,19)...
    
    Args:
        limit: The upper bound for prime generation
    
    Returns:
        List of tuples containing twin prime pairs
    """
    # Initialize a list for the twins, and the Sieve to get primes
    list_twin_primes = []
    sieve = sieve_of_eratosthenes(limit)

    # Loop through the sieve list, checking for neighboring primes (prime + 2 = another prime)
    for prime in sieve:
        if prime + 2 in sieve:
            list_twin_primes.append((prime, prime + 2))

    return list_twin_primes


def goldbach_conjecture_test(even_number: int) -> list:
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


def find_prime_constellations(limit) -> list:
    """
    Find prime constellations, categorized by exclusivity.

    Args:
        limit: the upper bound of constellations calculated

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
    Uncomment sections to test.
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
    #animation = animate_sieve(2000)
    
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

    #print("\n--- Testing Mersenne Primes ---")
    #mersenne_primes = find_mersenne_primes(20)
    #print(f"Mersenne primes up to 20: {mersenne_primes}")

    #print("\n--- Benchmark Trial Division vs. Sieve of Eratosthenes ---")
    #print(benchmark_algorithms(1000000))


    #result = find_prime_constellations(1500)
    #print("\n" + "=" * 60)
    #print("PRIME CONSTELLATIONS UP TO 1500")
    #print("=" * 60)
    #print(f"\n🌟 Quintuplets ({len(result['quintuplets'])} found - rarest!):")
    #for q in result['quintuplets']:
        #print(f"   {q}")
    #print(f"\n⭐ Quadruplets ({len(result['quadruplets'])} found - not in quintuplets):")
    #for q in result['quadruplets']:
        #print(f"   {q}")
    #print(f"\n✨ Triplets ({len(result['triplets'])} found - standalone only):")
    #for t in result['triplets']:
        #print(f"   {t}")
    #print("=" * 60)


if __name__ == "__main__":
    main()