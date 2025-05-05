import readline
from exec import error
from parser import parser
import colors


def greet():
    print(colors.blue("FEL. Press Ctrl+D to exit."))

def main():
    greet()
    while True:
        try:
            expr = input("expr = ")
        except (EOFError, KeyboardInterrupt):
            break
        try:
            result = parser.parse(expr)
            print(colors.bold(result))
        except Exception as e:
            error(repr(e))
            


if __name__ == "__main__":
    main()
