#Cliff Jorgensen
#Class module contains methods for inventory quntities

class Product:
    
    def __init__(self,newname,newquan,newprice = 0.0,newsupp = "Home Depot"):
        self.name = newname
        self.quantity = newquan
        self.price = newprice
        self.supplier = newsupp
        return
    
    def printDetails(self):
        print("Name:", self.name)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Supplier:", self.supplier)
        return
    
    def netWorth(self):
        money = self.quantity * self.price
        return money
    
    def __lt__(self, other):
        if self.quantity < other.quantity:
            return True
        else:
            return False
        
    def restock(self, number_delivered):
        self.quantity = self.quantity + number_delivered
        return
    
    def raisePrice(self, percent):
        self.price = self.price + self.price* percent/100
        return
    
    def buyOne(self):
        self.quantity = self.quantity -1
        return
        
    def __str__(self):
        return "Name: " + self.name + "quantity: " + str(self.quantity)
        

