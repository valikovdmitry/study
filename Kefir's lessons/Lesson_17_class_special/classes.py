# инкапсуляций - запихнуть в капсулу - скрыть все внутри

# объектно ориентированное программирование

# класс - описание структуры данных поля и методы

# camal case - каждая первая большая - название класса // snake case - через нижнее - так переменные и методы // костанта большими

class Fruit:
    def __init__(self, color, dia, taste):
        self.color = color
        self.dia = dia
        self.taste = taste

    def get_dia_cm(self):
        return int(self.dia * 100)

    def set_dia(self, new_dia):
        self.dia = abs(new_dia)

    def set_color(self, new_color):
        self.color = new_color


# создаем экземпляр класса
# get и set функции
fruit = Fruit('red', 0.3, 'sweet')
fruit.dia = -4
fruit.set_dia(-4)
print(fruit.__dict__)
print(fruit.get_dia_cm())


# нупрямую наследует поля и методы из род класса - наследование
class GreenApple(Fruit):
    def __init__(self, dia, taste, country):
        super(GreenApple, self).__init__('green', dia, taste)   # проинициализиуй мне предка - вызови функцию инит
        self.country = country

    def set_color(self, new_color):  # полиморфизм - разные функции для предка и потомка = переопределить функцию селф колор
        pass

green = GreenApple(0.3, 'sour', 'tyrkey')
print(green.color)
print(green.get_dia_cm())


# наследование, полиморфизм, инкапсуляция




