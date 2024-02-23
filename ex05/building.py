import sys


def check_argv():
    lower = 0
    upper = 0
    punctuations = 0
    spaces = 0
    digits = 0

    if len(sys.argv) == 2:
        string = sys.argv[1]
        for char in string:
            if char.islower():
                lower += 1
            elif char.isupper():
                upper += 1
            elif char.isdigit():
                digits += 1
            elif char.isspace():
                spaces += 1
            else:
                punctuations += 1
        print("The text contains", len(string), "characters:")
        print(upper, "upper letters")
        print(lower, "lower letters")
        print(punctuations, "punctuations marks")
        print(spaces, "spaces")
        print(digits, "digits")
    elif len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
    else:
        print("you need to provide a string")


if __name__ == "__main__":
    check_argv()
