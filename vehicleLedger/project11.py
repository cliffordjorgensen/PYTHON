#Cliff Jorgensen
#Program allows user to enter specified number of vehicles
#prints each vehicle entry after it is stored is a list
#increases and decreases speed, prints new speed after each increment
#prints all vehicles entries in list

import vehicleClass

#main process

vehicleList = [] #empty list

menu = int(input("How many vehicles would you like to add? "))
           
for i in range (menu):  # gather vehicle information from user
    yr = int(input("Enter vehicle year: "))                
    mk = input("Enter vehicle Make: ")
    clr = input("Enter vehicle color: ")
    spd = float(input("Enter starting speed: "))
    
    vehicleEntry = vehicleClass.Vehicle(yr,mk,clr,spd)
    vehicleList.append(vehicleEntry)#adds vehicle object to list
    print()
    for i in range (3): #increase vehicle speed 3 times
        vehicleEntry.speed = vehicleEntry.accelerate() 
        print ("Speed Increase: ", vehicleEntry.speed)
    print()
    for i in range (3): #decrease vehicle speed 3 times
        vehicleEntry.speed = vehicleEntry.brake()
        print ("Speed Decrease: ", vehicleEntry.speed)
        
    vehicleEntry.Vehicle = vehicleEntry.printItems
    print("\nCurrent entry:", vehicleEntry) #print current vehicle stats

for i in vehicleList: 
    print(i)            #print all vehicles in list
    
    

