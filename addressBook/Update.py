#Kevin Osfar

import Entry

def updateEntry(addressBook):
    name = input('What is the name for the updated entry? ')
    name = name.lower() #converts name for storage  
    name = name.capitalize() #converts name for dict
    if name not in  addressBook:
        print('Name not in the address book\n')
    else:
        #menu
        print('select which item you want to update.')
        print('1 - update address')
        print('2 - update phone')
        print('5 - EXIT(back to Main Menu)')
        choice = int(input('please enter a 1 or 2 or 5: '))

        while choice != 5:
                
            if choice == 1:
                address = input('Enter their address here: ')
                x = Entry.AddressEntry(name, address, addressBook[name].phone) 
                addressBook[name] = x
                    
            elif choice == 2:
                phone = input('please enter a phone number here: ')
                x = Entry.AddressEntry(name,addressBook[name].address, phone) 
                addressBook[name] = x
                    
            choice = int(input('please enter a 1,2 or 5(main menu)'))
    







