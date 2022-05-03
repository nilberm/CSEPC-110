childMeal = float(input("What is the price of a child's meal? "))
adultMeal = float(input("What is the price of a adult's meal? "))
numberOfChildren = int(input("How many children are there? "))
numberOfAdults = int(input("How many adults are there? "))
salesTax = float(input("What is the sales tax rate? ")) / 100
subtotal = (childMeal * numberOfChildren) + (adultMeal * numberOfAdults)
total = subtotal + (subtotal * salesTax)


print(f"\nSubtotal: ${subtotal:.2f}")

print(f"Sales Tax: ${subtotal * salesTax:.2f}")

print(f"Total: ${total:.2f}")

if numberOfAdults > 1:
    splitTheBill = str(input("Will the adults split the bill? [y/N] ")).lower()

    if splitTheBill[0] == 'y':
        individualValue = total / numberOfAdults
        print(f"Each one is going to pay ${individualValue:.2f}")

        print("\nWhat is the payment amount for each one?")

        arrayValue = []
        for x in range(numberOfAdults):
           amount = float(input(f"Amount value adult {x+1}: ")) 
           arrayValue.append(amount)
        for idx, x in enumerate(arrayValue):
            print(f"Change Adult {idx+1}: ${arrayValue[idx] - individualValue:.2f}")
    else: 
        paymentAmount = float(input("\nWhat is the payment amount? "))

        print(f"Change: ${paymentAmount - total:.2f}")
else:
    paymentAmount = float(input("\nWhat is the payment amount? "))

    print(f"Change: ${paymentAmount - total:.2f}")


