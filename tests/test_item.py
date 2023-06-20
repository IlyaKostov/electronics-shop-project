"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item():
    return Item("Мышь", 100, 20)


def test_item_total_price(item):
    '''Проверяем правильность расчета общей стоимости товара'''
    assert item.calculate_total_price() == 2000


def test_item_apply_discount(item):
    '''Проверяем расчет скидки'''
    item.pay_rate = 0.8
    item.apply_discount()
    assert 100 * item.pay_rate == item.price
    assert item.price == 80
