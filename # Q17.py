# Q17. Student Result Analyzer

print("\n" + "=" * 50)
print("Q17. Student Result Analyzer")
print("=" * 50)

marks_list = [85, 38, 90, 72, 41]

def average(marks):    return sum(marks) / len(marks)
def highest(marks):    return max(marks)
def lowest(marks):     return min(marks)
def passed(marks):     return [m for m in marks if m > 40]

print("Marks     :", marks_list)
print("Average   :", average(marks_list))
print("Highest   :", highest(marks_list))
print("Lowest    :", lowest(marks_list))
print("Passed    :", passed(marks_list))
