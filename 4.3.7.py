m =int(input())

A = []
for _ in range(m):
    A.append(list(map(int, input().split())))

tongcheochinh = 0
tongcheophu = 0

for i in range(m):
    tongcheochinh += A[i][i]
    tongcheophu += A[i][m-i-1]

print(tongcheochinh)
print(tongcheophu)
