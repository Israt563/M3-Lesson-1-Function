# Snack Vending Machine
# File  : vending_machine.py

print("====================================")
print("     Welcome to Snack Vending!      ")
print("====================================")
print()

# PART 1: A function that works out change and sends it back with return
def calculate_change(paid, price):
    change = paid - price
    return change

# PART 2: Snack Menu selection
print("Please select a snack:")
print("  1 - Candy Bar   (Cost: 10)")
print("  2 - Potato Chips (Cost: 15)")
print("  3 - Soda Bottle  (Cost: 25)")
print()

choice = int(input("Enter choice (1, 2, or 3): "))
if choice == 1:
    snack_name = "Candy Bar"
    snack_price = 10
elif choice == 2:
    snack_name = "Potato Chips"
    snack_price = 15
else:
    snack_name = "Soda Bottle"
    snack_price = 25

print()
print(f"You selected: {snack_name}")
print(f"This snack costs {snack_price} units.")
print("Accepted coins: 1, 5, 10, 25\n")

total_inserted = 0
coins_inserted = 0

# PART 3: Keep accepting coins until enough money is inserted
while True:
    coin = int(input("Insert a coin (1, 5, 10, or 25): "))

    # PART 4: Reject any coin that isn't a valid value
    if coin not in [1, 5, 10, 25]:
        print("Invalid coin, try again!\n")
        continue

    # PART 5: Add the valid coin to the running total
    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted {coin}. Total so far: {total_inserted}\n")

    # PART 6: Stop asking for coins once enough has been inserted
    if total_inserted >= snack_price:
        print("Enough money inserted!\n")
        break

# PART 7: Work out the change using the value returned by calculate_change
change_due = calculate_change(total_inserted, snack_price)

print(f"Dispensing your {snack_name}... 🍫")

# PART 8: Break down the change into individual coin denominations
if change_due == 0:
    print("Exact amount paid. No change needed.")
else:
    print(f"Here is your change: {change_due} units")
    
    # Calculate coin breakdown
    remaining_change = change_due
    c10 = remaining_change // 10
    remaining_change %= 10
    c5 = remaining_change // 5
    remaining_change %= 5
    c1 = remaining_change
    
    if c10 > 0: print(f"  {c10} x 10-unit coin(s)")
    if c5 > 0: print(f"  {c5} x 5-unit coin(s)")
    if c1 > 0: print(f"  {c1} x 1-unit coin(s)")

# PART 9: Print a short summary of the purchase
print("\n===== PURCHASE SUMMARY =====")
print(f"Snack Selected  : {snack_name}")
print(f"Snack Price     : {snack_price}")
print(f"Coins Inserted  : {coins_inserted}")
print(f"Total Paid      : {total_inserted}")
print(f"Change Given    : {change_due}")
print("=============================")
print("Thanks for your purchase! 🌟")
print("=============================")