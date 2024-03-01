from ft_filter import ft_filter
import sys


def main():
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return 1
    elif sys.argv[1].isdigit() is False:
        print("AssertionError: the arguments are bad")
        return 1
    else:
        string = sys.argv[1]
        num = int(sys.argv[2])

        filter = list(ft_filter(lambda word: len(word) > num, string.split()))

        print(filter)


if __name__ == "__main__":
    main()
