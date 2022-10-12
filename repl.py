from parser import parser
import readline

def greet():
    print("FEL. Press Ctrl+D to exit.\n")

def main():
    greet()
    while True:
        try:
            expr = input("expr = ")
        except EOFError:
            break
        result = parser.parse(expr)
        print(result)

if __name__ == "__main__":
    main()