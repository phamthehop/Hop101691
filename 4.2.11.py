import re
s = input()
kq = re.findall(r'[0-9]+',s)
kq = list(map(int, kq))
print(max(kq))
