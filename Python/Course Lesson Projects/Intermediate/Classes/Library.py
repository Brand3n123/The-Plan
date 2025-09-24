class Book:
    def __init__(self, title, author, year, checked_out=False):
        self.title = title
        self.author = author
        self.year = year
        self.checked_out = checked_out

    def __repr__(self):
        status = "Unavailable" if self.checked_out else "Available"
        return f"The status of {self.title} is {status}"
    
    def check_out(self):
        self.checked_out = True
    
    def check_in(self):
        self.checked_out = False

alex_book = Book("Shower", "Alex Hazelbutt", 2025)
alex_book.check_in()
alex_book.check_out()
alex_book.check_in()
print(alex_book)