#remove module
#Nicholas Phenner
#this module will take the function removeEntry, and the parameter 'book' a
#which will contain a dictionary, and call it

def removeEntry(book):
    address = input("Please enter a name:").title()
    for k in list(book):
        if address in book:
            del book[address]
            print("The dictionary has been updated.")
        else:
            print("The name is not in the dictionary.")







