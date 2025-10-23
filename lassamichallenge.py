bags = int(input("Enter the amount of bags: "))
sweets = int(input("Enter the amount of sweets: "))

if sweets < bags:
    print("Must have more sweets than bags")
elif (bags % 2 == 0 and sweets % 2 == 1) or (sweets % 2 == 0 and bags % 2 == 1):
    print("Impossilbe")
else:
    print("Possible")