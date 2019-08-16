from datetime import datetime

lst = [1, 3, 5]
print(lst)
print(repr(lst))
print(eval(repr(lst)) == lst)
print('------------------------')
dt = datetime.now()
print('repr: {}'.format(repr(dt)))
print('str: {}'.format(dt))


class Character():

    def __init__(self, race, damage=10):
        self.race = race
        self.damage = damage
        self.health = 100

    # repr()  # склонен описывать объект(выводить тип...)
    # __repr__ для восстановления объекта или чтения машиной

    def __repr__(self):
        return f'Character("{self.race}", {self.damage})'

    # __str__ для чтения человеком
    def __str__(self):
        return f'{self.race} with damage = {self.damage}'

    # == сравнивает адресса в памяти
    # eq() сравнивает объекты по их внутренним значениям(например, состояние классов)
    def __eq__(self, other):
        if isinstance(other, Character):
            return self.race == other.race and self.damage == other.damage
        return False

    # not equal(!=)/ not necessary in python3
    def __ne__(self, other):
        pass


c = Character('Elf', 40)
print(repr(c))  # по дефолту используется repr репрезентация(если в интерпретаторе просто вписать "c")
print(c)        # str - если идет вывод с помощью print(c)

d = eval(repr(c))
print(type(d))
print(d == c)  # executes dunder method __eq__()


