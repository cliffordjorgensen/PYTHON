#Cliff Jorgensen
#program stores names and associated email addresses in dictionary
#allows user to add, update, delete, and print entries
#dictionary stores {name:email} pairs, name = key, email = value
#addBook = {}
def menu():
    print("Choices are: \n\n"
          "(1) Add a new entry to addressbook. \n"
          "(2) Update an entry in address book. \n"
          "(3) List all the address book contents. \n"
          "(4) Look up a name in address book. \n"
          "(5) Delete an entry from address book. \n"
          "(6) EXIT.\n")
    option = int(input("Enter menu choice. "))
    while option< 1 or option > 6:
        option = int(input("\nInvalid entry. Please enter (1-6) "))
    return option

def addEntry():
    name = input("\nWhat is the name for the new entry? ")
    name = name.upper()
    if name in addBook:
        print("\nSorry, there is already an entry for ", name,"\n")
    else:
        email = input("\nWhat is their email address? ")
        addBook[name] = email
    return

def upDateEntry():
    name = input("\nWhat is the name for the new entry? ")
    name = name.upper()
    if name not in addBook:
        print("\nName not in address book. ")
    else:
        email = input("\nWhat is their new email address? ")
        addBook[name] = email
    return

def delEntry():
    name = input("\nWho do you want to delete? ")
    name = name.upper()
    if name in addBook:
        print("\n", name, " has been removed.\n ")
        del addBook[name]
        
    else:
        print(name, "is not in the address book. ")
    return

#main process

addBook = {}    #dictionary intially empty
choice = menu()

while choice != 6:  #true until user wishes to exit

      if choice == 1:    #add an entry
          addEntry()
          
      elif choice == 2:    #update an entry
          upDateEntry()
          
      elif choice == 3:    #print all names and emails.
          if len(addBook) == 0:
              print("\nNo names in dictionary. ")
          else:
               for name in addBook:
                   print(name," Email: ", addBook[name],"\n")
                   
      elif choice == 4:    #Look for an entry
          name = input("\nName of person you are looking up: ")
          name = name.upper()
          if name in addBook:
              print("\n ", name,":", addBook[name],"\n")
          else:
              print("\nThis person is not in the book. ")
              
      elif choice == 5:    #delete an entry
          delEntry()
          
      choice = menu()
          
