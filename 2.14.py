import math

n = int(input())
a = float(input())
S = 0
for i in range(1, 2*n + 1,2):
    tam=1/i
    S += 1/math.factorial(i)
    if tam < a:
        print(S)
        break
