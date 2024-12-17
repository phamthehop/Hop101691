import re

s = input()  
so = re.findall(r"\d+", s)
so_sap_xep = sorted(int(x) for x in so)
dem = 0
ket_qua = re.sub(r"\d+", lambda match: str(so_sap_xep.pop(0)), s)
print(ket_qua)
