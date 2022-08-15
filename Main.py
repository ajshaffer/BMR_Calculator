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

def basal_Metabolic_Rate(gender=''):

    answer_Male = int((mFormula.num_1 * weight_KG) + (mFormula.num_2 * height_CM) - (mFormula.num_3 * age) + (mFormula.num_4))

    answer_Female = int((wFormula.num_1 * weight_KG) + (wFormula.num_2 * height_CM) - (wFormula.num_3 * age) + (wFormula.num_4))


    if gender == "Male".lower():
        print("Your basal metabolic rate is " + str(answer_Male) + " calories per day. \nThis means that at rest, you should eat " + str(answer_Male) + " calories to maintain your current weight.")
        return answer_Male
    elif gender == "Female".lower():
        print("Your basal metabolic rate is " + str(answer_Female) + " calories per day. \nThis means that at rest, you should eat " + str(answer_Female) + " calories to maintain your current weight.")
        return answer_Female

BMR_Calculation = basal_Metabolic_Rate(gender)

BMR_Weight_Gain = BMR_Calculation + 500
BMR_Weight_Loss = BMR_Calculation - 500

def calorie_Intake():
    while True:
            try:
                weight_Choice = input("Would you like to gain or lose weight?: ").lower()
                if weight_Choice == "gain" or "lose":
                    break
                raise ValueError()
            except ValueError:
                print('Please enter "gain" or "lose".')

    if weight_Choice == "gain":
        print("You should consume atleast 500 calories more than your basal metabolic rate to gain weight.")
        print("According to your basal metabolic rate, you should consume", + BMR_Weight_Gain, "calories a day.")

    if weight_Choice == "lose":
        print("You should reduce your caloric intake by atleast 500 calories compared to your basal metabolic rate to lose weight.")
        print("According to your basal metabolic rate, you should consume", BMR_Weight_Loss, "calories a day.")

calorie_Intake()