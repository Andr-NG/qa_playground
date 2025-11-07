# Создай класс Library, который управляет книгами.
# flake8: Noqa
# Условия:
# Метод add_book(title: str, author: str, year: int) — добавляет книгу, если книги с таким названием ещё нет.
# Метод remove_book(title: str) — удаляет книгу по названию.
# Метод find_books_by_author(author: str) — возвращает список всех книг этого автора.
# Метод get_books_sorted(by: str = "title") — возвращает список книг, отсортированных по title, author или year.
# Метод get_statistics() — возвращает словарь с количеством книг и количеством уникальных авторов.


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, title: str, author: str, year: int):
        user_book = {"title": title, "author": author, "year": year}
        if not self.books:
            self.books.append(user_book)
        else:
            # проходимся по всему списку, сравнивая каждый элемент списка со входным элементом
            # если есть хотя бы 1 освпадение, то возвращаем False через any()
            if any(book["title"] == title for book in self.books):
                raise ValueError("This book already exsists")
            self.books.append(user_book)

    def remove_book(self, title: str):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                # иначе не сработает else
                break
        else:
            print("No such a book exists to delete")

    def __len__(self):
        return len(self.books)

    def get_books_sorted(self, by: str = "title"):
        return sorted(self.books, key=lambda el: el.get(by))

    def get_statistics(self):
        total_books = len(self.books)

        total_authors = list(dict.fromkeys(book["author"] for book in self.books))
        # total_authors = set(map(lambda el: el.get("author"), self.books))

        return {"total_books": total_books, "total_authors": total_authors}


lib = Library()

lib.add_book("GHI", "Child", 1950)
lib.add_book("ABC", "Man", 1955)
lib.add_book("SAD", "Man", 1955)
lib.add_book("IUU", "Man", 1955)
lib.add_book("LUU", "Cat", 1955)
lib.add_book("DEF", "Woman", 1950)
print(len(lib))
lib.remove_book("DEF")
print(len(lib))
print(lib.get_books_sorted())
print(lib.get_statistics())
