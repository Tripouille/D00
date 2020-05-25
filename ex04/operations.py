import sys

usage = "Usage: python operations.py <number1> <number2>\n"
usage += "Example:\n"
usage += "\tpython operations.py 10 3"
argNumber = len(sys.argv) - 1
if argNumber == 0:
    print(usage)
elif argNumber == 1:
    print("InputError: missing argument", usage, sep="\n")
elif argNumber > 2:
    print("InputError: too many arguments", usage, sep="\n")
else:
    try:
        number1 = int(sys.argv[1])
        number2 = int(sys.argv[2])
    except ValueError:
        print("InputError: only numbers", usage, sep="\n")
        quit(-1)
    print("{:<12} {}".format("Sum:", number1 + number2))
    print("{:<12} {}".format("Difference:", number1 - number2))
    print("{:<12} {}".format("Product:", number1 * number2))
    if number2 == 0:
        print("{:<12} ERROR (div by zero)".format("Quotient:"))
        print("{:<12} ERROR (modulo by zero)".format("Remainder:"))
    else:
        print("{:<12} {}".format("Quotient:", number1 / number2))
        print("{:<12} {}".format("Remainder:", number1 % number2))
