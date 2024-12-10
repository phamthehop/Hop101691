import math

n = int(input())
S = 0
for i in range(1, 2*n + 1,2):
    S += 1/math.factorial(i)
print(S)

m = int(input())
T=0
for i in range(1,m+1):
    T=T+i
    if(T>1000):
        print(f"Số thoả mãn: {i}")
        break

