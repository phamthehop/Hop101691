import re
s = input()
kq = re.findall(r'[0-9]+',s)
print(max(map(int,kq)))
