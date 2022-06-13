print("Welcome to the Shopping Cart Program!\n")

menu_choice = 0

menu_print = "1. Add item\n2. View item\n3. Remove item\n4. Compute total\n5. Quit"

name_list = []
price_list = []
total = 0

while menu_choice != 5:
  print("\nPlease select one of the following:\n")
  print(menu_print)
  menu_choice = int(input("Please enter an action: "))

  if menu_choice == 1:
    name = input("\nWhat item would you like to add? ")
    name_list.append(name)
    price = float(input(f"What is the price of '{name}'? "))
    price_list.append(price)
    print(f"'{name}' has been added to the cart.")

  elif menu_choice == 2:
    range_list = len(name_list)
    print("\nThe contents of the shopping cart are:")
    for i in range(range_list):
      print(f"{i+1}. {name_list[i]} - {price_list[i]}")

  elif menu_choice == 3:
    delete_item = int(input("\nWhich item would you like to remove?\n"))
    del name_list[delete_item - 1]
    del price_list[delete_item - 1]
    print("Item removed.")
  
  elif menu_choice == 4:
    total = 0
    for i in price_list:
      total += i
    print(f"\nThe total price of the items in the shopping cart is ${total}\n")

  elif menu_choice < 0 or menu_choice > 5:
    print("This number is not in the menu choices")



print(name_list, price_list)
print("Thank you. Goodbye")