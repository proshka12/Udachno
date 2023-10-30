from validators import is_valid_name, is_valid_height, is_valid_weight


def get_valid_name_user():
    while True:
        name_user = input("Enter your name (from 4 to 20 symbols): ")
        if is_valid_name(name_user):
            return name_user
        else:
            print("Please enter your name from 4 to 20 symbols")

def get_valid_weight():
    while True:
        try:
            weight = float(input("Enter your weight (kg): "))
            if is_valid_weight(weight):
                return weight
            else:
                print("Please enter your weight in the range 0.01 to 350 kg")
        except ValueError:
            print("Please enter a valid number for your weight")

def get_valid_height():
    while True:
        try:
            height = int(input("Enter your height (cm): "))
            if is_valid_height(height):
                return height
            else:
                print("Please enter your height in the range 10 to 250 cm")
        except ValueError:
            print("Please enter a valid number for your height")