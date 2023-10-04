from functools import cache

def nth_fib(n):
    """Return the Nth fibonacci number.

    Args:
        n (int): Number in the sequence to find the value for.

    Returns:
        int: Value of the Nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        a , b = 0,1
        for i in range(2, n+1):
            a,b = b, a+b
        return b

@cache
def recursive_fib(n):
    """Return the Nth fibonacci number.

    Args:
        n (int): Number in the sequence to find the value for.

    Returns:
        int: Value of the Nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)