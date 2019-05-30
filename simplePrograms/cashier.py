#This program accepts an amount of change from the user.
#and outputs the number of quarters, dimes , nickels, and pennies
#which comprise this amount of change.

#get the amount of change
print()
change = int(input("Please enter the amount of change "))
print()
print("The amount being change is ", change)
print()

#calculate the number of quarters
quarters =  change // 25

#calculate the amount left over
change = change % 25

#calculate the number of dimes
dimes = change // 10

#calculate the amount left over
change = change % 10

#calculate the number of nickels
nickels = change // 5

#calculate the number of pennies
pennies = change % 5

print("Results:")
print("quarters = " , quarters)
print("dimes = " , dimes)
print("nickels = " , nickels)
print("pennies = " , pennies)
print()
