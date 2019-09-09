# PPA1 - CIS4930 - Fall 2019
# Alexander Prascak

def making_bmi(weight, height):
    return round( ((weight*.45) / (height * .025) ** 2), 1)


if (__name__ == "__main__"):
    option = 5
    while option != 0:

        print()
        print("PRASCAK PPA PROGRAM MENU")
        print("Enter # for function selection.")
        print("0. Exit.")
        print("1. Calculate BMI")
        option = input("Function #: ")
        
        if option == "0":
            quit()
        elif option == "1":
            weight = input("Weight (in pounds): ")
            height = input("Height (in inches): ")
            bmi = "BMI: " + str(making_bmi(int(weight), int(height)))
            print(bmi)
