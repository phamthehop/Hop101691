import math

x = float(input())
n = int(input())

S = 0
for i in range(n):
    S = math.sqrt(x + S)
print(S+1)
