#Cliff Jorgensen
#ADD Module
#module prompts user for a new entry
#stores new entry in a dictionary, with name as key
#Contact info stored in list under each dictionary key


import Entry

def addEntry(addressBook):
    name = input("\nWhat is the name for the new entry? ")
    name = name.capitalize()
    
    if name in addressBook:
        print("\nSorry, there is already an entry for ", name,"\n")
       
    else:
        email = input("\nWhat is their address? ")
        pho_num = input("\nWhat is their phone number?")
        
        x = Entry.AddressEntry(name, email, pho_num)
        
        addressBook[name] = x
        
        return





                    

