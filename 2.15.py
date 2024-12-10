import math

x = float(input("Nhập giá trị x (số thực): "))
ep = float(input("Nhập giá trị ep (0 < ep < 1): "))

n = 0
gia_tri_hang = 1  
kq = 1 

while abs(gia_tri_hang) >= ep:
    n += 1
    gia_tri_hang = (x ** n) / math.factorial(n)
    kq += gia_tri_hang

print(f"Giá trị gần đúng của e^{x} là: {kq}")
