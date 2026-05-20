# Q11. Attendance System

print("\n" + "=" * 50)
print("Q11. Attendance System")
print("=" * 50)

attendance = ["Alice", "Bob", "Charlie"]

def add_student(name):
    attendance.append(name)
    print(f"  '{name}' added.")

def remove_student(name):
    if name in attendance:
        attendance.remove(name)
        print(f"  '{name}' removed.")
    else:
        print(f"  '{name}' not found.")

def display_students():
    print("  Students:", attendance)

add_student("Diana")
add_student("Eve")
remove_student("Bob")
display_students()