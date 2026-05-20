# Q7. Even or Odd using Function

print("\n" + "=" * 50)
print("Q7. Even or Odd using Function")
print("=" * 50)

def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

for num in [7, 12, 0, 33, 100]:
    print(f"  {num} -> {check_even_odd(num)}")
