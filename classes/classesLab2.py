    #Cliff Jorgensen

import runnerClass


#main process

'''person1 = runnerClass.Runner("Sue", 15.5, 8)
person2 = runnerClass.Runner("Roger", 128, 15)
person3 = runnerClass.Runner("Carl", 4, 12)

#person1.printStat()
#person2.printStat()
person3.printStat()

speedPerMin = person3.distancePerMin()
print(person3.name, "runs", speedPerMin, "meters a minute")

print(person3)'''

runnerList = [] 

for i in range (5):                 
    na = input("Enter a name: ")                
    dist = float(input("Enter a distance: "))
    time = float(input("Enter a time: "))

    person = runnerClass.Runner(na,dist,time)
    runnerList.append(person)

for r in runnerList:
    print(r)
    


#find Fastest runner

fastestspeed = runnerList[0].time
fastestname = runnerList[0].name

for r in runnerList:
    if r.time < fastestspeed:
        fastestspeed = r.time
        fastesttime = r.name



    
  
