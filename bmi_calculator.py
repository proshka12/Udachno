def calculate_bmi(weight, height):
    height_m = height / 100
    return weight / (height_m ** 2)