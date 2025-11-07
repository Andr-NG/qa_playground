class Book:
    def __init__(self, title, author, pages):
        """
        Initializes a Book object with a title, author, and number of pages.
        This method is called when you create a new instance, like Book("The Hobbit", "J.R.R. Tolkien", 310).
        """
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """
        Returns a user-friendly string representation of the object.
        Called by print() and str().
        """
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        """
        Returns an official string representation of the object for developers.
        Called by repr(). It's often used for debugging.
        """
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    def __len__(self):
        """
        Returns the 'length' of the object, which we define as the number of pages.
        Called by len().
        """
        return self.pages

    def __eq__(self, other):
        """
        Compares two Book objects for equality.
        This allows you to use the == operator.
        """

        # if other object if of Book
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    @classmethod
    def create_book(cls, info: str):
        title, author = info.split(", ")[:2]
        pages = int(info.split(", ")[-1])
        return cls(title, author, pages)


my_book = Book("My Book", "Me", 200)
friends_book = Book("His Book", "Friend", 150)

# print(my_book)  # __str()__ used
# print(repr(my_book))  # __repr()__ used by calling repr()
# print(len(my_book))
# print(my_book == friends_book)


more_book = Book.create_book("More Book, Title, 100")
print(more_book.__dict__)
