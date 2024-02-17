import doctest


class Pet:
    """
    Класс, который описывает домашнее животное.
    """
    def __init__(self, name: str, age: int):
        """
        Создание и подготовка к работе объекта "Домашнее животное"
        :param name: Кличка домашненго животного
        :param age: Возраст домашнего животного
        Примеры:
        >>> pet = Pet("Mike", 8)
        """
        self._name = name  # Наследуем атрибуты name и age
        self.age = age  # Инициализируем публичный атрибут, отработает setter свойства

    @property
    def name(self) -> str:
        """Возвращает кличку домашнего животного."""
        return self._name

    @property
    def age(self) -> int:
        """Возвращает возраст домашнего животного."""
        return self._age

    @age.setter
    def age(self, new_age: int) -> None:
        """Устанавливает новый возраст домашнего животного."""
        if not isinstance(new_age, int):
            raise TypeError("Возраст домашнего животного должен быть числом типа int")
        if new_age <= 0:
            raise ValueError("Возраст домашнего животного должен быть положительным числом")
        self._age = new_age

    def __str__(self) -> str:
        """Метод, предназначенный для чтения."""
        return f"Кличка домашнего животного {self.name}. Возраст {self.age}."

    def __repr__(self) -> str:
        """Возвращает строку, показывающую, как может быть инициализирован экземпляр."""
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age})"

    def sound(self) -> str:
        """Реализация метода, который возвращает строку о звуком, который издает животное."""
        return "Издаёт животный звук"


class Dog(Pet):
    """Класс, который описывает собаку, как один из видов
     домашнего животного."""
    def __init__(self, name: str, age: int, legs: int):
        """
        Создание и подготовка к работе объекта "Собака",
        дочерний класс объекта "Домашнее животное"
        :param name: Кличка домашненго животного
        :param age: Возраст домашнего животного
        :param legs: Количество ног у домашнего животного
        Примеры:
        >>> pet_1 = Dog("Tom", 3, 4)
        """
        super().__init__(name, age)  # Инициализируем защищенный атрибут, чтобы его нельяз было изменить
        self._legs = legs  # Инициализируем защищенный атрибут, чтобы его нельяз было изменить

    @property
    def legs(self) -> int:
        """Возвращает количество ног у домашнего животного."""
        return self._legs

    def __str__(self) -> str:
        """Метод, предназначенный для чтения."""
        return f"Кличка домашнего животного {self._name}. Возраст {self._age}. Количество ног {self.legs} "

    def __repr__(self) -> str:
        """Возвращает строку, показывающую, как может быть инициализирован экземпляр."""
        return f"{self.__class__.__name__}(name={self._name!r}, age={self._age}), legs={self.legs}) "

    def sound(self) -> str:
        """Перегрузка метода, чтобы он возвращал звук, который издает конкретно собака."""
        return "Гав-гав"


if __name__ == "__main__":
    doctest.testmod()
    pass
