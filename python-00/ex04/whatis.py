import sys


def check_argv():
    if len(sys.argv) == 2:
        num = sys.argv[1]
        if num.isdigit():
            num = int(num)
            if num % 2 == 0:
                print("I'm even")
            else:
                print("I'm odd")
        else:
            print("AssertionError: argument is not an integer")
    elif len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
    return 0


if __name__ == "__main__":
    check_argv()
