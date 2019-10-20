# PPA1 - CIS4930 - Fall 2019
# Alexander Prascak


from __future__ import division
from __future__ import absolute_import
import math



# PPA1 Functions
def bmi(weight, height):
    if height < 0:
        return 0
    else:
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
    email = unicode(email,u'utf-8')
    if (email[0] == u'.'):
        return False
    

    # Goal is to refactor this part of the email verification method as part of Refactoring.
    for i in xrange(len(email)):
        if email[i] == u'.':
            if email[i+1] == u'.':
                return False
        if email[i] == u'@':
            some_string_1 = email[0:i-1]
            if email[i-1] == u'.':
                return False

    if email[0].isdecimal():
        return False

    chars = set(u'"(),:;<>@[\]`')
    if any((c in chars) for c in some_string_1):
        return False

    return True

def split_the_tip(amount, guests):
    answer = []
    total = round( (float(amount) * 1.15), 2)
    answer.append(total)
    split = round((total / guests), 2)
    for i in xrange(guests):
        answer.append(split)
    if split * guests < total:
        answer[guests] += .01
    return answer





# PPA1 Command Line UI
if (__name__ == u"__main__"):
    option = 5
    while option != 0:

        # Function selection menu
        print
        print u"PRASCAK PPA1 PROGRAM MENU"
        print u"Enter # for function selection."
        print u"0. Exit Program"
        print u"1. Calculate BMI"
        print u"2. Calculate Retirement Age"
        print u"3. Calculate Shortest Distance"
        print u"4. Email Verifier"
        print u"5. Split the Tip"
        option = raw_input(u"Function #: ")
        
        # 
        if option == u"0":
            quit()
        elif option == u"1":
            weight = raw_input(u"Weight (in pounds): ")
            height = raw_input(u"Height (in inches): ")
            bmi = u"BMI: " + unicode(bmi(int(weight), int(height)))
            print bmi
        elif option == u"2":
            age = raw_input(u"Age: ")
            income = raw_input(u"Yearly Income: ")
            saving_rate = raw_input(u"What % of your income do you save: ")
            savings = raw_input(u"How much savings would you like to have at retirement: ")
            while float(saving_rate) < 0 or float(saving_rate) > 100:
                saving_rate = raw_input(u"Please enter a valid saving rate as a % of your income: ")
            print u"Your retirement age is: " + unicode(retirement(float(age), float(income), float(saving_rate), float(savings))) + u" years old."
        elif option == u"3":
            x1 = raw_input(u"X-coordinate of the first point: ")
            y1 = raw_input(u"Y-coordinate of the first point: ")
            x2 = raw_input(u"X-coordinate of the second point: ")
            y2 = raw_input(u"Y-coordinate of the second point: ") 
            print u"The shortest distance is: " + unicode(shortest_distance(x1, y1, x2, y2))
        elif option == u"4":
            email = raw_input(u"Email address: ")
            if email_verifier(email):
                print u"Your email address is valid!"
            else:
                print u"Your email address is not valid!"
        elif option == u"5":
            bill = raw_input(u"Bill amount (without tip): ")
            guests = raw_input(u"Number of guests: ")
            split = split_the_tip(float(bill), int(guests))
            print u"Your total bill is: " + unicode(split[0])
            if split[int(guests)] > split[int(guests)-1]:
                print u"All guests except for one will pay $" + unicode(split[1]) + u", the last guest will pay $" + unicode(split[int(guests)])
            else:
                print u"All guests will pay $" + unicode(split[1])            