# Q13. Unique Number Counter

print("\n" + "=" * 50)
print("Q13. Unique Number Counter")
print("=" * 50)

# Using a fixed list (replace with input() for interactive use)
numbers = [4, 7, 2, 7, 4, 9, 1, 9, 3, 2]
print("Input list  :", numbers)
unique = set(numbers)
print("Unique set  :", unique)
print("Unique count:", len(unique))