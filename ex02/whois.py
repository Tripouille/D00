import sys
if not len(sys.argv) == 2 or not all(map(lambda c: c.isdigit(), sys.argv[1])):
    print("ERROR")
elif int(sys.argv[1]) == 0:
    print("I'm Zero.")
elif int(sys.argv[1]) % 2:
    print("I'm Odd.")
else:
    print("I'm Even.")
