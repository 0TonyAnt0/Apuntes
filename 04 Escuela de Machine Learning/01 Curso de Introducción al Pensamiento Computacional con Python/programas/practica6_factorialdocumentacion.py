def factorial(n):
    """ calcula el factorial de un número (n)
    n int >0
    return n!
    """
    print(n)
    if n==1:
        return 1
    return n*factorial(n-1)

print(factorial(4))