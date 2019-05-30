#Cliff Jorgensen
#program allows user to update a list of groceries
#add, remove, search, print, find/print size of grocery list.

import numFunc    #functions module

#main process
grocery = []   #empty list
option = numFunc.menu()

while option != 6: #process the option
    
    if option == 1:   #add to list
        numFunc.addList(grocery)
    elif option == 2:  #remove from list
        numFunc.removeList(grocery)
    elif option == 3:  #find in list
        value = input("\nWhat item do you want to find?  ")
        if value in grocery:
            print("\nItem is in list")
        else:
            print(value, "\n is not in the list\n") 
    elif option == 4:  #print entire list
        for i in grocery:
            print(i)
    elif option == 5:  #find out size of list
            print(len(grocery)," items")

    option = numFunc.menu()





