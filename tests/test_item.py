"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item():
    item1 = Item('Мышь', 100, 20)
    return item1


def test_init(item):
    assert item.name == 'Мышь'
    assert item.price == 100
    assert item.quantity == 20


def test_item_total_price(item):
    """Проверяем правильность расчета общей стоимости товара"""
    assert item.calculate_total_price() == 2000


def test_item_apply_discount(item):
    """Проверяем расчет скидки"""
    item.pay_rate = 0.8
    item.apply_discount()
    assert 100 * item.pay_rate == item.price
    assert item.price == 80


def test_item_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_item_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('15.0') == 15
    assert Item.string_to_number('25.5') == 25


def test_name_setter(item):
    item.name = 'Мышка'
    assert item.name == 'Мышка'
    item.name = 'Суперпупермышь'
    assert item.name == 'Суперпупер'


def test_item_repr(item):
    assert repr(item) == "Item('Мышь', 100, 20)"


def test_item_str(item):
    assert str(item) == 'Мышь'
