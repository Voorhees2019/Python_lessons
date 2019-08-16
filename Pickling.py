import pickle  # сериализация(перевод инфы в последовательность битов)


class Character():

    def __init__(self, race, armor=50, damage=10):
        self.race = race
        self.armor = armor
        self.damage = damage
        self.health = 100

    def hit(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health == 0

    # def __getstate__(self):
    #     pass  # какие поля(инфу) пиклить(складывать в файл)
    
    def __setstate__(self, state):
        self.race = state.get('race', 'Elf')  # если значение race не передано, оно присвоится 'Elf' по умолчанию и т.д.
        self.damage = state.get('damage', 10)
        self.armor = state.get('armor', 50)
        self.health = state.get('health', 100)


c = Character('Elf')
c.hit(10)

with open(r'C:\Programming\Lessons\game_state.bin', 'w+b') as f:
    pickle.dump(c, f)  # преобразует состояние объекта в битовое представление. Передаем (объект, файл)

c = None
with open(r'C:\Programming\Lessons\game_state.bin', 'rb') as f:
    c = pickle.load(f)
print(c.health)
print(c.__dict__)

