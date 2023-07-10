class InstantiateCSVError(Exception):
    """Класс исключения при повреждении файла"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл item.csv поврежден'
