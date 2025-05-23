#!/usr/bin/python3
import sys

def factorial(n):
    """
    Recursively calculates the factorial of a non-negative integer n.

    Args:
        n (int): The number to compute the factorial of.

    Returns:
        int: The factorial of the number n.
    """
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Read the integer input from the first command-line argument
f = factorial(int(sys.argv[1]))

# Print the result to the console
print(f)
