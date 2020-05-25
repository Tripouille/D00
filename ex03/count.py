import sys
import string


def text_analyzer(*arg):
    if len(arg) > 1:
        return (print("ERROR"))
    elif len(arg) == 0:
        print("What is the text to analyse?")
        text = sys.stdin.read()
    else:
        text = ''.join(arg)
    print("The text contains {} characters:".format(len(text)))
    print("- {} upper letters".format(sum(map(lambda c: c.isupper(), text))))
    print("- {} lower letters".format(sum(map(lambda c: c.islower(), text))))
    punctuationCount = sum(map(lambda c: c in string.punctuation, text))
    print("- {} punctuation marks".format(punctuationCount))
    print("- {} spaces".format(sum(map(lambda c: c == ' ', text))))
