color = input("What is your favorite color? ")

if color.lower() == 'red':
    print("Awesome, {} my favorite color is too!" .format(color))
else :
    print("{} is really nice color!".format(color))

age = int(input("How old are you? "))

if age > 23:
    print("{} must be a really good age, I hope I can get that age looking good as you!".format(age))
elif age == 22:
    print("Cool, we have the same Age, {} years old!".format(age))
elif age < 22:
    print("{} is a really good age!" .format(age))







