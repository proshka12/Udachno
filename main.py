import os
import csv
from user_input import get_valid_name_user, get_valid_weight, get_valid_height
from bmi_calculator import calculate_bmi

def save_to_file(people, filename):
    # Your existing save_to_file function here

people = []
while True:
    name = get_valid_name_user()
    weight = get_valid_weight()
    height = get_valid_height()
    bmi = calculate_bmi(weight, height)
    person = {
        "Name": name,
        "Weight (kg)": weight,
        "Height (cm)": height,
        "BMI": bmi,
    }
    people.append(person)
    another_person = input("Enter 'yes' if you need to enter a new person: ")
    if another_person.lower() != "yes":
        break

save_to_file(people, "bmi.txt")

for person in people:
    print(f"Name: {person['Name']}, Weight: {person['Weight (kg)']:.1f} kg, Height: {person['Height (cm')} cm, BMI: {person['BMI']:.2f}")
