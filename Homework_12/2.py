"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title (len<50), year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""

from datetime import date

CURRENT_YEAR = date.today().year

class BookCard:
    def __init__(self, author: str, title: str, year: int):
        self.author = author
        self.title = title
        self.year = year

    # --- author ---
    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise ValueError("Author must be a string.")
        if len(value) > 50:
            raise ValueError("Author name must be under 50 characters.")
        self.__author = value

    # --- title ---
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string.")
        if len(value) > 50:
            raise ValueError("Title must be under 50 characters.")
        self.__title = value

    # --- year ---
    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise ValueError("Year must be an integer.")
        if not (0 < value <= CURRENT_YEAR):
            raise ValueError(f"Year must be between 1 and {CURRENT_YEAR}.")
        self.__year = value

    # --- сравнение по году издания ---
    def __eq__(self, other):
        return self.year == other.year

    def __lt__(self, other):
        return self.year < other.year

    def __le__(self, other):
        return self.year <= other.year

    def __gt__(self, other):
        return self.year > other.year

    def __ge__(self, other):
        return self.year >= other.year

    def __ne__(self, other):
        return self.year != other.year

    def __str__(self):
        return f"{self.author}: '{self.title}' ({self.year})"
    

book1 = BookCard("J.K. Rowling", "Harry Potter and the Philosopher's Stone", 1997)
book2 = BookCard("J.R.R. Tolkien", "The Hobbit", 1937)
book3 = BookCard("C.S. Lewis", "The Lion, the Witch and the Wardrobe", 1950)

books = [book1, book2, book3]

# Сортировка по возрастанию года
sorted_books = sorted(books)
for book in sorted_books:
    print(book)

# Сортировка по убыванию года
print("\nПо убыванию:")
for book in sorted(books, reverse=True):
    print(book)