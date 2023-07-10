from src.instantiate_csv_error import InstantiateCSVError


def test_instantiate_csv_error_init():
    error = InstantiateCSVError()
    assert error.message == 'Файл item.csv поврежден'
