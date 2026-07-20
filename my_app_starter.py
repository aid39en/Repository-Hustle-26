# ============================================================
# LAB 7 - MY OWN ORDERING APP
# Week 7 - Hack the Hood
# ============================================================
# Name: Aiden H.
#
# My store sells: Phones and Computers
# ============================================================


# ============================================================
# DAY 1 - BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint
class Phone:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # TICKET 3: The price guard
    def set_price(self, price):
        if price < 0:
            print("Price cannot be below zero!")
        else:
            self.price = price

    # TICKET 5: Each item's own action
    def use(self):
        print(f"Preparing your {self.name}!")


# TICKET 4: A second kind of item (inheritance)
class Computer(Phone):
    def use(self):
        print(f"Checking your {self.name}!")


# TICKET 2: Make your real items
item1 = Phone("iPhone 17", 999)
item2 = Computer("MacBook Pro", 1999)
item3 = Computer("Dell XPS Laptop", 1299)

# PREDICT:
# print(item1.name) will show iPhone 17
print(item1.name)


# TICKET 3
# PREDICT:
# This will print a message saying the price cannot be below zero.

item1.set_price(-5)

# Message seen:
# Price cannot be below zero!


# TICKET 5
# EXPLAIN:
# The same method name can do different things because each class
# has its own version of the method.


# ============================================================
# DAY 2 - BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(item.name + " added!")


    # TICKET 9: Checkout
    def checkout(self):
        total = 0

        for item in self.items:
            item.use()
            total += item.price

        print("Total: $" + str(total))


# TICKET 7: My menu and my cart

store = {
    "1": item1,
    "2": item2,
    "3": item3
}

cart = Cart()


# TICKET 8: Let customers shop

# PREDICT:
# Picking 1 will add iPhone 17 to the cart.

while True:
    print("\nPhone & Computer Store")
    print("1 - iPhone 17 ($999)")
    print("2 - MacBook Pro ($1999)")
    print("3 - Dell XPS Laptop ($1299)")

    choice = input("Pick 1, 2, 3, or 'done': ")

    if choice == "done":
        break

    if choice in store:
        cart.add(store[choice])
    else:
        print("Invalid choice.")


# TICKET 10
# PREDICT:
# The items selected will be added to the cart.
# Each item will do its own action.
# The final total will be displayed.

cart.checkout()