#Cliff Jorgensen
#program allows user to convert date formats(Buisness and ISO 8601)
#handles common user errors

import dateFunc     #functions module

print("****** DATE CONVERTER ******\n")
print("1. Convert date from buisness format to ISO 8601 format.")
print("2. Convert date from ISO 8601 format to buisness format.\n")
menu = input("Select Date coversion method. ")

while menu != "q":            #re-prompts user until 'q' is entered
    
    if menu == '1':             # converts from buisness to ISO
        origDate = input("\nEnter a date in business format (DD-MMMM-YYYY):  ")
        origDate = dateFunc.format(origDate)        #formats date
        firstDash = origDate.find("-")               #get index of first dash
        day = origDate[0:firstDash]   
        secondDash = origDate.rfind("-")             #get index of second dash
        month = origDate[firstDash+1:secondDash]
        year = origDate[secondDash+1:]
        month = dateFunc.convertMonth(month)         #change month to number
        day = dateFunc.twoDigitDay(day)              #check day has two digits
        datePiece = [year, month, day]
        iso_Date = '-'.join(datePiece)               #join date with dashes
        print('\nISO 8601 format = ', iso_Date,'\n')

      
    elif menu == '2':                        #converts from ISO to buisness
        origDate = input("\nEnter a date in ISO 8601 format (YYYY-MM-DD):  ")
        origDate = dateFunc.format(origDate)          
        firstDash = origDate.find("-")     
        year = origDate[0:firstDash]
        secondDash = origDate.rfind("-")
        month = origDate[firstDash+1:secondDash]
        day = origDate[secondDash+1:]
        month = dateFunc.convertMonth(dateFunc.twoDigitDay(month)) #check month has 2 digits
        day = dateFunc.twoDigitDay(day)      
        datePiece = [day, month, year]
        buisness_Date = '-'.join(datePiece) 
        print('\nBuisness format = ', buisness_Date,'\n')
        
    menu = input("Select Date coversion method.('q' to exit) ") 

