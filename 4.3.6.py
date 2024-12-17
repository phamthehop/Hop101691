n = int(input())

A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

doi_xung = True
for i in range(n):
    for j in range(n):
        if A[i][j] != A[j][i]:
            doi_xung = False
            break

if doi_xung:
    print("YES")
else:
    print("NO")
