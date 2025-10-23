menu = (''' 
#####################################        
    1: VAT calculator
    2: Tax calculator
    3: Times tables  
_____________________________________        
    ''')
print(menu)

userinput = int(input("Enter the number for the calculator you would like to use: "))

match userinput:
    case 1:
        price = float(input("Enter the price of the object: "))
        _VAT = 1.2
        total = price * _VAT
        print("£" + str(total))
    case 2:
        wage = float(input("Enter your wage: "))
        if wage < 25395.92:
            print("You will not get taxed")
        elif 25395.92 < wage < 37700:
            tax = 0.2
            deduction = wage * tax
            finalTax = round(wage - deduction, 2)
            print("You will have  £" + str(finalTax) + " after tax.")
        elif  37701 < wage < 125140:
            tax = 0.4
            deduction = wage * tax
            finalTax = round(wage - deduction, 2)
            print("You will have £" + str(finalTax) + " after tax.")
        else:
            tax = 0.45
            deduction = wage * tax
            finalTax = round(wage - deduction, 2)
            print("You will have £" + str(finalTax) + " after tax.")
    case 3:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        total = num1 * num2
        print("Your answer is " + str(total))