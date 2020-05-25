import sys


def printRecipe(name):
    global recipes
    name = name.lower()
    if name not in recipes:
        print("ERROR: recipe {} is not in your cook book.".format(name))
    else:
        print("Recipe for {}:".format(name))
        print("Ingredients list: {}".format(recipes[name]["ingredients"]))
        print("To be eaten for {}.".format(recipes[name]["meal"]))
        print("Takes {} minutes of cooking.".format(recipes[name]["time"]))


def deleteRecipe(name):
    global recipes
    name = name.lower()
    if name not in recipes:
        print("ERROR: recipe {} is not in your cook book.".format(name))
    else:
        print("{} has been removed from your cook book.".format(name))
        del recipes[name]


def addRecipe(name, ingredients, meal, time):
    global recipes
    name = name.lower()
    if name in recipes:
        print("ERROR: recipe {} is already in your cook book.".format(name))
    else:
        recipes[name] = {}
        recipes[name]["ingredients"] = ingredients
        recipes[name]["meal"] = meal
        recipes[name]["time"] = time
        print("{} has been added to your cook book.".format(name))


def showCommands():
    print("\nPlease select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")


def commandIsValid(command):
    return (len(command) == 1 and command[0].isdigit()
            and 0 < int(command[0]) < 6)


def askCommand():
    showCommands()
    command = input()
    while not commandIsValid(command):
        commandError()
        command = input()
    return (int(command))


def commandError():
    print("This option does not exist, please type the corresponding number.")
    print("To exit, enter 5.")


def askRecipe():
    name = input("\nRecipe name: ")
    ingredients = input("Ingredients: ").split()
    meal = input("meal: ")
    time = input("prep time: ")
    addRecipe(name, ingredients, meal, time)


def printCookBook():
    global recipes
    if len(recipes) == 0:
        print("\nYour cook book is actually empty.")
    else:
        print("\nActual recipes in your cook book:")
        for recipe in recipes:
            print(recipe)


recipes = {}
addRecipe("Sandwich", ["ham", "bread", "cheese", "tomatoes"], "lunch", 10)
addRecipe("Cake", ["flour", "sugar", "eggs"], "dessert", 60)
addRecipe("Salad", ["avocado", "arugula", "tomatoes", "spinach"], "lunch", 15)
command = -1
while command != 5:
    command = askCommand()
    if command == 1:
        askRecipe()
    elif command == 2:
        deleteRecipe(input("\nPlease enter the recipe's name: "))
    elif command == 3:
        printRecipe(input("\nPlease enter the recipe's name: "))
    elif command == 4:
        printCookBook()
print("\n*Clap!*")
