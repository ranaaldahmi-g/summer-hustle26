# ============================================================
# LAB 7  -  MY OWN ORDERING APP
# Week 7  -  Hack the Hood
# ============================================================
# Name: Rana Aldahmi
#
# This is YOUR app. YOU write the code.
# Do the tickets IN ORDER from the Lab 7 sheet.
# Run this file after EVERY ticket to check your work.
#
# My store sells: bags, slides, and sneakers.
# ============================================================


# ============================================================
# DAY 1  -  BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint
#   A class for your item. Every item has a name and a price.
#   Write your class below.

class Bag:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# TICKET 3: The price guard
#   Add a set_price method INSIDE your class above.
#   It should say no to a price below zero.
#   BREAK ON PURPOSE: after you build it, try item1.set_price(-5)
#   PREDICT what happens: error due to the 
#   Paste the message you see here: AttributeError: 'Bag' object has no attribute 'set_price'

class Bag:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_price(self, price):
        if price >= 0:
            self.price = price
        else:
            print("Price cannot be negative.")

bag = Bag("Backpack", 50)
bag.set_price(-5)
print(bag.price)

# TICKET 4: A second kind of item
#   A new class that copies (inherits from) your first class.
#   Write it below.

class Slide(Bag):
    def __init__(self, name, price):
        super().__init__(name, price)
pass # copies everything

# TICKET 5: Each item's own action
#   Give each class its own method (deliver, serve, play...).
#   Same method name, different message.
#   EXPLAIN why the same name can do two things: a method can be defined in multiple classes, and when called on an instance of a specific class, it will execute the method defined in that class. This allows for polymorphism, where the same method name can have different behaviors depending on the object it is called on.

class Bag:
    def deliver(self):
        print("The bag is delivered to the customer.")

class Toy:
    def deliver(self):
        print("The toy is delivered to the child.")

# TICKET 2: Make your real items
#   Make 2 or 3 real items with YOUR OWN names and prices.
#   PREDICT what print(item1.name) shows: It will show the name of the first item created, which is "Backpack".

class Sneaker:
    def __init__(self, name, price):
        self.name = name
        self.price = price

item1 = Sneaker("Air Max", 120)
item2 = Sneaker("Converse", 75)
item3 = Sneaker("Vans", 65)

print(item1.name)

# ============================================================
# DAY 2  -  BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart
#   A class that holds items in a list and can check out.
#   Write your Cart class below.

class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

# TICKET 9: Checkout  (add this method INSIDE your Cart class)
#   Deliver every item and add up the total.

class Bag:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def deliver(self):
        print(f"{self.name} has been delivered.")

class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def checkout(self):
        total = 0
        for item in self.items:
            item.deliver()
            total += item.price
        print("Total:", total)

# Create items
item1 = Bag("Backpack", 50)
item2 = Bag("Tote Bag", 25)

# Add items to cart
cart = Cart()
cart.add(item1)
cart.add(item2)

# Checkout
cart.checkout()


# Example
item1 = Bag("purse", 120)
item2 = Bag("tote", 75)

cart = Cart()
cart.add(item1)
cart.add(item2)

cart.checkout()

# TICKET 7: My menu and my cart
#   A dictionary that gives each item a number, and one empty cart.

# Create items
item1 = Bag("Backpack", 50)
item2 = Bag("Tote Bag", 25)
item3 = Bag("Laptop Bag", 80)

# Dictionary menu
store = {
    "1": item1,
    "2": item2,
    "3": item3
}

# Empty cart
cart = Cart()

# TICKET 8: Let customers shop
#   Use input() and a loop to keep adding picks until "done".
#   PREDICT what happens when you pick 1: It will add the item associated with number 1 (Backpack) to the cart.

# Ask the user what they want
while True:
    choice = input("Enter item number (1, 2, 3) or 'done': ")

    if choice == "done":
        break
    else:
        cart.add(store[choice])

# Checkout
cart.checkout()

# TICKET 10: Test the whole app
#   Run it start to finish. PREDICT the full output first,
#   then check it against what really prints.



# ============================================================
# CHALLENGE: add a THIRD kind of item, or your own feature!
# ============================================================