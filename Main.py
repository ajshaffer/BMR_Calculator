import mFormula
import wFormula


while True:
    try:
        weight = int(input("Enter weight in pounds: "))
        if 1 <= weight <= 1000:
            break
        raise ValueError()
    except ValueError:
        print("Weight must be between 1 and 1000 pounds")

weightKG = (float(weight) / 2.2)

while True:
    try:
        height = int(input("Enter height in inches: "))
        if 1 <= height <= 100:
            break
        raise ValueError()
    except ValueError:
        print("Height must be between 1 and 100 inches.")

heightCM = (float(height) * 2.5)

while True:
    try:
        age = int(input("Enter age in years: "))
        if 1 <= age <= 110:
            break
        raise ValueError()
    except ValueError:
        print("Age must be between 1 and 100 years old.")

while True:
    try:
        gender = str(input("What is your gender?: ")).lower()
        if gender == "Male".lower() or gender == "Female".lower():
            break
        raise ValueError()
    except ValueError:
        print("Gender must be Male or Female.")

x = " Calories per day"

if gender == "Male".lower():
    {
        print(str((mFormula.num_1 * weightKG) + (mFormula.num_2 * heightCM) - (mFormula.num_3 * age) + mFormula.num_4) + x)
    }
if gender == "Female".lower():
    {
        print(str((wFormula.num_1 * weightKG) + (wFormula.num_2 * heightCM) - (wFormula.num_3 * age) + wFormula.num_4) + x)
    }
