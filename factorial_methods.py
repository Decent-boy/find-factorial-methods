# find factorial methods
# recursive methode
def fact(n):
    result=1
    i=1
    while i<=n:
        result*=i
        i+=1
    return result
n=int(input("enter number: "))
print(f"the factorial is {fact(n)}")
# find factorial using a while loop
i=1
fact=1
n=int(input("enter number: "))
while i<=n:
    fact*=i
    i+=1
print(fact)
# find factorial using a for loop
def fact(n):
    result=1
    for i in range(1,n+1):
        result*=i
        return result
n=int(input("enter number: "))
# fact(n)
print(f"factorial is {fact(n)}")

# math module
import math
n=int(input("enter number: "))
x=math.factorial(n)