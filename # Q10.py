# Q10. Prime Number Checker

print("\n" + "=" * 50)
print("Q10. Prime Number Checker")
print("=" * 50)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in [1, 2, 7, 10, 13, 25, 29]:
    print(f"  is_prime({num}) -> {is_prime(num)}")