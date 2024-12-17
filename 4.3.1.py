a,b,c = map(int,input().split())
dem = 0
for i in range (a):
    hang = list(map(int,input().split()))
    dem += hang.count(c)
print(dem)
