#Cliff Jorgensen

#this program allows the user to perform a math calculation
#the user will choose the operation(+,*,-)
#the user will provide the operands

#main process

def greeting():                  # function welcomes the user
    print('Welcome to the Math Calculator\n')
    return 
def menu():                       #present user with operation choices
    print("\nValid Operations are:  * + - ")
    return
def add(num1, num2):
    total = num1 + num2
    print("\nSum is ", total)
    return
def subtract(num1, num2):
    total = num1 - num2
    print("\nSubtraction is ", total)
    return
def multiply(num1, num2):
    total = num1 * num2
    print("\nProduct is ", total)
def divide(num1, num2):
    total = num1//num2
    print("\nProduct is ", total)


operation = input("Enter your choice of operation (Valid Operations are:  *  +  -  / )")
# loop only executes if input is invalid
while operation != '*' and operation != '+' and operation != '-'and operation != '/':
    print("Invalid operation")
    menu()
    operation = input("Enter your choice of operation ")

op1 = int(input("\nenter the first operand "))           
op2 = int(input("\nenter the second operand "))

if operation == '+':
    add(op1, op2)
elif operation == '*':
    multiply(op1, op2)
elif operation == '-':
    subtract(op1, op2)
else:
    divide(op1, op2)


    

