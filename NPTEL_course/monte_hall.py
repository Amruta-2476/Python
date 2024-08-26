# 3 doors and 1 prize
# 1. Contestant chooses a door
# 2. Host opens a door
# 3. Contestant switches or stays
# 4. Contestant wins or loses

#whether to switch or not
import random
doors = [0, 0, 0]  # 0 represents goat
goat_doors = [0] * 2
swap = 0  # number of swap wins
dont_swap = 0  # number of dont swap wins
j = 0
while (j < 10):
    x = random.randint(0, 2)   # xth door will have the prize
    doors[x] = "BMW"
    for i in range(0, 3):
        if i == x:
            continue
        else:
            doors[i] = "Goat"
            goat_doors.append(i)

    choice = int(input("Enter your choice: "))
    door_open = random.choice(goat_doors)  # host will open a door that has a goat
    while door_open == choice:  # door_open should not be equal to the choice made by the contestant
        door_open = random.choice(goat_doors) 

    ch = input("Do you want to swap? y/n: ")
    if ch == "y":  # if the contestant wants to swap
        if doors[choice] == "Goat":    # if the initial choice was a goat, then after swap he will get BMW
            print("You win")
            swap += 1
        else:
            print("You lost")  # if the initial choice was BMW, then after swap he will get a goat
    else:   # does not want to swap
        if doors[choice] == "Goat":
            print("You lost")  # if the initial choice was a goat, then he will get a goat
        else:
            print("You win")  # initial choice was BMW
            dont_swap += 1
    j += 1
print(swap)
print(dont_swap)