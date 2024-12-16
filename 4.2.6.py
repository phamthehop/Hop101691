import re

s = input()
chuoi = set(s)
for i in chuoi:
    dem = len(re.findall(re.escape(i), s))
    print(f"'{i}': {dem}")
