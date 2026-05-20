# Q5. Mini Shopping Cart

print("\n" + "=" * 50)
print("Q5. Mini Shopping Cart")
print("=" * 50)

items  = ["Apple",  "Milk",   "Bread",  "Eggs",   "Butter"]
prices = [50,       40,       35,       60,       80]

total   = sum(prices)
highest = max(prices)
lowest  = min(prices)

for item, price in zip(items, prices):
    print(f"  {item:<10} ₹{price}")

print(f"\nTotal Bill    : ₹{total}")
print(f"Highest Price : ₹{highest}")
print(f"Lowest Price  : ₹{lowest}")
