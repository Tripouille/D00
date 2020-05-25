import sys
import string


if len(sys.argv) != 3 or sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print("ERROR")
else:
    st = sys.argv[1]
    st = ''.join([c if c not in string.punctuation else ' ' for c in st])
    st = [word for word in st.split() if len(word) > int(sys.argv[2])]
    print(st)
