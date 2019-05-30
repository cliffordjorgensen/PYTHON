def menu():
    print("*******************GROCERIES*******************\n")
    print("Options:\n\
          (1)Add item to grocery list.\n\
          (2)Remove item from grocery list.\n\
          (3)Find item in grocery list.\n\
          (4)Print the entire list.\n\
          (5)Find out the size of the list.\n\
          (6)Exit.\n")
    choice = int(input("Enter your choice. "))
    while choice < 1 or choice > 6: #invalid choice
        choice = int(input("Re-enter. Value must be between 1 and 5  "))
    return choice

def removeList(list):
    value = input("\nWhat would you like to remove from the grocery list? ")
    if value in list:
        list.remove(value)
    else:
        print(value, "\nis not in the list\n")

def addList(list):
    value = input("\nWhat would you like to add to the grocery list? ")
    if value in list:
        print("\n", value, "is already on the list. \n")
    else:
        list.append(value)
