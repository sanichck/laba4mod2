class Vehicle:
    """
    Базовый класс для всех транспортных средств
    """
    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Инициализация транспортного средства
        Параметры:
            make (str): марка транспортного средства
            model (str): модель транспортного средства
            year (int): год выпуска транспортного средства
        """
        self._make = make
        self._model = model
        self._year = year

    def __str__(self) -> str:
        """
        Возвращает строковое представление транспортного средства
        """
        return f"{self._year} {self._make} {self._model}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление транспортного средства с дополнительной информацией
        """
        return f"Vehicle(make={self._make}, model={self._model}, year={self._year})"

    def start_engine(self) -> str:
        """
        Запускает двигатель транспортного средства
        """
        return "Двигатель запущен"


class Car(Vehicle):
    """
    Класс для автомобилей, наследующийся от Vehicle
    """
    def __init__(self, make: str, model: str, year: int, doors: int) -> None:
        """
        Инициализация автомобиля
        Параметры:
            make (str): марка автомобиля
            model (str): модель автомобиля
            year (int): год выпуска автомобиля
            doors (int): количество дверей
        """
        super().__init__(make, model, year)
        self._doors = doors

    def __str__(self) -> str:
        """
        Возвращает строковое представление автомобиля
        """
        return f"{self._year} {self._make} {self._model}, {self._doors} doors"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление автомобиля с дополнительной информацией
        """
        return f"Car(make={self._make}, model={self._model}, year={self._year}, doors={self._doors})"

    def start_engine(self, mode: str = "normal") -> str:
        """
        Перегрузка метода для запуска двигателя автомобиля
        Параметры:
            mode (str): режим запуска двигателя (например, "standart", "sport", "eco")
        """
        if mode == "sport":
            return "Двигатель автомобиля запустился в спорт режиме"
        elif mode == "eco":
            return "Двигатель автомобиля запустился в эко режиме"
        else:
            return "Двигатель автомобиля запустился в стандартном режиме"

    def honk(self) -> str:
        """
        Сигналит
        """
        return "Bip Bip"


if __name__ == "__main__":
    my_vehicle = Vehicle(make="Toyota", model="Camry", year=2020)
    my_car = Car(make="Honda", model="Civic", year=2021, doors=4)

    print(my_vehicle)
    print(repr(my_vehicle))
    print(my_car)
    print(repr(my_car))
    print(my_vehicle.start_engine())
    print(my_car.start_engine())
    print(my_car.start_engine(mode="sport"))
    print(my_car.start_engine(mode="eco"))
    print(my_car.honk())
