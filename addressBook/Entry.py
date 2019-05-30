#this class represents one entry in an AddressBook

class AddressEntry:
    def __init__(self,newname, newaddress, newphone):
        self.name= newname
        self.address= newaddress
        self.phone= newphone
   
    def __str__(self):
        return self.name + " " + self.address + " " + self.phone
    
             
