# Зачем нужно наследование
# Задача  "Съедобное, несъедобное"

class Animal:                             # животное
    def __init__(self, name):
        self.alive =  True
        self.fed = False
        self.name = name

    def eat(self, food):                  # съесть
        if isinstance(food, Plant):       # еда - растение?            
            if food.edible:               # съедобно ли?
                self.fed = True
                print(self.name,' съел ', food.name)
            else:
                self.alive = False
                print(self.name,' не стал есть ', food.name)
        else:
            print(food,' не растение')       


class Plant:                            # растение
    def __init__(self, name):  
        self.name = name
        self.edible = False 

class Mammal(Animal):                   # млекопитающее
    # def __init__(self, food):           # еда (растение)
    #     self.food = food
    pass
    

class Predator(Animal):                 # хищник
    pass

class Flower(Plant):                     # цветок
    pass

class Fruit(Plant):                      # фрукт
    def __init__(self, name,):
        super().__init__(name)
        self.edible = True

a1 = Predator('Волк с Уолл-Стрит')

a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')

p2 = Fruit('Заводной апельсин')



print(a1.name)

print(p1.name)



print(a1.alive)

print(a2.fed)

a1.eat(p1)

a2.eat(p2)

print(a1.alive)

print(a2.fed)

       