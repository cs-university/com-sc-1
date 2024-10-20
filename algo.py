def sum_two_numbers(a, b):
    """
    Algorithm:
    1. Input: two numbers a and b
    2. Compute the sum: result = a + b
    3. Output: result
    """
    return a + b


print("Sum of 5 and 3: ", sum_two_numbers(5, 3))


def max_of_three(a, b, c):
    """
    Algorithm:
    1. Input: three numbers a, b, and c
    2. Compare the three numbers
    3. If a is greater than or equal to b and c, return a
    4. Else if b is greater than or equal to a and c, return b
    5. Else return c
    6. Output: maximum of the three numbers
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


print("Maximum of 3, 7, and 5: ", max_of_three(3, 7, 5))


def is_prime(n):
    """
    Algorithm:
    1. Input: a number n
    2. If n is less than 2, return False (not prime)
    3. Loop from 2 to sqrt(n):
       a. If n is divisible by any number in this range, return False (not prime)
    4. If no divisors found, return True (prime)
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


print("Is 11 prime?: ", is_prime(11))


def factorial(n):
    """
    Algorithm:
    1. Input: a number n
    2. Initialize result = 1
    3. Loop from 1 to n:
       a. Multiply result by the current number in the loop
    4. Output: result (the factorial of n)
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print("Factorial of 5: ", factorial(5))


def fibonacci(n):
    """
    Algorithm:
    1. Input: number of terms n
    2. Initialize two variables a = 0, b = 1
    3. Loop n times:
       a. Print a
       b. Update a and b as follows: a = b, b = a + b
    4. Output: n terms of the Fibonacci sequence
    """
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


print("First 7 terms of Fibonacci sequence: ", end="")
fibonacci(7)
