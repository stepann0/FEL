from parser import parser
import readline
import colors


def greet():
    print(colors.blue("FEL. Press Ctrl+D to exit."))
    # print("\033[01;38;05;20m"+"FEL. Press Ctrl+D to exit."+"\033[0m")

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