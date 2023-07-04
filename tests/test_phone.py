import pytest

from src.phone import Phone


@pytest.fixture
def phone1():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    return phone1


def test_phone_init(phone1):
    assert phone1.name == 'iPhone 14'
    assert phone1.price == 120_000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2


def test_phone_repr(phone1):
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim_setter(phone1):
    phone1.number_of_sim = 3
    assert phone1.number_of_sim == 3


def test_number_of_sim_value_error(phone1):
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0