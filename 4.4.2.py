class Book:
    def __init__(self):
        self.name = ""
        self.page = 0
        self.cost = 0

    def nhap(self):
        self.name = input()
        self.page = int(input())
        self.cost = int(input())
        self.average = round(self.page/self.cost,2)

    def xuat(self):
        print("{0} {1} {2} {3}".format(self.name,self.page,self.cost,self.average))
    
    def ghi_vao_file(self, f):
        f.write("{0} {1} {2} {3}\n".format(self.name, self.page, self.cost, self.average))
        
print("Nhập số lượng sách: ")
n = int(input())
books = []
for i in range(n):
    print("Nhap quyen sach thu",i+1)
    book = Book()
    book.nhap()
    books.append(book)

books.sort(key=lambda x:(x.average,x.name))

for book in books:
    book.xuat()
    
with open("sach.txt", "w", encoding="utf-8") as f:
    for book in books:
        book.ghi_vao_file(f)
