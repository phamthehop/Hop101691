n, q = map(int, input().split())
mang = list(map(int, input().split()))
cau_hoi = list(map(int, input().split()))

def tim_kiem_nhi_phan(mang, x):
    trai, phai = 0, len(mang) - 1
    while trai <= phai:
        giua = (trai + phai) // 2
        if mang[giua] == x:
            return True
        elif mang[giua] < x:
            trai = giua + 1
        else:
            phai = giua - 1
    return False

for x in cau_hoi:
    if tim_kiem_nhi_phan(mang, x):
        print("YES")
    else:
        print("NO")
