print("Welcome to the Quiz Game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Perfect! Let's get this game underway!")
score = 0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

answer = input("Are Apple's Mac computers touchscreen? ")

if answer.lower() == "no":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

answer = input("What popular operating system is owned by Microsoft? ")

if answer.lower() == "windows":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

answer = input("IPhones use what operating system? ")

if answer.lower() == "ios":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

print("You got " + str(score) + " questions correct!")
print("Your score is " + str((score / 4) * 100) + "%")