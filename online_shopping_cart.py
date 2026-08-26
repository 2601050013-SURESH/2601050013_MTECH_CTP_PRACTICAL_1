cart = {}

GST_RATE = 18

def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    if name in cart:
        cart[name]["quantity"] += quantity
    else:
        cart[name] = {
            "price": price,
            "quantity": quantity
        }

    print("Product added successfully!")

def remove_product():
    name = input("Enter product name to remove: ")

    if name in cart:
        del cart[name]
        print("Product removed successfully!")
    else:
        print("Product not found in cart.")

def change_quantity():
    name = input("Enter product name: ")

    if name in cart:
        quantity = int(input("Enter new quantity: "))

        if quantity <= 0:
            del cart[name]
            print("Product removed.")
        else:
            cart[name]["quantity"] = quantity
            print("Quantity updated successfully!")
    else:
        print("Product not found.")

def display_cart():
    if not cart:
        print("Cart is empty.")
        return

    print("\n---------- SHOPPING CART ----------")

    for name, details in cart.items():
        price = details["price"]
        quantity = details["quantity"]
        total = price * quantity

        print(
            f"{name} | Price: ₹{price:.2f} | "
            f"Quantity: {quantity} | Total: ₹{total:.2f}"
        )

def calculate_bill():
    if not cart:
        print("Cart is empty.")
        return

    subtotal = 0

    for details in cart.values():
        subtotal += details["price"] * details["quantity"]

    discount_rate = float(input("Enter discount percentage: "))

    discount = subtotal * discount_rate / 100
    amount_after_discount = subtotal - discount

    gst = amount_after_discount * GST_RATE / 100
    final_amount = amount_after_discount + gst

    print("\n========== FINAL BILL ==========")
    print(f"Subtotal              : ₹{subtotal:.2f}")
    print(f"Discount ({discount_rate}%)     : ₹{discount:.2f}")
    print(f"After Discount        : ₹{amount_after_discount:.2f}")
    print(f"GST ({GST_RATE}%)             : ₹{gst:.2f}")
    print("--------------------------------")
    print(f"FINAL AMOUNT          : ₹{final_amount:.2f}")
    print("================================")

while True:
    print("\n===== ONLINE SHOPPING CART =====")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Change Quantity")
    print("4. Display Cart")
    print("5. Calculate Final Bill")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        remove_product()
    elif choice == "3":
        change_quantity()
    elif choice == "4":
        display_cart()
    elif choice == "5":
        calculate_bill()
    elif choice == "6":
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice. Please try again.")
