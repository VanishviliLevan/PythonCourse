class Book:
    def __init__(self, name, author, year, pages):
        self.__name = name
        self.__author = author
        self.__year = year
        self.__pages = pages

    def info(self):
        return f"Name - {self.__name} , Author - {self.__author} , Year - {self.__year}, Pages - {self.__pages} "

    def get_name(self):
        return self.__name

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__author

    def get_pages(self):
        return self.__pages

    def set_name(self, name):
        self.__name = name

    def set_author(self, author):
        self.__author = author

    def set_year(self, year):
        self.__year = year

    def set_page(self, pages):
        self.__pages = pages


b1 = Book("Book", "Tom", 1990, 400)
print(b1.info())
b1.set_page(700)
print(b1.info())

b2 = Book("Book2", "Jane", 2002, 500)
print(b2.info())
b2.set_year(2005)
print(b2.info())
