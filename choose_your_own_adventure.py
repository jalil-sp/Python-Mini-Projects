name = input("Type your name: ")
print("welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You've come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()

    if answer == "swim":
        print("You've swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You've walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option, you lose!")

elif answer == "right":
    answer = input("You've come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()

    if answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()

        if answer == "yes":
            print("You talked to the stranger and they give you gold. You WIN!!!")
        elif answer == "no":
            print("You ignored the stranger and he snatches your phone. You LOSE!")
        else:
            print("Not a valid option, you lose!")
    elif answer == "back":
        print("You've gone bak and now you lose.")
    else:
        print("Not a valid option, you lose!")
else:
    print("Not a valid option, you lose!")

print("Thank you for playing", name)