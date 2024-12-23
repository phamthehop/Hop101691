s = input()
chuoi = set(s)  
for i in chuoi:
    dem = s.count(i) 
    print(f"'{i}': {dem}")
