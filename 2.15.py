import math

x = int(input())
n = int(input())
ep = float(input())

tam = 0
kq = 0
for i in range(1, n + 1):
    tam = (x ** i) / math.factorial(i)
    if abs(tam) < ep:
        break
    kq += tam
print(1+kq)
