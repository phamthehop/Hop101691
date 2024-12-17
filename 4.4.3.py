class Book:
    def __init__(self, name, page, cost):
        self.name = name
        self.page = page
        self.cost = cost

    def __str__(self):
        return f"{self.name} {self.page} {self.cost}"

books = []

with open("sach.txt", "r", encoding="utf-8") as f:
    for line in f:
        data = line.strip().split()
        name = " ".join(data[:-3]) 
        page = int(data[-2])     
        cost = int(data[-1])     
        books.append(Book(name, page, cost))


loc_books = [book for book in books if book.cost > 100000 and book.page < 200]


with open("ketqua.txt", "w", encoding="utf-8") as f:
    for book in loc_books:
        f.write(str(book) + "\n")
