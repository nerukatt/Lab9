class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return f'Название книги:{self.title}, Имя автора:{self.author}, Год издания:{self.year}'
    
book1 = Book('Лживые боги','Грем Макнилл','2006')
end = book1.get_info()
print(end)