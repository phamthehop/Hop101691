class Nhanvien:
    def __init__(self):
        pass
    def nhap(self):
        #Nhập sai
        self.ma,self.ten,,self.hesoluong,self.phucap = input().split()
        self.ma = int(self.ma)
        self.hesoluong = float(self.hesoluong)
        self.phucap = int(self.phucap)
        self.luongthang = self.hesoluong*2000000+self.phucap
    def inthongtin(self):
        print("{0} {1} {2:.2f} {3} {4}".format(self.ma,self.ten,self.hesoluong,self.phucap,self.luongthang))
    
n = int(input())
dsnv = []
for i in range(n):
    nv = Nhanvien()
    nv.nhap()
    dsnv.append(nv)

print("Nhan vien co luong thap nhat")
min_nv = dsnv[0]
for i in dsnv:
    if i.luongthang < min_nv.luongthang:
        min_nv = i
min_nv.inthongtin()
