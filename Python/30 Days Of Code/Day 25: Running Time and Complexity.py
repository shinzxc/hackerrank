# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def isPrime(n):
    if n == 2:
        return True
    elif n == 1:
        return False
        
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    
    return True

p = int(input())
for i in range(0, p):
    x = int(input())

    s = "Prime" if (isPrime(x)) else "Not prime"
    print(s)
