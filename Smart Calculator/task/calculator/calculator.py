memory = dict()


def make_a_list(smth):
    numbers = [x for x in smth.split()]
    result = 0
    sign = 1
    for number in numbers:
        try:
            result += int(number) * sign

        except ValueError:
            symbols = set(number)
            if len(symbols) == 1:
                sign_in = symbols.pop()
                if sign_in == "+":
                    sign = 1
                elif sign_in == "-":
                    if len(number) % 2 == 0:
                        sign = 1
                    else:
                        sign = -1
                else:
                    pass
            else:
                print("Invalid expression")
    return result


def make_right_part(right_symbols):
    for symbol in right_symbols:
                if symbol.isalpha:
                    if symbol in memory.keys():
                        symbol = memory[symbol]
                    else:
                        print("Unknown variable")
                elif symbol.isdigit() or symbol in ["+", "-"]:
                    pass

                else:
                    print("Invalid assignment")


def take_input(something):
    if something[1:-1].count("=") > 0:
        left, separator, right = something.partition("=")
        left = left.strip()
        if left.isalpha():  # left part is correct
            right = right.strip()
            make_right_part(right.split())

        else:
            print("Invalid identifier")
    elif something[1:-1].count("=") == 0:
        make_right_part(something.strip().split())


def main():
    while True:
        something = input()
        if "=" in something:
            take_input(something)
        elif " " in something and ("+" in something or "-" in something):
            print(make_a_list(something))
        elif something == "/exit":
            print("Bye!")
            exit()
        elif something == "":
            pass
        elif something == "/help":
            print("Print expression you want to count. If you want to add number type '+' or several pluses. Same rule for subtraction")
        else:
            try:
                print(int(something))
            except ValueError:
                if something.startswith("/"):
                    print("Unknown command")
                else:
                    print("Invalid expression")


main()
