class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin_number, __numbers):
        self.model = model
        self.vin_number = vin_number
        self.__numbers = __numbers
        if self.__is_valid_vin() and self.__is_valid_numbers():
            print(f'{model} успешно создан')

    def __is_valid_vin(self):
        try:
            if not (isinstance(self.vin_number, int)):
                message = 'Некорректный тип vin номер'
                raise IncorrectVinNumber(message)
            if self.vin_number < 1000000 or self.vin_number > 9999999:
                message = 'Неверный диапазон для vin номера'
                raise IncorrectVinNumber(message)
        except IncorrectVinNumber as e:
            print(e.message)
        else:
            return True

    def __is_valid_numbers(self):
        try:
            if not (isinstance(self.__numbers, str)):
                message = 'Некорректный тип данных для номеров'
                raise IncorrectCarNumbers(message)
            if not len(self.__numbers) == 6:
                message = 'Неверная длина номера'
                raise IncorrectCarNumbers(message)
        except IncorrectCarNumbers as e:
            print(e.message)
        else:
            return True


first = Car('Model1', 1000000, 'f123dj')
second = Car('Model2', 300, 'т001тр')
third = Car('Model3', 2020202, 'нет номера')
