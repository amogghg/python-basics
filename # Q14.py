# Q14. Voting Eligibility Checker

print("\n" + "=" * 50)
print("Q14. Voting Eligibility Checker")
print("=" * 50)

ages = (15, 20, 17, 22, 18, 16, 25)

def check_voting(age):
    return "Eligible" if age >= 18 else "Not Eligible"

for age in ages:
    print(f"  Age {age}: {check_voting(age)}")
