import random

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

# Item blueprint
class Phone:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Price guard
    def set_price(self, price):
        if price < 0:
            print("Price cannot be below zero!")
        else:
            self.price = price

    # Item action
    def use(self):
        print(f"Preparing your {self.name}!")


# Second kind of item (inheritance)
class Computer(Phone):
    def use(self):
        print(f"Checking your {self.name}!")


# Make items
item1 = Phone("iPhone 17", 999)
item2 = Computer("MacBook Pro", 1999)
item3 = Computer("Dell XPS Laptop", 1299)


# ============================================================
# DAY 2 - BUILD YOUR STORE
# ============================================================

# Cart
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(item.name + " added!")

    def checkout(self):
        total = 0

        for item in self.items:
            item.use()
            total += item.price

        print("Total: $" + format(total, ","))


# Products and cart
store = {
    "1": item1,
    "2": item2,
    "3": item3
}

cart = Cart()


# Random welcome message
welcome_messages = [
    "Welcome to the Phones & Computers Store!",
    "Looking for a new device today?",
    "Thanks for visiting Phones & Computers Store!"
]

print(random.choice(welcome_messages))


# Put an item on sale
item1.set_price(899)
print(item1.name + " is on sale for $" + str(item1.price) + "!")


# Show products
print("Here is what we have:")

for number, item in store.items():
    print(number + ": " + item.name + " - $" + str(item.price))


# Shopping loop
while True:
    choice = input("Pick a number, or 'done': ")

    if choice == "done":
        break
    elif choice in store:
        cart.add(store[choice])
    else:
        print("Sorry, that's not on the menu!")


# Receipt
print("----- Your receipt -----")

for item in cart.items:
    print(item.name + " ..... $" + str(item.price))


# Count items
print("You bought " + str(len(cart.items)) + " items.")


# Checkout
cart.checkout()