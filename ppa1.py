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
    return math.sqrt( ((float(x2) - float(x1)) ** 2) + ((float(y2) - float(y1)) ** 2) )

def email_verifier(email):
    if (email[0] == '.'):
        return False
    
    for i in range(len(email)):
        if email[i] == '@':
            some_string_1 = email[0:i-1]
            if email[i-1] == '.':
                return False

    for i in range(len(email)):
        if email[i] == '.':
            if email[i+1] == '.':
                return False

    if email[0].isnumeric():
        return False

    chars = set('"(),:;<>@[\]`')
    if any((c in chars) for c in some_string_1):
        return False

    return True

def split_the_tip(amount, guests):
    answer = []
    total = round( (float(amount) * 1.15), 2)
    print(total)
    answer.append(total)
    split = round((total / guests), 2)
    for i in range(guests):
        answer.append(split)
    if split * guests < total:
        answer[guests] += .01
    return answer





# PPA1 Command Line UI
if (__name__ == "__main__"):
    option = 5
    while option != 0:

        # Function selection menu
        print()
        print("PRASCAK PPA1 PROGRAM MENU")
        print("Enter # for function selection.")
        print("0. Exit Program")
        print("1. Calculate BMI")
        print("2. Calculate Retirement Age")
        print("3. Calculate Shortest Distance")
        print("4. Email Verifier")
        print("5. Split the Tip")
        option = input("Function #: ")
        
        # 
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
            x1 = input("X-coordinate of the first point: ")
            y1 = input("Y-coordinate of the first point: ")
            x2 = input("X-coordinate of the second point: ")
            y2 = input("Y-coordinate of the second point: ") 
            print("The shortest distance is: " + str(shortest_distance(x1, y1, x2, y2)))
        elif option == "4":
            email = input("Email address: ")
            if email_verifier(email):
                print("Your email address is valid!")
            else:
                print("Your email address is not valid!")
        elif option == "5":
            bill = input("Bill amount (without tip): ")
            guests = input("Number of guests: ")
            split = split_the_tip(float(bill), int(guests))
            print("Your total bill is: " + str(split[0]))
            if split[int(guests)] > split[int(guests)-1]:
                print("All guests except for one will pay $" + str(split[1]) + ", the last guest will pay $" + str(split[int(guests)]))
            else:
                print("All guests will pay $" + str(split[1]))            