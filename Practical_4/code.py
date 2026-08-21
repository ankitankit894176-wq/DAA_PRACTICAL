# Practical 4
# Implementation and Time Analysis of Factorial
# using Iterative and Recursive Method

# Iterative Method
def factorial_iterative(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


# Recursive Method
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# Main Program
n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Iterative Result
    result1 = factorial_iterative(n)

    # Recursive Result
    result2 = factorial_recursive(n)

    print("\nFactorial using Iterative Method =", result1)
    print("Factorial using Recursive Method =", result2)

    # Time Complexity
    print("\nTime Complexity:")
    print("Iterative Method : O(n)")
    print("Recursive Method : O(n)")