import sys
ar = [c.upper() if c.islower() else c.lower() for c in ' '.join(sys.argv[1::])]
print(*reversed(ar), sep='')
