m, n, p = map(int, input().split())

A = []
for _ in range(m):
    A.append(list(map(int, input().split())))
B = []
for _ in range(n):
    B.append(list(map(int, input().split())))

#Tạo một ma trận C với kích thước m × p, trong đó tất cả các phần tử đều là 0.
C = [[0] * p for _ in range(m)] 

for i in range(m):
    for j in range(p):
        for k in range(n): 
            C[i][j] += A[i][k] * B[k][j]

for row in C:
    print(*row)
