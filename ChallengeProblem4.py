#Psuedocode:

# Start
# Check if n <= 1
# Return 1
# Check if lookup table contains n
# Return value from lookup table
# Calculate factorial recursively:
#    - Calculate factorial of n-1
#    - Multiply n by factorial of n-1
#    - Add n and factorial to lookup table
#    - Return factorial
# End

lookup_table = {}  # Lookup table to store factorial values

def factorial(n):
    if n <= 1:
        return 1
    elif n in lookup_table:
        return lookup_table[n]
    else:
        factorial_n_minus_1 = factorial(n - 1)
        factorial_n = n * factorial_n_minus_1
        lookup_table[n] = factorial_n
        return factorial_n

# Testing the factorial function
n = int(input("Enter a number: "))
result = factorial(n)
print(f"The factorial of {n} is: {result}")