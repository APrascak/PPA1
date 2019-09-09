# PPA1 - CIS4930 - Fall 2019
# Alexander Prascak

def bmi(weight, height):
    return round( ((weight*.45) / (height * .025) ** 2), 1)

def retirement(age, income, saving_rate, savings):
     return 2

def shortest_distance(test):
    return 'Shortest Distance Function Call'

def email_verifier(test):
    return 'Email Verifier Function Call'

def split_the_tip(test):
    return 'Split the Tip Function Call'


if (__name__ == "__main__"):
    option = 5
    while option != 0:

        print()
        print("PRASCAK PPA PROGRAM MENU")
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
            print(retirement(3))
        elif option == "3":
            print(shortest_distance(3))
        elif option == "4":
            print(email_verifier(3))
        elif option == "5":
            print(split_the_tip(3))