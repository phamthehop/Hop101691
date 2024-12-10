import math
def UCLN(a,b):
    return math.gcd(a,b)

a,b = map(int,input().split())
print(UCLN(a,b))
