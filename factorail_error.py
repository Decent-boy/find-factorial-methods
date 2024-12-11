def factorial(n):
    "this is a doc string"
    if (n==1 or n==0):
        return n
    elif (n<=-1):
        raise ValueError("value should be positive")
    
    else:
        # a=n*factorial(n-1)
        # print(a)
        return n*factorial(n-1)
n=int(input("Enter number for factorial: "))
print(factorial(n))
print(factorial.__doc__)