contacts = []
def add_data():
        q = int(input("How many contacts do you want to add: "))
        for i in range(q): 
            name = input("Enter Name: ")
            phone = input("Enter Phone number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            contact = {
                    "name": name,
                    "phone": phone,
                    "email": email,
                    "address": address
                }
            contacts.append(contact)

def view_contacts():
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def search_data():
        search_name = input("Enter name or phone number you want to seach:")
        for contact in contacts:
            if search_name == contact["name"] or search_name == contact["phone"]:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
                return
        print("Contact not found..")
    
def update_data():
    update_name = input("Enter name or phone number you want to update: ")

    for contact in contacts:
        if update_name == contact["name"] or update_name == contact["phone"]:

            contact["name"] = input("Enter new Name: ")
            contact["phone"] = input("Enter new Phone number: ")
            contact["email"] = input("Enter new Email: ")
            contact["address"] = input("Enter new Address: ")

            print("Contact updated successfully")
            return

    print("Contact not found..")

print("Welcome to Contact Book")
hey = True
while hey:
     print("1. Add Contact")
     print("2. View Contacts")
     print("3. Search Contact")
     print("4. Update Contact")
     print("5. Exit")
     choice = int(input("Enter your choice: "))
     if choice == 1:
         add_data()
     elif choice == 2:
         view_contacts()
     elif choice == 3:
         search_data()
     elif choice == 4:
         update_data()
     elif choice == 5:
         hey = False
     else:
         print("Invalid choice..")
