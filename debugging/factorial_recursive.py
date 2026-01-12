#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    This function calculates the factorial of a given non-negative integer
    using a recursive approach.

    Parameters:
    n (int): The non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the given integer n.
    """
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    else:
        # Recursive case: n * factorial of (n - 1)
        return n * factorial(n - 1)

# Convert the command-line argument to an integer
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
