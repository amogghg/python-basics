# Q18. Password Strength Checker

print("\n" + "=" * 50)
print("Q18. Password Strength Checker")
print("=" * 50)

def check_password_strength(password):
    checks = {
        "Min length 8": len(password) >= 8,
        "Has digit"   : any(c.isdigit() for c in password),
        "Has uppercase": any(c.isupper() for c in password),
        "Has lowercase": any(c.islower() for c in password),
    }
    print(f"  Password: '{password}'")
    for check, result in checks.items():
        print(f"    {check}: {'✓' if result else '✗'}")
    if all(checks.values()):
        print("    => STRONG PASSWORD")
    else:
        print("    => WEAK PASSWORD")

check_password_strength("hello")
check_password_strength("Hello@123")