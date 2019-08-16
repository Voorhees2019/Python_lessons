class Character():
    # константы, что не должны изменятьдя в дальнейшем определяются всеми заглавными буквами
    MAX_SPEED = 100

    def __init__(self, race, damage=100, armor=20):
        self.__race = race   # приватный атрибут (шифруется запутыванием имен). доступ через ._Character__race
        # __race  теперь является приватным атрибутом даного класса Character()
        # и изменение его из вне(через экземпляр класса) не доступно через экземпляр.__race
        # для использования внутри класса
        self.damage = damage
        self.armor = armor
        # _health с одним нижним подчеркиванием - без прямого доступа из вне, а только для использования внутри
        # класса и для его наследников (только на уровне соглашения python сообщества)
        self._health = 100  # защищённый атрибут(не шифруется запутыванием имен)
        self._current_speed = 20

    @property  # доступ к чтению приватного атрибута с помощью СВОЙСТВА(метод, покрытый декоратором @property)
    def health(self):
        return self._health

    @property
    def race(self):
        return self.__race

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, current_speed):
        if current_speed < 0:
            self._current_speed = 0
        elif current_speed > 100:
            self._current_speed = 100
        else:
            self._current_speed = current_speed


unit = Character('Elf')
# print(unit.__race) # AttributeError: 'Character' object has no attribute '__race'
print("UnitRace is " + unit._Character__race)
unit._Character__race = 'Gnome'
print("UnitRace is " + unit._Character__race)
print("UnitHealth = " + str(unit.health))

print("Current speed(default=20) = " + str(unit.current_speed))
unit.current_speed = 50
print("Current speed(set 50) = " + str(unit.current_speed))
unit.current_speed = 500
print("Current speed(set 500) = " + str(unit.current_speed))

