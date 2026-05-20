# Q9. Factorial using Function

print("\n" + "=" * 50)
print("Q9. Factorial using Function")
print("=" * 50)

def factorial(n):
    if n < 0:
        return "Undefined for negative numbers"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

for num in [0, 1, 5, 7, 10]:
    print(f"  {num}! = {factorial(num)}")