from sys import exit
from math import sqrt

def linear():
    print("To find X in a linear equation, where ax + b = 0, please enter the values for [a] and [b]:")
    inputvalidator = False
    while inputvalidator == False:
        try:
            a = float(input("\nEnter a: "))
            b = float(input("\nEnter b: "))

        except ValueError:
            print("ERROR! Enter only numerical values.\n")
        else:
            inputvalidator = True
    x = - b / a
    print("For the equation ", a, "x + (", b, ") = 0\nx = ",x)
    print("To calculate a new equation, type N.\nTo go back to the main menu, type M.\nTo quit, press any other key.")
    sel = input("Enter selection: ")
    if sel == 'N' or sel == 'n':
        linear()
    elif sel == 'M' or sel =='m':
        Main()


def quadratic():
    print("To find X in a quadratic equation, where ax² + bx + c = 0, please enter the values for [a] and [b]:")
    inputvalidator = False
    while inputvalidator == False:
        try:
            a = float(input("\nEnter a: "))
            b = float(input("\nEnter b: "))
            c = float(input("\nEnter c: "))
        except ValueError:
            print("ERROR! Enter only numerical values.\n")
        else:
            inputvalidator = True
    delta = b*b - 4 * a * c
    if delta > 0:
        print("Positive discriminant/delta: value of ", delta,". This equation has two different and real roots.")
        print("x' = ", (-b + sqrt(delta) ) /2*a)
        print("x'' = ", (-b - sqrt(delta) ) /2*a)
    elif delta == 0:
        print("Discriminant/delta = 0. This equation has real and same roots.")
        print("x = ", -b / (2 * a))
    else:
        print("Negative discriminant/delta: value of ", delta,". This equation has no real roots, only imaginary/complex.")
        print("x' = ", - b / (2 * a), " + i", delta)
        print("x'' = ",- b / (2 * a), " - i", delta)
    print("To calculate a new equation, type N.\nTo go back to the main menu, type M.\nTo quit, press any other key.")
    sel = input("Enter selection: ")
    if sel == 'N' or sel == 'n':
        quadratic()
    elif sel == 'M' or sel =='m':
        Main()

def Main():
    print("-------------------------\nEQUATION CALCULATOR\n-------------------------\nThis CLI application can find the roots/solution/x of any linear or quadratic equation.\nOPTIONS MENU:")
    inputvalidator = False
    while inputvalidator == False:
        print("[1] - Solve Linear Equation\n[2] - Solve Quadratic Equation\n[0] - Quit the calculator")
        usersel = input("\nEnter your selection: ")
        if usersel == '1':
            inputvalidator = True
            linear()
        elif usersel == '2':
            inputvalidator = True
            quadratic()
        elif usersel == '0':
            print("Terminating...")
            exit(0)
        else:
            print("\nIncorrect input. Please type in 1, 2, or 0 only.\n")

Main()