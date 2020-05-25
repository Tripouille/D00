import random


def askNumber():
    print("What's your guess between 1 and 99?")
    return(input())


print("python guess.py")
print("This is an interactive guessing game!")
print(("You have to enter a number between 1 and"
       " 99 to find out the secret number."))
print("Type 'exit' to end the game.")
print("Good luck!")
i = 0
answer = -1
number = random.randint(42, 42)
while answer != number:
    i += 1
    answer = askNumber()
    if answer == "exit":
        print("Goodbye!")
        quit(0)
    while not answer.isdigit() or not 0 < int(answer) < 100:
        print("That's not a number.")
        answer = askNumber()
    answer = int(answer)
    if answer < number:
        print("Too low!")
    elif answer > number:
        print("Too high!")
if number == 42:
    print(("The answer to the ultimate question of life,"
           " the universe and everything is 42."))
if i == 1:
    print("Congratulations! You got it on your first try!")
else:
    print("Congratulations, you've got it!")
    print("You won in {} attempts!".format(i))
