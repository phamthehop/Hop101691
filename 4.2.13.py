import re

so_luong_chuoi = int(input())
for _ in range(so_luong_chuoi):
    chuoi = input()
    nhom_ky_tu = re.finditer(r"(.)\1*", chuoi)
    ket_qua = "".join(f"{i.group(1)}{len(i.group(0))}" for i in nhom_ky_tu)
    print(ket_qua)
