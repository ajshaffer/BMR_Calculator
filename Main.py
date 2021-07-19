import mFormula
import wFormula

weight = float(input("Enter weight in pounds: "))
weightKG = (float(weight) / 2.2)

height = input("Enter height in inches: ")
heightCM = (float(height) * 2.5)

age = float(input("Enter age in years: "))

gender = input("Male or Female?: ")

x = " Calories per day"

if gender == "Male":
    {
        print(str((mFormula.num_1 * weightKG) + (mFormula.num_2 * heightCM) - (mFormula.num_3 * age) + mFormula.num_4) + str(x))
    }
if gender == "Female":
    {
        print(str((wFormula.num_1 * weightKG) + (wFormula.num_2 * heightCM) - (wFormula.num_3 * age) + wFormula.num_4) + str(x))
    }
