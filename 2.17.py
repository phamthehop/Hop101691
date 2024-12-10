import math

x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

a = math.sqrt(x1**2+y1**2)
b = math.sqrt(x2**2+y2**2)
c = math.sqrt(x3**2+y3**2)

if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")
    
chuvi = a + b + c
s = (a + b + c) / 2
dientich = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(chuvi)
print(dientich)


