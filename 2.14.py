import math

def tinh_tong(a):
    S = 1 
    n = 1 
    while True:
        hieu = 1 / math.factorial(2 * n + 1)  
        if hieu < a:
            break  
        S += hieu  
        n += 1   
    return S

a = float(input())

ket_qua = tinh_tong(a)
print(f"Tổng là: {ket_qua}")
