class NV:
    def __init__(self):
        pass

    def nhap(self):
        
        self.ten,self.ma,self.diemtoan,self.diemtriet,self.diemLTC = input().split()
        self.ma = int(self.ma)
        self.diemtoan = float(self.diemtoan)
        self.diemtriet = float(self.diemtriet)
        self.diemLTC = float(self.diemLTC)
        self.diemtrungbinh = (self.diemtoan + self.diemtriet + self.diemLTC)/3
    
    def xuat(self):
        print("{0} {1} {2:.2f} {3:.2f} {4:.2f} {5:.2f}".format(self.ma,self.ten,self.diemtoan,self.diemtriet,self.diemLTC,self.diemtrungbinh))

n = int(input())
dsnv = []
for i in range(n):
    nv=NV()
    nv.nhap()
    dsnv.append(nv)
    
dem = 0
print("Danh sach sinh vien hoc lai")
for i in dsnv:
    if ((i.diemtoan < 4.0 and i.diemtriet < 4.0) or (i.diemtoan < 4.0 and i.diemLTC < 4.0) or (i.diemtriet < 4.0 and i.diemLTC < 4.0)):
        i.xuat()
        dem += 1
print(f"Danh sach nay co {dem} sinh vien hoc lai")
