class NV:
    def __init__(self):
        pass

    def nhap(self):
        self.ten,self.ma,self.hesoluong,self.phucap = input().split()
        self.ma = int(self.ma)
        self.hesoluong = float(self.hesoluong)
        self.phucap = int(self.phucap)
        self.luong = self.hesoluong*2000000+self.phucap
    
    def xuat(self):
        print("{0} {1} {2:.2f} {3} {4:.2f}".format(self.ma,self.ten,self.hesoluong,self.phucap,self.luong))

n = int(input())
dsnv = []
for i in range(n):
    nv = NV()
    nv.nhap()
    dsnv.append(nv)
    
dsnv.sort(reverse=True,key=lambda x:x.luong)

print("Danh sach nhan vien da sap xep:",n)
for i in dsnv:
    i.xuat()
