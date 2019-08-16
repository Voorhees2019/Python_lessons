class Character():

    _instance = None
    # реализация шаблона Singleton: сколько бы экземпляров класса не создавали, вернеться лишь одна инстанция
    # новый экземпляр создаваться не будет(все время возвращается инстанция, созданная в первый раз)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)  # обращаемся к классу Object, вызывая на нем метод __new__,
        return cls._instance                      # передавая инфу(cls) о классе Character

    def __init__(self):
        self.race = 'Elf'


c = Character()
print(c.race)
print('---------------------------')
d = Character()
d.race = 'Ork'
print(c.race)
print(d.race)

