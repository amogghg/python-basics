# Q1. Student Marks Manager

print("=" * 50)
print("Q1. Student Marks Manager")
print("=" * 50)

marks = [85, 72, 90, 60, 78]
print("Original marks:", marks)

marks.append(95)
print("After append(95):", marks)

marks.insert(2, 88)
print("After insert(2, 88):", marks)

marks.remove(60)
print("After remove(60):", marks)

marks.sort()
print("After sort():", marks)