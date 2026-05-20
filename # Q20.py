# Q20. Mini Banking System

print("\n" + "=" * 50)
print("Q20. Mini Banking System")
print("=" * 50)

balance = 5000  # global balance

def deposit(amount):
    global balance
    balance += amount
    print(f"  Deposited ₹{amount}. New Balance: ₹{balance}")

def withdraw(amount):
    global balance
    if amount > balance:
        print("  Insufficient balance!")
    else:
        balance -= amount
        print(f"  Withdrawn ₹{amount}. New Balance: ₹{balance}")

def check_balance():
    print(f"  Current Balance: ₹{balance}")

check_balance()
deposit(2000)
withdraw(1500)
withdraw(10000)
check_balance()
