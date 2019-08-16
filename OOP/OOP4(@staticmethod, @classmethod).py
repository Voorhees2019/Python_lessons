class StaticTest():
    x = 1


print('----------------------------------')
t1 = StaticTest()
print(f'Via instance: {t1.x}')
print(f'Via class: {StaticTest.x}')
print('----------------------------------')
t1.x = 2
print(f'Via instance: {t1.x}')
print(f'Via class: {StaticTest.x}')
print('----------------------------------')
StaticTest.x = 3
print(f'Via instance: {t1.x}')
print(f'Via class: {StaticTest.x}')
print('----------------------------------')


class Date():
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def display(self):
        return f'{self.month}-{self.day}-{self.year}'

    @classmethod
    def millenium_c(cls, month, day):  # первый аргумент статического метода принимает информацию о классе,
        #                              # на котором вызывается
        return cls(month, day, 2000)

    @staticmethod   # не возвращают инстанцию(экземпляр) класса, могут вызиватся через имя класса
    #               # класс не требует состояния(значения атрибутов класса)
    def millenium_s(month, day):
        return Date(month, day, 2000)


d1 = Date.millenium_c(6, 9)
d2 = Date. millenium_s(6, 9)
print(d1.display())
print(d2.display())


class DateTime(Date):
    def display(self):
        return f'{self.month}-{self.day}-{self.year} - 00:00:00 PM'


print('==================================')

dt1 = DateTime(10, 10, 1990)
dt2 = DateTime.millenium_s(10, 10)
print(isinstance(dt1, DateTime))
print(isinstance(dt2, DateTime))
print(dt1.display())
print(dt2.display())

print('==================================')

dt1 = DateTime(10, 10, 1990)
dt2 = DateTime.millenium_c(10, 10)
print(isinstance(dt1, DateTime))
print(isinstance(dt2, DateTime))
print(dt1.display())
print(dt2.display())

print('==================================')


class StrConverter():
    @staticmethod
    def to_str(bytes_or_str):
        if isinstance(bytes_or_str, bytes):
            value = bytes_or_str.decode('utf-8')
        else:
            value = bytes_or_str
        return value

    @staticmethod
    def to_bytes(bytes_or_str):
        if isinstance(bytes_or_str, str):
            value = bytes_or_str.encode('utf-8')
        else:
            value = bytes_or_str
        return value


print(StrConverter.to_str('\x41'))
print(StrConverter.to_str('A'))
print(StrConverter.to_bytes('\x41'))
print(StrConverter.to_bytes('A'))


