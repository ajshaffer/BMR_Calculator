import mFormula
import wFormula

def calorie_Calculator():
    while True:
        try:
            weight = int(input("Enter weight in pounds: "))
            if 1 <= weight <= 1000:
                break
            raise ValueError()
        except ValueError:
            print("Weight must be between 1 and 1000 pounds")

    weight_KG = (float(weight) / 2.2)

    while True:
        try:
            height = int(input("Enter height in inches: "))
            if 1 <= height <= 100:
                break
            raise ValueError()
        except ValueError:
            print("Height must be between 1 and 100 inches.")

    height_CM = (float(height) * 2.5)

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

    x = "You should eat at least this many calories to maintain your current weight."
    y = f" calories per day. \n{x}"

    answer_M = int((mFormula.num_1 * weight_KG) + (mFormula.num_2 * height_CM) - (mFormula.num_3 * age) + (mFormula.num_4))

    answer_F = int((wFormula.num_1 * weight_KG) + (wFormula.num_2 * height_CM) - (wFormula.num_3 * age) + (wFormula.num_4))

    if gender == "Male".lower():
        {
            print("Your basal metabolic rate is " + str(answer_M) + y)
        }
    if gender == "Female".lower():
        {
            print("Your basal metabolic rate is " + str(answer_F) + y)
        }

calorie_Calculator()

#Future: add option to choose whether you want to lose or gain weight
