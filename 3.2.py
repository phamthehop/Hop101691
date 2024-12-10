def kiem_tra_nguyen_to(n):
    if n < 2:
    for i in range(2, n):
        if n % i == 0:
            return False 
    return True 

n = int(input())

if kiem_tra_nguyen_to(n):
    print("YES")
else:
    print("NO")
