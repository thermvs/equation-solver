def input_number(text):
    while True:
        try:
            number = int(input(text))
            return number
        except ValueError:
            print("Wrong input. Please enter a valid number.")


def input_float(text):
    while True:
        try:
            number = float(input(text))
            return number
        except ValueError:
            print("Wrong input. Please enter a valid number.")