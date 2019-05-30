#Cliff Jorgensen
#class module for runner program


class Runner:

    def __init__(self,newname, newdistance, newtime):
        self.name = newname
        self.distance = newdistance
        self.time = newtime
        return

    def printStat(self):
        print("Name:", self.name)
        print("Distance:", self.distance)
        print("Time:", self.time)
        return
        
    def distancePerMin(self):           #return meters per minute
        return self.distance/self.time

    def __str__(self):
        return "Name: " + self.name + "\nDistance: " + str(self.distance) + "\nTime: " + str(self.time)

    def __lt__(self, other):
        if self.time < other.time:
            return True
        else:
            return False
        
