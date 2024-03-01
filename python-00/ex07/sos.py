import sys


# function that translates a string to morse code
def translate_to_morse_code(text):
    NESTED_MORSE = {
        " ": "/", "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....",
        "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
        "O": "---", "P": ".--.", "Q": "--.-",
        "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--",
        "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---",
        "3": "...--", "4": "....-", "5": ".....",
        "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----"
    }

    ret = ""
    for char in text.upper():
        if (char not in NESTED_MORSE):
            print("Unsupported character: " + char)
            return "AssertionError: the arguments are bad"
        ret += NESTED_MORSE[char] + " "
    return ret


def main():
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return 1
    print(translate_to_morse_code(sys.argv[1]))
    return 0


if __name__ == "__main__":
    main()
