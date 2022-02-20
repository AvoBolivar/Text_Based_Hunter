class Animals:
    def __init__(self, name, size, current_population, population_min, repopulation, potion, worth, s_line, e_line):
        self.name = name
        self.size = size
        self.current_population = current_population
        self.population_min = population_min
        self.repopulation = repopulation
        self.potion = potion
        self.worth = worth
        self.s_line = s_line
        self.e_line = e_line

    def reproduce(self):
        self.size += 5

    def check_population_min(self):
        pass

    def print_picture(self, start, end):
        f = open("scratch.txt", "r")
        lines = f.readlines()
        print(*lines[start:end])


# level 4
# dragon

# africa themed becuase of Amina :(((

# level 1
rabbit = Animals("rabbit", 1, 100, 30, [2, 10], .5, 10, 14, 33)
mouse = Animals("mouse", 1, 50, 20, [3, 8], .5, 20, 1, 12)
snake = Animals("snake", 1, 30, 15, [1, 5], .5, 30, 36, 53)
bird = Animals("bird", 1, 25, 20, [1, 3], .25, 30, 54, 62)

# level 2
deer = Animals("antelope", 2, 35, 15, [2, 4], .5, 65, 63, 88)
moose = Animals("Zebra", 2, 200, 150, [10, 20], .5, 50, 88, 113)
brown_bear = Animals("Hyena", 2, 10, 3, [1, 2], .3, 75, 114, 127)
cobra = Animals("cobra", 2, 5, 2, [1, 2], .5, 75, 128, 145)

# level 3
hawk = Animals("hawk", 3, 15, 8, [2, 5], .5, 100, 0, 0)
black_bear = Animals("African Elephant", 3, 6, 2, [1, 3], .5, 125, 0, 0)
hippo = Animals("Rhinoceros", 3, 30, 20, [2, 7], .5, 125, 0, 0)
lion = Animals("Lion", 3, 10, 6, [1, 2], .5, 150, 0, 0)

level_one = [rabbit, mouse, snake, bird]

all_animals = [[rabbit, [mouse, snake], bird], [deer, [moose, brown_bear], cobra], [hawk, [black_bear, hippo], lion]]

animal_populations = {rabbit: rabbit.current_population,
                      mouse: mouse.current_population,
                      snake: snake.current_population,
                      bird: bird.current_population}

animal_sell_price = {rabbit.name: rabbit.worth,
                     mouse.name: mouse.worth,
                     snake.name: snake.worth,
                     bird.name: bird.worth,
                     deer.name: deer.worth,
                     moose.name: moose.worth,
                     brown_bear.name: brown_bear.worth,
                     cobra.name: cobra.worth,
                     hawk.name: hawk.worth,
                     lion.name: lion.worth,
                     hippo.name: hippo.worth}


class Cages:
    def __init__(self, cage, cage_left, cage_right, level, cost, unlock_price, size):
        self.cage = cage
        self.cage_left = cage_left
        self.cage_right = cage_right
        self.level = level
        self.cost = cost
        self.unlock_price = unlock_price
        self.size = size

    def level_up(self):
        self.level += 1
        return self.level


def change_cage_price(cage):
    x = int(cage.cost/3)
    cage.cost += x


level_one_cage = Cages("()", "(", ")", 1, 15, 0, 1)
level_two_cage = Cages("[]", "[", "]", 2, 65, 300, 1)
level_three_cage = Cages("([])", "([", "])", 3, 125, 700, 1)
cages = [level_one_cage, level_two_cage, level_three_cage]


class Potions:
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type


healer = Potions("Healer", 20, 0)
duplicate = Potions("Double", 300, 0)
restore_population = Potions("Restoration", 250, 2)
luck = Potions("Lucky Hand", 120, 1)

potions = [healer, duplicate, luck]
potion_objects = {"Healer": healer, "Double": duplicate, "Lucky Hand": luck}
