print("White two integers numbers bellow")
number = int(input("first number: "))
number2 = int(input("Second number: "))

if (number > number2):
    print("The first number is greater.")
elif (number == number2):
    print("The numbers are equal")
else:
    print("The second number is greater.")

animal = input("What is your favorite animal? ").lower()

if (animal == 'dog'):
    print("That's my favorite animal too!!")
else:
    print("That one is not my favorite.")
