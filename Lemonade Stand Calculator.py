# Lemonade Stand Calculator
# File  : lemonade_stand.py

print("====================================")
print("     Welcome to Lemonade Stand!     ")
print("====================================")
print()

# PART 1: Define a function with no arguments to greet the customer
def greet_customer():
    print("Fresh lemonade, made just for you! 🍋")
    print("-" * 36)

# PART 2: Call the greet_customer function
greet_customer()
print()

# PART 3: Ask for the price per cup and the number of cups sold
price_per_cup = float(input("Enter the price per cup in dollars (e.g., 1.50): "))
cups_sold = int(input("Enter the number of cups sold: "))
print()

# PART 4: Define a function that takes arguments and returns the total cost
def calculate_total(price, cups):
    total = price * cups
    return total

# PART 5: Call calculate_total and store the value it returns
total_cost = calculate_total(price_per_cup, cups_sold)

# PART 6: Use a built-in function to round the total, then print it
rounded_total = round(total_cost, 2)

# PART 7: Ask how much money the customer paid
amount_paid = float(input("Enter the amount paid by the customer: "))

# PART 8: Define a function that takes arguments and returns the change due
def calculate_change(paid, total):
    change = paid - total
    return change

# PART 9: Call calculate_change and store the value it returns
change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

# PART 10: Define a function that returns a thank you message based on cups sold
def thank_you_message(cups):
    if cups >= 5:
        return "🎉 Wow, big order! Thanks so much for your support!"
    else:
        return "👍 Thanks for stopping by the stand!"

# PART 11: Call thank_you_message and store the value it returns
closing_message = thank_you_message(cups_sold)

# PART 12: Print the final lemonade stand receipt
print()
print("====================================")
print("===== LEMONADE STAND RECEIPT =======")
print("====================================")
print(f"Price Per Cup : ${price_per_cup:.2f}")
print(f"Cups Sold     : {cups_sold}")
print(f"Total Cost    : ${rounded_total:.2f}")
print(f"Amount Paid   : ${amount_paid:.2f}")

if amount_paid >= rounded_total:
    print(f"Change Due    : ${rounded_change:.2f}")
else:
    print("Warning       : Insufficient payment! ⚠️")

print("-" * 36)
print(closing_message)
print("====================================")