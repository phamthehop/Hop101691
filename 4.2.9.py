import re
s = input()
so = re.findall(r'[0-9]',s)
kq = ""
for i in so:
    if int(i)%2 != 0:
        kq += i
print(*kq)
