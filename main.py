import os
import keyboard
import time
import animal_index
import random
import login

# TODO think about how capturing the dragon is going to work
# TODO add log in

# TODO pick up where i left off starts at lines 63
# make sure all if statements have an else
# Dragon has been made in instructions and dialogue
# the requirments needed to beat the dragon
# you need all 3 cages to be a level 4 and then
# money to weld them together into a big cage
# this will be called the dragons cage
# an entire funtion wil be used for the dragon capture
# after the game will end
# Showing how many days it took
# how many animals captured in total
# how much money made in total


# clears the board
clear = lambda: os.system('cls')


def get_user_number(min=-1, max=100000000):
    x = input(": ")
    valid = False
    while not valid:
        if x.isnumeric() == True:
            if min <= int(x) <= max:
                break
        print("not valid input, please enter a number")
        x = input(": ")
    return int(x)


def show_inventory(inventory):
    print(("~" * 3) + "Inventory" + ("~" * 3))
    for x in inventory:
        print(x + ("-" * 9) + f"{inventory[x]}")


def using_potions(potions, h, potions_used):

    p = potions
    h = health
    pinu = potions_used
    print("Available Potions\n" + "-" * 10)
    count = 1

    if potions:
        for i in potions:
            print(f"{count}"+") "+i+("-" * 9) + f"{potions[i]}")
            count += 1
    else:
        print("empty")

    print("*enter "+f"{count}"+" to exit*")
    print(count)
    print("Which potion would you like to use?")
    u_i = get_user_number(1, count+1)-1
    # i need to know what potion they are using and implement correctly
    if u_i+1 == count:
        print("Good bye")
        time.sleep(1)
    else:
        print("How many would you like to use?")
        u_ii = get_user_number()
        potion_name = list(potions.keys())[u_i]
        potion_amnt = potions[potion_name]
        print(potion_amnt)
        if potion_amnt >= u_ii:
            # specific to healer
            if potion_name == "Healer":
                h += 20*u_ii
            else:
                # this adds one to the list
                x = animal_index.potion_objects[potion_name].type
                place_holder = pinu[x] + 1
                pinu[x] = place_holder
            # this takes it away from inventory
            amnt = p[potion_name]
            amnt -= u_ii
            p[potion_name] = amnt
        else:
            print("You do not have that many potions")
            time.sleep(1.5)

        input("Press enter to continue")

    return p, h, pinu


def store(inventory, coins, level, cages, potions):
    clear()

    # buys cages
    def buy_cage(coins, cages, level):
        print("--Display--")
        for i in range(level):
            print(f"{i+1}"+") "+animal_index.cages[i].cage+"-"*5+f"{animal_index.cages[i].cost}")
            if i == 2:
                break
        print()
        print("What would you like to buy?\n * Enter number *\n")
        item_index = get_user_number(1, level)-1
        print()
        print("How many would you like to buy:")
        amnt = get_user_number()
        item = animal_index.cages[item_index]
        item_symbol = item.cage
        print("-"*7)
        price = item.cost*amnt
        print("Total: $"+f"{price}")
        input("press enter to confirm")
        if price <= coins:
            if item_symbol in cages:
                x = cages[item_symbol][0]
                x += amnt
                cages[item_symbol][0] = x
            else:
                cages[item_symbol] = [amnt, 1]
            coins -= price
        else:
            print("not enough money")
        return coins, cages

    def upgrade(coins, cages):
        print("\nWhich Cage would you like to upgrade")
        cg = cages
        c = coins
        count = 1
        cg_apendex = animal_index.cages
        for i in range(level):
            print(f"{i+1}"+") "+cg_apendex[i].cage+" "+"-"*8+" "+f"{cg_apendex[i].cost*2}")
        print("Which cage would you like to upgrade?\nEnter number or 0 to exit")
        u = get_user_number(0, count)
        if u == 0:
            return coins, cages
        else:
            if c >= cg_apendex[u-1].cost*2:
                the_cage = cg_apendex[u-1]
                cg[the_cage.cage][1] = cg_apendex[u-1].level_up()
                animal_index.change_cage_price(the_cage)
                c -= cg_apendex[u-1].cost*2
            else:
                print("You do not have enough money")
                time.sleep(1.5)
        return c, cages

    def sell(inventory, coins):
        print()
        c = coins
        inven = inventory
        coins_earned = 0
        print("Would you like to sell all your animals?")
        print("1) yes\n2) No")
        answr = get_user_number(1, 2)
        if answr == 1:
            for i in inventory:
                in_stock = inventory.get(i)
                coins_earned += in_stock*animal_index.animal_sell_price[i]
            c += coins_earned
        print("Total made: "+f"{coins_earned}")
        input("hit enter to continue")
        inven.clear()
        return inven, coins_earned, c

    def buy_potions(coins, potions):
        clear()
        c = coins
        p = potions
        print("-"*3+"The Laboratory"+"-"*3)
        print()
        p_list = animal_index.potions
        for i in range(len(p_list)):
            print(f"{i+1}"+") "+p_list[i].name+"-"*5+f"{p_list[i].price}")
        print("_"*12)
        print()
        print("for a description of each potion enter 5")
        print()
        print("What would you like to buy? * enter the number *")
        item = get_user_number(1, len(p_list))-1
        item = p_list[item]
        print("How many would you like to buy?")
        amnt = get_user_number()
        price = item.price*amnt
        print("Total: "+f"{price}")
        input("press enter to confirm")
        # here im putting the actual item in the list instead of the item name
        if coins > price:
            if item in potions:
                x = p[item.name]
                x += amnt
                p[item.name] = x
            else:
                p[item.name] = amnt
            c -= price
        else:
            print("not enough money")
            time.sleep(1.5)
        return c, p


    print(" "*5+"Store")
    print("-"*15)
    print("Coins: "+f"{coins}")
    print("-"*10+"\n")
    print("1) Buy Cages\n2) Upgrade Cages\n3) Sell Animals\n4) Buy Potions\n5) leave the store")
    print("*Enter number to choose option*")
    user = get_user_number(1, 5)
    inven = inventory
    cg = cages
    p = potions
    c = coins
    if int(user) == 1:
        c, cg = buy_cage(coins, cages, level)
    elif int(user) == 2:
        c, cg = upgrade(c, cg)
    elif int(user) == 3:
        inven, coins_made, c = sell(inventory, coins)
    elif int(user) == 4:
        c, p = buy_potions(c, potions)
    elif int(user) == 5:
        print("leaving...")

    print("="*10)
    print("Are you done shopping?\n1) yes\n2) no")
    us_an = get_user_number(1, 2)
    if us_an == 1:
        return inven, c, cg, p
    else:
        inven, c, cg, p = store(inven, c, level, cg, p)
        return inven, c, cg, p


# once animal is captured
def hunt_captured(inventory, cage_type, cage_level, potions_used):
    inven = inventory
    # luck is one - meaning they will only get rare types
    # double is zero - meaning they will get double the animals caught
    pinu = potions_used
    # it picks randomly from list of animals
    if pinu[1] > 0:
        holder = pinu[1]
        pinu[1] = holder - 1
        x = random.randint(45, 100)
    else:
        x = random.randint(0, 100)
    if x < 40:
        catch = 0
    elif x < 80:
        catch = 1
    else:
        catch = 2
    if catch != 1:
        animal = animal_index.all_animals[cage_type][catch]
    else:
        other = random.randint(0, 1)
        animal = animal_index.all_animals[cage_type][catch][other]
    print("Congratulations you caught a", animal.name)
    # prints the picture of the animal
    animal.print_picture(animal.s_line, animal.e_line)
    # gives stats on the animal
    print()
    print("Information on the " + animal.name)
    # print("Current population: "+ str(animal.current_population)+"\nMinimum Population: "+ str(animal.population_min))
    print("Value: "+f"{animal.worth}")
    print()
    print("Would you like to keep the animal or let it go?")
    print("1) keep\n2) Let it go")
    user = get_user_number(1, 2)
    if user == 1:
        if animal.name in inven:
            stock = inven.get(animal.name)
            if pinu[0] > 0:
                holder = pinu[0]
                pinu[0] = holder - 1
                stock += animal_index.cages[cage_type].level*2
            else:
                stock += animal_index.cages[cage_type].level
            print(cage_level)
            inven[animal.name] = stock
        else:
            inven[animal.name] = animal_index.cages[cage_type].level

    return inven, pinu


# if animal gets away
def hunt_escaped(index):
    print("the animal got away")
    print(index)
    time.sleep(1.5)


# hunting mechanics
def hunting(cages, level, inventory, health, cage_type, potion_used):
    # cage type defines the size and speed of the animal
    # sets variables
    inven = inventory
    cg = cages
    h = health
    pinu = potion_used
    cage_left = animal_index.cages[cage_type].cage_left
    cage_right = animal_index.cages[cage_type].cage_right
    actaul_cage = animal_index.cages[cage_type].cage

    # enemy data
    cage_size = cages[actaul_cage][1]
    print(cage_size)
    enemy_size = cage_type+1
    enemy_speed = 5-cage_type
    enemy = list("_"*(10+(cage_size*2)))
    position_of_cage = random.randint(0, len(enemy)-2)
    target = ("*"*cage_size)
    slot = ("_"*cage_size)
    player_slot = cage_left+slot+cage_right
    enemy_in_player = cage_left+target+cage_right
    index = 0
    cycle = 0
    # inserting player slot in enemy
    center = int(enemy_size/2)
    enemy.pop(center)
    enemy.insert(center, player_slot)
    free = True
    while free:
        # takes health away from player as soon as battle starts and every cycle
        h -= 1
        # the enemy cycling through list
        # puts the enemy in the slot
        # going to generate random number, so that the cage is in a new spot everytime
        if index == position_of_cage:
            enemy.pop(index)
            enemy.insert(index, enemy_in_player)
        else:
            enemy.pop(index)
            enemy.insert(index, target)
        print(*enemy)
        for i in range(enemy_speed):
            if keyboard.is_pressed("s"):
                free = False
            time.sleep(.1)
        clear()
        # replaces it back to empty slot
        if index == position_of_cage:
            enemy.pop(index)
            enemy.insert(index, player_slot)
        else:
            enemy.pop(index)
            enemy.insert(index, slot)
        # once it gets to the end of the list it resets
        if index > len(enemy)-2:
            index = 0
            cycle +=1
            if cycle > 2:
                break
        # check to see if the player wants to capture
        index += 1
    if index == position_of_cage+1:
        time.sleep(.5)
        inven, pinu = hunt_captured(inventory, cage_type, cg[actaul_cage][0], pinu)
    else:
        hunt_escaped(index)
    stock_cg = cg[actaul_cage][0]
    stock_cg -= 1
    cg[actaul_cage][0] = stock_cg
    return inven, cg, h, pinu


# the main menu
def main_menu(name, health, day, level, coins, cages, potions, inventory, potions_used, user_name):
    # printing the main menu
    clear()
    # check for if they meet the standards for the Dragon
    # amount = 0 and level = 1 for cages in the list
    dragon_ready = 0
    if level>=3:
        if len(cages) >= 3:
            if cages["()"][0] >= 5 and cages["()"][1] >= 4:
                if cages["[]"][0] >= 4 and cages["[]"][1] >= 3:
                    if cages["([])"][0] >= 3 and cages["([])"][1] >= 2:
                        dragon_ready = 1

    v = [name, health, day, level, coins, cages, inventory, potions_used]
    print(" "*8+"\nMain MENU\n"+"=~"*16)
    print("Hello, {}\nIt's day {}\nLevel: {}\nHealth: {}\nCoins: {}\n".format(name, day, level, health, coins))
    print(("~"*8)+"Cages"+("~"*8))
    print("Cage"+" "*3+"Amount"+" "*3+"Level")
    # to get index in list of cages in animal.py
    count = 0
    for i in cages:
        print(" "+animal_index.cages[count].cage+(" "*6)+f"{cages[i][0]}"+(" "*8)+f"{cages[i][1]}")
        count += 1
    print()
    print(("~" * 3) + "Inventory" + ("~" * 3))
    if inventory:
        for i in inventory:
            print(i+("-"*9)+f"{inventory[i]}")
    else:
        print("empty")
    print()
    print("~"*3+"Potions"+"~"*3)
    if potions:
        for i in potions:
            print(i+("-"*9)+f"{potions[i]}")
    else:
        print("empty")
    print()
    print(potions_used)
    print()
    # amount of options in main menu
    main_menu = 4
    # extra part is the player having the options to check requirements for the dragon
    if level >= 3:
        if dragon_ready ==1:
            dragon_part = "\n5) Capture the Dragon"
            main_menu += 1
        else:
            dragon_part = ""
        extra_part = "\n4) Check requirements for the Dragon"
        main_menu += 1
    else:
        extra_part = ""
        dragon_part = ""
    print(("~"*3)+"Options"+("~"*3))
    print("1) Store\n2) Hunt\n3) Use potion\n4) Save Game"+extra_part+dragon_part)
    print()
    us = get_user_number(1, main_menu)
    h = health
    inven = inventory
    c = coins
    cg = cages
    p = potions
    pinu = potions_used

    if us == 1:
        inven, c, cg, p = store(inventory, coins, level, cages, potions)
    elif us == 2:
        # list of how much of each cage player is taking
        cgs_being_taken = []
        # looping through the different types of cages and asking how many they wanna take
        for i in cg:
            print("How many of these:{} would you like to take: ".format(i))
            amnt_of_cages = (cg.get(i)[0])
            reps = get_user_number(-1, amnt_of_cages)
            # adding that number to the list
            cgs_being_taken.append(reps)
        # this just explains hunting to the player the first time they go hunting
        print()
        if day <= 2:
            print("Some advice: ")
            f = open("instructions and dialogue.txt", "r")
            lines = f.readlines()
            print(*lines[17:21])
            print()
            input("*When your ready hit enter*")
        # going to repeat for each type of cage available
        # for index in list

        if sum(cgs_being_taken) > 0:
            for i in range(len(cgs_being_taken)):
                # for the amount in that index
                for j in range(cgs_being_taken[i]):
                    # run hunting
                    inven, cg, h, pinu = hunting(cg, level, inven, health, i, potions_used)
        else:
            print("You can not hunt without taking cages")
            print("Returning to main menu")
            time.sleep(1.5)
    elif us == 3:
        clear()
        p, h, pinu = using_potions(potions, health, potions_used)
    elif us == 5:
        read_txt("four")
        input()
    elif us == 4:
        login.save(name, health, day, level, coins, cages, potions,
                   inventory, potions_used, user_name)

    return inven, c, cg, h, p, pinu


def level_up(lvl):
    clear()
    f = open("instructions and dialogue.txt", "r")
    lines = f.readlines()
    print(*lines[30:37])
    print("You are now a level " + str(lvl))
    print()
    input("*press enter to continue*")
    if level == 3:
        read_txt("three")
    input("*press enter to continue*")


def read_txt(part):
    f = open("instructions and dialogue.txt", "r")
    lines = f.readlines()
    if part == "intro":
        print(*lines[1:5])
    if part == "intro two":
        print(*lines[8:13])
    if part == "three":
        print()
        print(*lines[40:51])
    if part == "four":
        clear()
        print(*lines[46:52])



def intro():
    read_txt("intro")
    print()
    read_txt("intro two")
    input("press enter to continue to main menu")


if __name__ == '__main__':
    data, answr, user_name = login.called()
    print(data, answr, user_name)
    str = ''.join(data)
    d = str.split()
    print(d)
    name = d[13][1:]
    print(name)
    print()
    intro()
    health = 100
    coins = 50
    inventory = {"nothing": 0}
    if "nothing" in inventory:
        inventory.clear()
    cages = {"()": [0, 1]}
    potions = {"nothing": 0}
    if "nothing" in potions:
        inventory.clear()
    potions_in_use = [0, 0]
    day = 0
    level = 1

    while True:
        if coins >= (level * 2) * 100:
            level += 1
            level_up(level)

        day += 1
        inventory, coins, cages, health, potions, potions_in_use = main_menu(name, health, day, level,
                                                             coins, cages, potions, inventory,
                                                             potions_in_use, user_name)
