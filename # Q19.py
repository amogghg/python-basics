# Q19. Contact Book Application

print("\n" + "=" * 50)
print("Q19. Contact Book Application")
print("=" * 50)

contacts = {"Aman": "9876543210", "Pooja": "9123456780"}

def add_contact(name, number):
    contacts[name] = number
    print(f"  Contact '{name}' added.")

def search_contact(name):
    if name in contacts:
        print(f"  {name}: {contacts[name]}")
    else:
        print(f"  '{name}' not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"  '{name}' deleted.")
    else:
        print(f"  '{name}' not found.")

def display_contacts():
    print("  All contacts:", contacts)

add_contact("Raj", "9000012345")
search_contact("Pooja")
delete_contact("Aman")
display_contacts()
