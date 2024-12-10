import math
def UCLN(a,b):
    return math.gcd(a,b)

def BCNN(a,b):
    return a*b//UCLN(a,b)

a,b = map(int,input().split())
print(BCNN(a,b))
