class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Продолжительность чтения {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration})"

    @property
    def duration(self) -> float:
        """Возвращает продолжительность чтения книги."""
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        """Устанавливает продолжительность чтения книги."""
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность чтения книги должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность чтения книги должна быть положительным числом")
        self._duration = new_duration


book_1 = PaperBook("Стихи", "Пушкин", 100)
book_2 = AudioBook("Проза", "Толстой", 5.6)
print(book_1)
print(book_2)
print(book_1.name)
print(book_2.author)
book_1.pages = 300
book_2.duration = -3.4
print(book_1.pages)
print(book_2.duration)
book_1.name = "Новое название"
