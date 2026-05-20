# Q8. Largest Among Three Numbers

print("\n" + "=" * 50)
print("Q8. Largest Among Three Numbers")
print("=" * 50)

def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print("Largest of 10, 45, 30 :", largest_of_three(10, 45, 30))
print("Largest of 99, 99, 55 :", largest_of_three(99, 99, 55))