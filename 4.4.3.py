class Book:
    def __init__(self, name, page, cost):
        self.name = name
        self.page = page
        self.cost = cost

    def __str__(self):
        return f"{self.name} {self.page} {self.cost}"

    def ghi_vao_file(self, f):
        f.write(f"{self.name} {self.page} {self.cost}\n")

books = []
with open("sach.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()  
    for i in range(0, len(lines), 3):
        name = lines[i].strip()     
        page = int(lines[i + 1].strip()) 
        cost = int(lines[i + 2].strip()) 
        books.append(Book(name, page, cost))

loc_books = [book for book in books if book.cost > 100000 and book.page < 200]

with open("ketqua.txt", "w", encoding="utf-8") as f:
    f.write("Danh sách các sách lọc theo điều kiện:\n") 
    for book in loc_books:
        book.ghi_vao_file(f)
