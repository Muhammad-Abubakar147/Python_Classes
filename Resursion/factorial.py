def factorial(n):
    if n == 0 or n == 1:   # Base Case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive Call

print(factorial(5))  # Output: 120