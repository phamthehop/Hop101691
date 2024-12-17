m, n = map(int, input().split())

A = []
for _ in range(m):
    row = list(map(int, input().split()))
    A.append(row)

tong = 0
soluong = 0
for i in A:
    tong += sum(i)
    soluong += len(i)

tbcong = tong / soluong
print(f"{tbcong:.2f}")

for i in range(m):
    for j in range(n):
        if A[i][j] > tbcong:
            print(f"{A[i][j]} {i + 1} {j + 1}")
