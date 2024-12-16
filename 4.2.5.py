import re
s = input()
a = re.findall(r"[a-z]", s) 
b = re.findall(r"[A-Z]", s) 
c = re.findall(r"[0-9]", s) 
print(len(a), len(b), len(c)) 
