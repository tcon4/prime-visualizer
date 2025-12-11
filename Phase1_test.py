n = int(input("Enter a number >= 2: "))
def is_prime(n):
    """
    Check if a number is prime using trial division.
    
    Args:
        n: Integer to check
    
    Returns:
        Boolean: True if prime, False otherwise
    
    TODO: Implement this function
    Hint: Check divisibility up to sqrt(n)
    Edge cases: Handle n < 2
    """
    #n = int(input("Enter a number >= 2: "))
    if n % num !=0 in range(2,sqrt(num)):
        return True
    else:
        return False
    pass

print(is_prime(n))
