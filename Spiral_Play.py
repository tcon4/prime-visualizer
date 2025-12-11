import math
import matplotlib.pyplot as plt
import numpy as np

def is_prime(n: int) -> bool: ###COMPLETE

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


    grid_size = 1001
    grid = np.zeros((grid_size, grid_size))

    x = grid_size // 2
    y = grid_size // 2

    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    num = 1

    step_size = 1
    dir_index = 0
    while num <= grid_size * grid_size:
        for step in range(step_size):
            if is_prime(num):
                grid[x][y] = num
            else:
                grid [x][y] = 0

            num += 1
            
            x += directions[dir_index][0]
            y += directions[dir_index][1]
            
        dir_index = np.mod((dir_index + 1), 4)
        if dir_index % 2 == 0:
            step_size += 1

    #print(grid)
    plt.imshow(grid, cmap='binary')
    plt.title('Ulam Spiral')
    plt.show()
