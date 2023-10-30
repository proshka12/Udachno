import os
import csv
from user_input import get_valid_name_user, get_valid_weight, get_valid_height
from bmi_calculator import calculate_bmi

def save_to_file(people, filename):
    # Your existing save_to_file function here
    pass
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

save_to_file(people, "bmi.txt")

for person in people:
    print(f"Name: {person['name']}, Weight: {person['weight']:.1f} kg, Height: {person['height']} cm, BMI: {person['bmi']:.2f}")
