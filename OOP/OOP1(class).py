class Character():
    # self - доступ к экземпляру класса изнутри самого класса
    def __init__(self, race, hit_points=100, damage=10):  # конструктор(атрибуты)
        self.race = race
        self.damage = damage
        self.hit_points = hit_points


unit = Character('Elf', 200, 50)
print(unit.race)
print(unit.hit_points)
print(unit.damage)
