import re
# make it so that they can save their data and test


def save(name, health, day, level, coins, cages, potions, inventory, potions_used, user_name):
    n = name
    i = ""
    cg = ""
    p = ""
    p_u = str(str(potions_used[0])+" "+str(potions_used[1]))
    for j in inventory:
        i+=j+" "
        i+=str(inventory[j])+" "
    for k in cages:
        cg += k+" "
        cg += str(cages[k][0])+" "
        cg += str(cages[k][1]) + " "
    for l in potions:
        p += l+" "
        p += str(potions[l])+" "

    stuff = str(" "+n+" "+str(health)+" "+str(coins)+" "+str(i)+
                str(cg)+str(p)+str(p_u)+" "+str(day)+" "+str(level))

    f2 = open("User_game_data.txt")
    index_for_f2 = []
    sorted_index_for_f2 = {}
    for y in f2:
        index_for_f2.append(y)
        if len(index_for_f2) == 2:
            l = list(index_for_f2[1].split(" "))
            s = l[2].replace('\n', '')
            l[2] = s
            s = index_for_f2[0].replace('\n', '')
            sorted_index_for_f2[s] = index_for_f2[1]
            index_for_f2 = []
    f2.close()

    sorted_index_for_f2[user_name] = stuff

    d = open("User_game_data.txt", "w")
    for x in sorted_index_for_f2:
        d.write(x)
        d.write(sorted_index_for_f2[x])
    d.close()



def called():
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

    def new_user():
        index = []
        sorted_index = {}
        f = open("Data.txt", "r")
        for x in f:
            index.append(x)
            if len(index) == 2:
                sorted_index[index[0]] = index[1]
                index = []
        f.close()

        us = input("Enter UserName: ")
        pw = input("Enter Password: ")
        hunter_name = input("Name your hunter: ")
        us = us + "\n"
        pw = pw + "\n"
        sorted_index[us] = pw
        print(sorted_index)

        d = open("Data.txt", "w")
        for x in sorted_index:
            d.write(x)
            d.write(sorted_index[x])
        d.close()
        # making new game data and storing it
        user_game_data = hunter_name+" 100 50 nothing 0 () 0 1 nothing 0 0 0 1 1 \n"
        f2 = open("User_game_data.txt")
        index_for_f2 = []
        sorted_index_for_f2 = {us: user_game_data}
        for y in f2:
            index_for_f2.append(y)
            if len(index_for_f2) == 2:
                l = list(index_for_f2[1].split(" "))
                length = len(l)
                s = l[length-1].replace('\n', '')
                l[length-1] = s
                sorted_index_for_f2[index_for_f2[0]] = index_for_f2[1]
                index_for_f2 = []
        f2.close()
        print("This is the sorted index: "+str(sorted_index_for_f2))
        d = open("User_game_data.txt", "w")
        for x in sorted_index_for_f2:
            d.write(x)
            d.write(sorted_index_for_f2[x])
        d.close()

        return us

    def login():
        index = []
        sorted_index = {}
        f = open("Data.txt", "r")
        for x in f:
            index.append(x)
            if len(index) == 2:
                sorted_index[index[0]] = index[1]
                index = []

        print("Enter Username:")
        us = input(": ")

        data = open("Data.txt", "r")
        txt = data.read()
        word = re.findall(us, txt)
        data.close()

        if len(word) == 0:
            print("not found")
            exit()
        else:
            print("found")
            ps = input("Enter Password: ")
            ps = ps + "\n"
            us = us + "\n"
            if ps != sorted_index[us]:
                print("Wrong password")
        return us

    def get_player_data(user_name):
        n = user_name
        print(n)
        # finds username in data
        data = open("User_game_data.txt", "r")
        txt = data.read()
        word = re.findall(n, txt)
        data.close()
        # if it was not found, it will print not found and exit
        if len(word) == 0:
            print("not found")
            exit()
        else:
            # if found it will make a dictionary and get ur data from there
            f2 = open("User_game_data.txt")
            index_for_f2 = []
            sorted_index_for_f2 = {}
            for y in f2:
                index_for_f2.append(y)
                if len(index_for_f2) == 2:
                    l = list(index_for_f2[1].split(" "))
                    s = l[2].replace('\n', '')
                    l[2] = s
                    s = index_for_f2[0].replace('\n', '')
                    sorted_index_for_f2[s] = index_for_f2[1]
                    index_for_f2 = []
            f2.close()
            print("This is all player data: "+str(sorted_index_for_f2))
            size = len(n)
            # Slice string to remove last 3 characters from string
            mod_string = n[:size - 1]
            data = sorted_index_for_f2[mod_string]
            return data, n



    print("="*20+"\n"+"-"*5+"THE HUNTER"+"-"*5+"\n"+"="*20)
    print()
    print("How to play:\nNumbers will appear with choices to choose from. To pick one\n"
          "you will just type in the number associated with the option and hit Enter.\n")
    print("1) Returning Hunter\n 2)New Hunter\n")
    answr = get_user_number(1, 2)
    if answr == 1:
        us = login()
    else:
        us = new_user()

    data = get_player_data(us)

    return data, answr, us
