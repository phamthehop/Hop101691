n = int(input())

ma_tran = []
for _ in range(n):
    ma_tran.append(list(map(int, input().split())))

la_tam_giac_tren = True
la_tam_giac_duoi = True

for hang in range(n):
    for cot in range(n):
        if hang > cot and ma_tran[hang][cot] != 0:
            la_tam_giac_tren = False
        if hang < cot and ma_tran[hang][cot] != 0:  
            la_tam_giac_duoi = False

if la_tam_giac_tren:
    print("UPPER TRIANGLE")
elif la_tam_giac_duoi:
    print("LOWER TRIANGLE")
else:
    print("NONE")
