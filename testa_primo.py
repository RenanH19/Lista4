def func(n):
    return n**2 - n + 41

def ehPrimo(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

print(ehPrimo(func(100)))