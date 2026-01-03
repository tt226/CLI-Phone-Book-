# the program owns the contacts
# so overtime contacts should be accumulated.




# add a menu -> how? checkin with the user for specific options
# add a contact
# view a contact ? access it by search? contact 3? nice?
# quit


# first let's add the buttons: switch statements
# it's a nice alternative to the complex if/else/elif chains


# it can match against various data types and not just litteral values






# state -> long live data
# behavior -> functions that act on that data ()
# control flow -> menu/ loop deciding when behavior runs
contact_list = []# contact list is created
# stage 3: each rerun of the program is basically going to create a new empty list.


def add_contact():
    #n = int(input("How many contacts would you like to add? " ))


   # for i in range (n):
    #print(f"Add your {i+1}'s contact")


    name = input("Enter the name: ")
    email = input("Enter the email: ")
    phone = input("Enter the phone: ")
    # save the contact
    contact = {
        "name": name,
        "email": email,
        "phone" : phone
    }
    # add it to our contact_list
    contact_list.append(contact)
    print(f"Contact added: ")
    print("-" * 20)
    print(f"Name: {contact['name']}")
    print(f"Email: {contact['email']}")
    print(f"Phone: {contact['phone']}")
    print("-" * 20)
    # used for pauses


    return contact_list


# mistake: can't print a dictionay like a list
# kept getting nothing printed for view_contact until i realized that Ihadn't added anything to the contact_list
# so this isn't like a database.
def view_contact(contact_list):
    print("INSIDE PRETTY VIEW")


    for contact in contact_list:
        print("-" * 20)
        print(f"Name:  {contact['name']}")
        print(f"Email: {contact['email']}")
        print(f"Phone: {contact['phone']}")
        print("-" * 20)


     
def delete_contact(contact_list):
    # make sure there's something to delete,
    # if the list is empty we return
    # and let the user know
    if len(contact_list) == 0:
        print("the list is empty, no contacts to delete")
        return
    # this loop is adding a key called index and assigning it the index. how?
    for index, contact in enumerate(contact_list):
        print(f"{index+1}. {contact['name']}")
   
    # assume the user doesn't know shi
    # full proof method to verify user input
    # this index can't be out of bound
    # it also needs to be a valid
    while True:
        choice = input("Enter the number of the contact you want to delete: ")


        if not choice.isdigit():
            print("pls enter a number.")
            continue # will send user back to the prompt


        delete_index = int(choice) - 1


        if delete_index < 0 or delete_index >= len(contact_list):
            print("This number is out of range. Please try again.")
            continue  


        break
    removed = contact_list.pop(delete_index)  


    print(f"Deleted: {removed['name']}")    








while True:
    command = input("Enter a command: ").strip().lower() # normalize the output


    match command:
        case "add":
            print("Let's add a contact")
            add_contact()
        case "view":
            print("Let's view a contact")
            view_contact(contact_list)
        case "delete":
            print("Select the contact you would like to delete")
            delete_contact(contact_list)
        case "quit":
            print("let's quit this game")
           
        case _:
            print("Invalid choice. Please try again")
           
   
   
   
