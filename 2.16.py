import math

a,b,c = map(int,input().split())
if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")
    
chuvi = a + b + c
s = (a + b +c) / 2
dientich = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(chuvi)
print(dientich)
