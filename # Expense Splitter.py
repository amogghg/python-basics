# Expense Splitter

expenses = [1200, 850, 1500, 950]

total = sum(expenses)
average = total / len(expenses)

highest = max(expenses)
person = expenses.index(highest) + 1

print("Total Expense:", total)
print("Average Share:", average)
print("Person", person, "paid the highest:", highest)

print("\nEqual Contribution Details:")

for i in range(len(expenses)):
    difference = expenses[i] - average

    if difference > 0:
        print("Person", i + 1, "should receive", difference)
    else:
        print("Person", i + 1, "should pay", abs(difference))