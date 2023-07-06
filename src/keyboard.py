from src.item import Item


class LayoutMixin:
    LANGUAGE = 'EN'

    def __init__(self):
        """
        Инициализация атрибута LANGUAGE класса LayoutMixin
        """
        self.__language = self.LANGUAGE

    def change_lang(self):
        """
        Смена языка раскладки клавиатуры
        """
        self.__language = 'RU' if self.__language == 'EN' else 'EN'
        return self

    @property
    def language(self):
        """Геттер языка раскладки клавиатуры"""
        return self.__language


class Keyboard(Item, LayoutMixin):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса Keyboard, путем переопределения
        метода __init__ класса-родителя
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара
        """
        super().__init__(name, price, quantity)
