import readline
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
        result = parser.parse(expr)
        print(result)

if __name__ == "__main__":
    main()