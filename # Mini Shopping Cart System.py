# Mini Shopping Cart System

cart = []
prices = []

while True:

    print("\n1.Add Item")
    print("2.Remove Item")
    print("3.Search Item")
    print("4.Calculate Total Bill")
    print("5.Display Duplicate Items")
    print("6.Show Cart")
    print("7.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))

        cart.append(item)
        prices.append(price)

        print("Item added")

    elif choice == 2:
        item = input("Enter item to remove: ")

        if item in cart:
            index = cart.index(item)

            cart.pop(index)
            prices.pop(index)

            print("Item removed")
        else:
            print("Item not found")

    elif choice == 3:
        item = input("Enter item to search: ")

        if item in cart:
            print(item, "found in cart")
        else:
            print(item, "not found")

    elif choice == 4:
        total = sum(prices)
        print("Total Bill =", total)

    elif choice == 5:
        duplicates = []

        for item in cart:
            if cart.count(item) > 1 and item not in duplicates:
                duplicates.append(item)

        print("Duplicate Items:", duplicates)

    elif choice == 6:
        print("Cart Items:", cart)

    elif choice == 7:
        break

    else:
        print("Invalid choice")