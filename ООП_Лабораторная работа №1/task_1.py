# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Car:
    """
    Документация на класс №1.
    Класс описывает модель машины
    """
    def __init__(self, color: str, gearbox: int):
        """
        Создание и подготовка к работе объекта "Машина"

        :param color: Цвет машины
        :param gearbox: Количество передач у машины

        Примеры:
        >>> car = Car("red", 8)  # инициализация экземпляра класса
        """
        if not isinstance(gearbox, int):
            raise TypeError("Количество передач должно быть типа int")
        if gearbox <= 3:
            raise ValueError("Количество передач должно быть больше 3")
        self.gearbox = gearbox
        self.color = color

    def is_racing_car(self) -> bool:
        """
        Функция которая проверяет является ли машина гоночной

        :return: Является ли машина гоночной

        Примеры:
        >>> car = Car("blue", 10)
        >>> car.is_racing_car()
        """
        ...

    def is_color_car(self) -> bool:
        """
        Функция которая проверяет является ли цвет машины хроматическим

        :return: Является ли цвет машины хроматическим

        Примеры:
        >>> car = Car("black", 5)
        >>> car.is_color_car()
        """
        ...


class Table:
    """
    Документация на класс №2.
    Класс описывает модель стола
    """
    def __init__(self, table_legs: int, items_on_the_table: int):
        """
        Создание и подготовка к работе объекта "Стол"

        :param table_legs: Количество ножек у стола
        :param items_on_the_table: Количество предметов, которые лежат на столе

        Примеры:
        >>> table = Table(4, 2)  # инициализация экземпляра класса
        """
        if not isinstance(table_legs, int):
            raise TypeError("Количество ножек у стола должно быть типа int")
        if items_on_the_table < 0:
            raise ValueError("Количество предметов, лежащих на столе не должно быть отрицательным числом")
        self.table_legs = table_legs
        self.items_on_the_table = items_on_the_table

    def add_items_to_table(self, items: int) -> None:
        """
        Добавление предметов на стол.
        :param items: Количество предметов,добавляемых на стол

        Примеры:
        >>> table = Table(4, 3)
        >>> table.add_items_to_table(1)
        """
        if not isinstance(items, int):
            raise TypeError("Количество добавляемых предметов должно быть типа int")
        if items < 0:
            raise ValueError("Добавляемые предмет ына стол должны быть положительным числом")
        self.items_on_the_table += items
        ...

    def is_empty_table(self) -> bool:
        """
        Функция которая проверяет является ли стол пустым

        :return: Является ли стол пустым

        Примеры:
        >>> table = Table(4, 0)
        >>> table.is_empty_table()
        """
        ...


class Wallet:
    """
    Документация на класс №3.
    Класс описывает модель кошелька
    """
    def __init__(self, material: str, coins: int):
        """
        Создание и подготовка к работе объекта "Кошелек"

        :param material: Материал уошелька
        :param coins: Количество монет в кошельке

        Примеры:
        >>> wallet = Wallet("leather", 4)  # инициализация экземпляра класса
        """
        if not isinstance(coins, int):
            raise TypeError("Количество монет в кошельке быть типа int")
        if coins < 0:
            raise ValueError("Количество монет в кошельке не должно быть отрицательным числом")
        self.material = material
        self.coins = coins

    def is_empty_wallet(self) -> bool:
        """
        Функция которая проверяет является ли кошелек пустым

        :return: Является ли кошелек пустым

        Примеры:
        >>> wallet = Wallet("shammy", 0)
        >>> wallet.is_empty_wallet()
        """
        ...

    def is_wallet_leather(self) -> bool:
        """
        Функция которая проверяет является ли кошелек кожаным

        :return: Является ли кошелек кожаным

        Примеры:
        >>> wallet = Wallet("leather", 100)
        >>> wallet.is_wallet_leather()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
