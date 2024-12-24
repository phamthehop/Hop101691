n = int(input())

A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

tamgiactren = True
tamgiacduoi = True

for hang in range(n):
    for cot in range(n):
        if hang > cot and A[hang][cot] != 0:
            tamgiactren = False
        if hang < cot and A[hang][cot] != 0:  
            tamgiacduoi = False

if tamgiactren:
    print("UPPER TRIANGLE")
elif tamgiacduoi:
    print("LOWER TRIANGLE")
else:
    print("NONE")
