#Cliff Jorgensen
#Kevin Osfar
#Christopher Parks
#Nick

import Entry
import Add
import Search
import Remove
import Update
import pickle

#This program uses the Python pickle module. pickle provides functions for
#file I/O of objects to and from a binary file


def menu():
    print("Choose one option: ")
    print("1 add a new entry to address book")
    print("2 update entry in the address book")
    print("3 remove an entry from the address book")
    print("4 search for an entry in the book")
    print("5 print out the entire address book")
    print("6 EXIT")
    choice = int(input("Enter your choice"))
    return choice
                 
addressBook={}   #addressbook is initially entry

#open file to see if any addresses have been previously entered
try:
    print("This program will read input from address.dat")
    ifile = open("address.dat", "rb")    #open binary file for input
    addressBook = pickle.load(ifile)     #dictionary object read from file
    ifile.close()
except:
    print("AddressBook is empty")


userChoice= menu()
while userChoice != 6:

    if userChoice == 1:  #add entry to addressBook
        Add.addEntry(addressBook)

    elif userChoice == 2:  #update entry to addressBook
        Update.updateEntry(addressBook)

    elif userChoice == 3:  #remove entry to addressBook
        Remove.removeEntry(addressBook)

    elif userChoice == 4:  #search for entry in addressBook
        Search.searchEntry(addressBook)

    elif userChoice == 5:  #print out entire book
        for i in addressBook:
             print(addressBook[i])


    userChoice = menu()

#output dictionary to binary file for next time
try:
    ofile = open("address.dat","wb")   #open binary file for output
    pickle.dump(addressBook, ofile)
    ofile.close()
except:
    print("Error writing file, sorry")

    
    
    


