# from abc import ABC, abstractmethod
#
# class Transport(ABC):
#     engine: str
#     model: str
#     mileage: int
#     color: str
#     year_of_release: int
#     maximum_speed: int
#
#     def __init__(self,engine, model, mileage, color, year_of_release, maximum_speed):
#         self.engine = engine
#         self.model = model
#         self.mileage = mileage
#         self.color = color
#         self.year_of_release = year_of_release
#         self.maximum_speed = maximum_speed
#
#     @abstractmethod
#     def start(self, distance):
#         print(f"{self.model} может двигаться")
#
#     @abstractmethod
#     def stop(self, brakes):
#         print(f"{self.model} использует тормоз")
#
#
# class AirTransport(Transport):
#     number_of_seats: int
#     maximum_height: int
#     number_of_chassis: int
#     number_of_wings: int
#
#
#     def __init__(self,engine, model, mileage, color, year_of_release, maximum_speed, number_of_seats,
#                  maximum_height, number_of_chassis, number_of_wings):
#         super().__init__(engine, model, mileage, color, year_of_release, maximum_speed)
#         self.number_of_seats = number_of_seats
#         self.maximum_height = maximum_height
#         self.number_of_chassis = number_of_chassis
#         self.number_of_wings = number_of_wings
#
#
#     def fly(self):
#         print("Может летать")
#
#
# class GraundTransport(Transport):
#     def __init__(self, engine, model, mileage, color, year_of_release, maximum_speed):
#         super().__init__(engine, model, mileage, color, year_of_release, maximum_speed)
#
#     def become_taxi(self, taxi):
#         self.taxi = True


class Automobile:
    model: str
    color: str
    year_of_release: int

    def __init__(self, model, color, year_of_release):
        self.model = model
        self._color = color
        self.__year_of_release = year_of_release

    def start(self):
        print("Старт")

    def stop(self):
        print("Стоп")

    def set_model(self, new_value):
        self.model = new_value

    def set_color(self, new_value):
        self._color = new_value

    @property
    def year_of_release(self):
        return self.__year_of_release

    @year_of_release.setter
    def year_of_release(self, new_value):
        self.__year_of_release = new_value


class Math:
    def __init__(self, a, b):
        if not isinstance(a, (float, int)) or not isinstance(b, (float, int)):
            raise ('Invalid Data')
        self.a = a
        self.b = b

    def myltiply(self):
        print(self.a * self.b)

    def div(self):
        try:
            print(self.a / self.b)

        except ZeroDivisionError as e:
            print(e)