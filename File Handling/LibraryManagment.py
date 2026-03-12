class LibraryBook:
    def __init__(self, name, price):
        self.book_name = name
        self.__book_price = price   
    def set_price(self, price):
        self.__book_price = price

    def get_price(self):
        return self.__book_price
class DigitalBook(LibraryBook):
    def update_price(self, price):
        self.set_price(price)


book = DigitalBook("Python", 500)
print("Book Name:", book.book_name)
print("Original Price:", book.get_price())
book.update_price(650)
print("Updated Price:", book.get_price())