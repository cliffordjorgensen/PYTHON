#Cliff Jorgensen
#program stores states/capitals in a dictionary
#allows user to add, print, find, and delete entries
#dictionary stores {state:capital} pairs, state = key, capital = value

def menu():
    print("\nMENU: \n\n"
          "(1) Add a new state to the study guide. \n"
          "(2) Print all state/capital pairs stored. \n"
          "(3) How many states are in the study guide. \n"
          "(4) Look for a specific state capital. \n"
          "(5) Delete an entry from the study guide. \n"
          "(6) EXIT.\n")
    
    option = int(input("Enter menu choice: "))
    while option < 1 or option > 6:
        option = int(input("\nInvalid entry. Please enter (1-6) "))
    return option

#allows user to add a new state:capital entry if not already stored
def addCapital():
    state = input("\nPlease enter state: ")
    state = state.capitalize()
    if state in stateDict:
        print("\nSorry, there is already an entry for ", state,"\n")
    else:
        capital = input("\nPlease enter the capital: ")
        capital = capital.capitalize()
        stateDict[state] = capital
    return

#prints all state/capitals entries
def allState():
    if len(stateDict) == 0:
        print("\nNo states in dictionary. ")
    else:
        for state in stateDict:
            print("\nSTATE:", state," CAPITAL:", stateDict[state])

#checks for and deletes entry
def delEntry():
    state = input("\nWhat state do you want to delete? ")
    state = state.capitalize()
    if state in stateDict:
        print("\n", state, " has been removed.\n ")
        del stateDict[state]
    else:
        print(state, "is not in the study guide. ")
    return

#finds specific state and prints the capital
def findState():
    state = input("\nName of state you are looking up: ")
    state = state.capitalize()
    if state in stateDict:
      print("\n ","Capital:", stateDict[state],"\n")
    else:
      print("\nState is not in the study guide. ")
    

#main process
stateDict = {}    #dictionary intially empty
print("\n********** U.S. States and Capitals **********")
choice = menu()

while choice != 6:      #true until user wishes to exit

      if choice == 1:           #add an entry
          addCapital()
      elif choice == 2:         #print all states and capitals.
          allState()
      elif choice == 3:
          print(len(stateDict),"states")    # prints number of states stored
          
      elif choice == 4:         #look for a state
          findState() 
      elif choice == 5:         #delete an entry
          delEntry()
          
      choice = menu()
          

