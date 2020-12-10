class Animal:
    def __init__(self, eat=0, weight=0, voice='', name=''):
        self.eat = eat
        self.weight = weight
        self.voice = voice
        self.name = name
        self.animals = []

    def __str__(self):
        return f'{self.name} , {self.voice}'

    def weight_a(self):
        return self.weight

    def ring(self):
        return self.voice

    def eating(self, kg):
        return self.eat * kg

    def show(self):
        return f'{self.name}'

    def get_animal(self):
        return [animal.show() for animal in self.animals]

    def name_a(self):
        return self.name

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise NotImplementedError('Can not add this object to track list')
        self.animals.append(animal)



class MakeEgg(Animal):
    egg = 1

    def collect_eggs(self, quantity):
        return quantity

class Milk(Animal):
    milk = 0

    def milking(self, liter):
        return self.milk * liter


class Geese(MakeEgg, Animal):
    voice = 'Quack'
    def collect_eggs(self, quantity):
        return quantity

class Cow(Milk, Animal):
    voice = 'Muu'
    milk = 15
    def __str__(self):
        return f'{self.weight}'


class Sheep(Animal):
    voice = 'Bee'
    wool = 15

    def hair_shearing(self, quantity):
        return self.wool * quantity


class Chicken(MakeEgg, Animal):
    voice = 'Co-co'

    def collecting_eggs(self, quantity):
        return quantity

class Goat(Milk, Animal):
    voice = 'Mee'
    milk = 10

    def milking(self, liter):
        return self.milk * liter

class Duck(MakeEgg, Animal):
    voice = 'Quack'

    def collecting_eggs(self, quantity):
        return quantity

ani = []

ani.append(Geese(1, 2, 'Кря', 'Серый'))
ani.append(Geese(1, 2, 'Кря', 'Белый'))

ani.append(Chicken(2, 1, 'Кудах', 'Ко-Ко'))
ani.append(Chicken(2, 1, 'Кудах', 'Кукареку'))

ani.append(Sheep(7, 55, 'Бее', 'Барашек'))
ani.append(Sheep(6, 61, 'Бее', 'Кудрявый'))

ani.append(Goat(3, 80, 'Мее', 'Рога'))
ani.append(Goat(3, 90, 'Мее', 'Копыта'))

ani.append(Cow(10, 90, 'Мууу', 'Манька'))

ani.append(Duck(2, 3, 'Кря', 'Кряква'))


for an in ani:
    print(f'Животное {an.show()} говорит {an.ring()}')

# grey = Geese(1, 2, 'Кря', 'Серый')
# white = Geese(1, 2, 'Кря', 'Белый')

# manka = Cow(10, 90, 'Мууу', 'Манька')

# barashek = Sheep(7, 55, 'Бее', 'Барашек')
# kudryavy = Sheep(6, 61, 'Бее', 'Кудрявый')

# coco = Chicken(2, 1, 'Кудах', 'Ко-Ко')
# cucareca = Chicken(2, 1, 'Кудах', 'Кукареку')

# roga = Goat(3, 80, 'Мее', 'Рога')
# kopyta = Goat(3, 90, 'Мее', 'Копыта')

# cryakva = Duck(2, 3, 'Кря', 'Кряква')



# dict_a = {grey: grey.weight, white: white.weight, coco: coco.weight,
#           cucareca: cucareca.weight, cryakva: cryakva.weight, manka: manka.weight,
#           barashek: barashek.weight, kudryavy: kudryavy.weight, roga: roga.weight,
#           kopyta: kopyta.weight}
#
# count = 0
# for weight_a in dict_a.values():
#     count += weight_a
# print(f'Общий вес животных: {count}')
#
# max_count = 0
# animal_max = 0
# for i, y in dict_a.items():
#     if max_count < y:
#         max_count = y
#         animal_max = i
#
#
# print(f'Самое тяжелое животное: {animal_max}')
# print(f'Молока сегодня {manka.milking(3)} литра')
# print(f'{cryakva.name} съела {cryakva.eating(0.5)} кг зерна')
# print(f'{coco.name} снесла {coco.collecting_eggs(2)} яйца')