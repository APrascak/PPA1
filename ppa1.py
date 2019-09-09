# PPA1 - CIS4930 - Fall 2019
# Alexander Prascak


import math


# PPA1 Functions
def bmi(weight, height):
    return round( ((weight*.45) / (height * .025) ** 2), 1)

def retirement(age, income, saving_rate, savings):
    yearly_saving = (income * (float(saving_rate) / 100)) * 1.35
    time_to_savings = savings / yearly_saving
    answer = round((time_to_savings + age), 1)
    if answer < 100:
        return answer
    else:
        return 100

def shortest_distance(x1, y1, x2, y2):
    return math.sqrt( ((x2 - x1) ** 2) + ((y2 - y1) ** 2) )

def email_verifier(test):
    return 'Email Verifier Function Call'

def split_the_tip(test):
    return 'Split the Tip Function Call'


# PPA1 Command Line UI
if (__name__ == "__main__"):
    option = 5
    while option != 0:

        print()
        print("PRASCAK1 PPA PROGRAM MENU")
        print("Enter # for function selection.")
        print("0. Exit Program")
        print("1. Calculate BMI")
        print("2. Calculate Retirement Age")
        print("3. Calculate Shortest Distance")
        print("4. Email Verifier")
        print("5. Split the Tip")
        option = input("Function #: ")
        
        if option == "0":
            quit()
        elif option == "1":
            weight = input("Weight (in pounds): ")
            height = input("Height (in inches): ")
            bmi = "BMI: " + str(bmi(int(weight), int(height)))
            print(bmi)
        elif option == "2":
            age = input("Age: ")
            income = input("Yearly Income: ")
            saving_rate = input("What % of your income do you save: ")
            savings = input("How much savings would you like to have at retirement: ")
            while float(saving_rate) < 0 or float(saving_rate) > 100:
                saving_rate = input("Please enter a valid saving rate as a % of your income: ")
            print("Your retirement age is: " + str(retirement(float(age), float(income), float(saving_rate), float(savings))) + " years old.")
        elif option == "3":
            print(3)
        elif option == "4":
            print(email_verifier(3))
        elif option == "5":
            print(split_the_tip(3))