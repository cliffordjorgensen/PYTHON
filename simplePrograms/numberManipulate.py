#Cliff Jorgensen

# This program prompts the user for a positive number, then gives 4 choices.
# re-prompts user for a menu choice (1-4).
# menu choice determines which function is called.


# main process function 
def main_process():
    
# Function calculates and prints if user input is even/odd.
    def isEven(number):
        if number % 2 == 0:
            return("%d Is even." % number)
        else:
            return ("%d Is odd." % number)
        
# Function prints all even numbers in the range of user input.   
    def printEven(number):
        for i in range(0, number +1):
           if i % 2 == 0:
               print(i)
        return ("Done")
    
# Function prints all numbers from user_input down to 1.
    def countDown(number):
        for i in range(number):
            print(number - i)
        return("Done")
    
# Function prints the number of digits in user input
    def howManyDigits(number):
        digits = str(number)          
        return("There are %s digits. " % len(digits))
    print()
    
# Prompts user for a positive number
    user_input = int(input("Please enter a positive number to begin. "))
    
# Loop that re-prompts user if the value is less than 0.  
    while user_input <= 0:
        user_input = int(input("Please enter a positive number to begin. "))

# Loop prompts user to enter a choice (1-4) or 5 to start over.
    while user_input > 0:
        print()
        print("1. Identify number as even or odd.")
        print("2. Print even values up to the number.")
        print("3. Print all values from number down to 1.")
        print("4. See how many digits are in the number.\n")
        
# menu variable prompts user for desired menu operation.       
        menu = int(input("Enter number of operation (1-4) or enter 5 to start over: "))
        print()

        if menu == 1:
            print(isEven(user_input))

        elif menu == 2:
            print(printEven(user_input))

        elif menu == 3:
            print(countDown(user_input))

        elif menu == 4:
            print(howManyDigits(user_input))
            
# If menu choice is not equal to (1-4) then user is prompted for intial value.
        else:
            user_input = int(input("Please enter a positive number to begin. "))       

# Calls main function
main_process()
