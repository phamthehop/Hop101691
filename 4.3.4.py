m,n = map(int,input().split())
A = []
for _ in range(m):
    A.append(list(map(int,input().split())))
B = []
for _ in range(m):
    B.append(list(map(int,input().split())))

C = []
for i in range(m):
    dongC = []
    for j in range(n):
        dongC.append(A[i][j] + B[i][j])
    C.append(dongC)

for dong in C:
    print(*dong)
        
