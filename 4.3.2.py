m,n = map(int,input().split())

A = []
for _ in range(m):
    A.append(list(map(int,input().split())))

B = []
for _ in range(m):
    B.append(list(map(int,input().split())))

C = []
D = []
for i in range(m):
    dongC = []
    dongD = []
    for j in range(n):
        dongC.append(A[i][j]+B[i][j])
        dongD.append(A[i][j]-B[i][j])
    C.append(dongC)
    D.append(dongD)

for dong in C:
    print(*dong)
for dong in D:
    print(*dong)
