class Character():
    # атрибуты класса
    max_speed = 100
    dead_health = 0

    # self - доступ к экземпляру класса изнутри самого класса
    def __init__(self, race, damage=10, armor=20):  # конструктор(атрибуты экземпляра класса)
        self.race = race
        self.damage = damage
        self.armor = armor
        self.health = 100

    def hit(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health == Character.dead_health


unit = Character('Elf', 200, 50)
#print(Character.max_speed)
unit.hit(50)
unit.hit(50)
if unit.is_dead():
    print('unit is dead')
else:
    print('unit is still alive')
