#Cliff Jorgensen
#Program is an inventory ledger. Allows user to enter new inventory
#returns total inventory and pricing
#Program implements a class module to handle all the relavant operations

import productClass

#main process
prod1 = productClass.Product("Hammers ", 30, 10.00)
prod2 = productClass.Product("Balloons ", 50, 2.50, "Dollar Store")
prod3 = productClass.Product("Bubblegum ", 1500, 0.05, "BJ's")


prod1.printDetails()
print()
prod2.printDetails()
print()
prod3.printDetails()
print()

howmany = int(input("how many " + prod1.name + "were just delivered? "))
prod1.restock(howmany)
prod1.printDetails()

prod1.buyOne()
prod1.buyOne()
prod1.printDetails()

prodList = [ prod1, prod2 ]
prodList.append(prod3)

print("\nThis is the list")
for i in prodList:
    i.printDetails()
    print()
    
print("\nPrinting one object")
print(prod1)

for i in prodList:
    print(i)

print("Product 1 networth is:", prod1.netWorth())

print()
if prod1 < prod2:
    print("we have more of ", prod2.name)

else:
    print("we have more of", prod1.name)
