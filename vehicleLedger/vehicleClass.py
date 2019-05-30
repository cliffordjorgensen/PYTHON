#Cliff Jorgensen
#class module for vehicle objects

class Vehicle:

    def __init__(self, year, make, color, speed):
        self.year = year
        self.make = make
        self.color = color
        self.speed = speed
        return

    def accelerate(self):
        return self.speed + 5

    def brake(self):
        return  self.speed - 5

    def printItems(self):
        print("Year:", self.year)
        print("Make:", self.make)
        print("Color:", self.color)
        print("Speed:", self.speed)
        return 

    def __str__(self):
        return "\nYear: "+str(self.year)+"\nMake: "+str(self.make)+"\nColor: "+str(self.color)+"\nSpeed: "+str(self.speed)
        
