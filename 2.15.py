import math

x = float(input())
ep = float(input())

n = 0
gia_tri_hang = 1  
kq = 1 

while abs(gia_tri_hang) >= ep:
    n += 1
    gia_tri_hang = (x ** n) / math.factorial(n)
    kq += gia_tri_hang

print(f"Giá trị gần đúng của e^{x} là: {kq}")
