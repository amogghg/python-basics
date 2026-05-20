# Q12. Employee Salary Dictionary

print("\n" + "=" * 50)
print("Q12. Employee Salary Dictionary")
print("=" * 50)

employees = {"Amit": 45000, "Priya": 52000, "Ravi": 38000}

def add_employee(name, salary):
    employees[name] = salary
    print(f"  Added: {name} -> ₹{salary}")

def update_salary(name, new_salary):
    if name in employees:
        employees[name] = new_salary
        print(f"  Updated {name}'s salary to ₹{new_salary}")
    else:
        print(f"  Employee '{name}' not found.")

def search_employee(name):
    if name in employees:
        print(f"  {name}: ₹{employees[name]}")
    else:
        print(f"  '{name}' not found.")

add_employee("Sneha", 60000)
update_salary("Amit", 50000)
search_employee("Priya")
search_employee("Raj")
