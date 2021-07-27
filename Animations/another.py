import numpy as np
import math

def series(x, n):
    ans = 0.0
    i = 0
    while i <= n:
        ans = ans + (pow(x, i)/math.factorial(i))
        i = i+1
    return ans

degree=float(input("Enter the degree : "))
serial=int(input("\nEnter the serial : "))
answer = series(degree, serial)
print("\n")
print(answer)
