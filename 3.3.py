def kiemtraSoHoanHao(n):
    x=0
    for i in range(1,n):
        if n%i==0:
            x+=i
    return x==n
        
def trongkhoang(a,b):
    for i in range(a, b + 1):
        if kiemtraSoHoanHao(i):
            print(i, end=" ")
            
n = int(input())
if kiemtraSoHoanHao(n):
    print("YES")
else:
    print("NO")

a,b = map(int,input().split())
print("Các số hoàn hảo trong khoảng (a,b): ")
trongkhoang(a,b)
