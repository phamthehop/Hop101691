import math

x = float(input())
n = int(input())

S = x
for i in range(n - 1):
    S = math.sqrt(x + S)
print(S+1)
