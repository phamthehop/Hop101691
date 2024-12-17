n,m = map(int,input().split())

A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

found = False
s = 0
for i in range(n):
    s = sum(A[i])
    if s%7==0:
        print(i + 1)
        found = True
        
if not found:
    print("NO")
