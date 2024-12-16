import re

s = input()
chuoi = re.findall(r"[a-zA-Z]+",s)
chuoi_chinh_sua = [i.capitalize() for i in chuoi]
print(*chuoi_chinh_sua)
