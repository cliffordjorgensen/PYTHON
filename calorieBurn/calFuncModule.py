#Cliff Jorgensen
''' This module contains functions that calculate calories burned per minute and
time required to burn a specific number of calories. The function parameters are
collected in the main program and implemented in this module'''

#function returns calories needed to maintain current weight
def standardCalBurn(weight, height, age):       
    weight *= 4.3                           
    height *= 4.7                           
    age *= 4.7
    calories = 655 + weight + height - age
    return calories

#function returns calories burned per minute(running)
def burnedRunning(weight):
    weight *= .095          
    return weight

#function returns calories burned per minute(jogging)
def burnedJogging(weight):
    weight *= .0775         
    return weight

#function returns calories burned per minute(walking)
def burnedWalking(weight):
    weight *= .054          
    return weight

#function returns minutes of running required to burn entered calories 
def timeRequiredRun(calories, weight):
    time = calories / burnedRunning(weight)
    print("Minutes of Running =", end = ' ')
    return time

#function returns minutes of jogging required to burn entered calories 
def timeRequiredJog(calories, weight):
    time = calories / burnedJogging(weight)
    print("Minutes of Jogging =", end = ' ')
    return time

#function returns minutes of walking required to burn entered calories 
def timeRequiredWalk(calories, weight):
    time = calories / burnedWalking(weight)
    print("Minutes of Walking =", end = ' ')
    return time

              
