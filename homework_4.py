import os
import csv

def get_valid_name_user():
    while True:
        name_user = input("Enter your name (from 4 to 20 symbols): ")
        if 4 <= len(name_user) <= 20:
            return name_user
        else:
            print("Please enter your name from 4 to 20 symbols")

def get_valid_weight():
    while True:
        try:
            weight = float(input("Enter your weight (kg): "))
            if 0.01 <= weight <= 350:
                return weight
            else:
                print("Please enter your weight in the range 0.01 to 350 kg")
        except ValueError:
            print("Please enter a valid number for your weight")

def get_valid_height():
    while True:
        try:
            height = int(input("Enter your height (cm): "))
            if 10 <= height <= 250:
                return height
            else:
                print("Please enter your height in the range 10 to 250 cm")
        except ValueError:
            print("Please enter a valid number for your height")

def calculate_bmi(weight, height):
    """Calculate body mass index"""
    height_m = height / 100
    return weight / (height_m ** 2)

def save_to_file(people, filename):
    if os.path.exists(filename):
        user_response = input(f"The file '{filename}' already exists. Do you want to create a new file? (yes/no): ")
        if user_response.strip().lower() != "yes":
            return  

    with open(filename, "w", newline="") as file:
        file.write("Name ;Weight (kg) ;Height (cm) ;BMI\n")
        for person in people:
            file.write(f"{person['name']} ;{person['weight']} ;{person['height']} ;{person['bmi']}\n")

people = []
while True:
    name = get_valid_name_user()
    weight = get_valid_weight()
    height = get_valid_height()
    bmi = calculate_bmi(weight, height)
    person = {
        "name": name,
        "weight": weight,
        "height": height,
        "bmi": bmi,
    }
    people.append(person)
    another_person = input("Enter 'yes' if you need to enter a new person: ")
    if another_person.lower() != "yes":
        break

save_to_file(people, "bmi.csv")

for person in people:
    print(f"Name: {person['name']}, Weight: {person['weight']:.1f} kg, Height: {person['height']} cm, BMI: {person['bmi']:.2f}")