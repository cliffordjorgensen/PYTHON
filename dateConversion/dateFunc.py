#Cliff Jorgensen
#functions for Date conversion program

def convertMonth(mon):  #changes month to upper case 
    mon = mon.upper()    
    if mon == "JAN":        #changes month to number
        return"01"
    elif mon == "FEB":
        return "02"
    elif mon == "MAR":
        return "03"
    elif mon == "APR":
        return "04"
    elif mon == "MAY":
        return "05"
    elif mon == "JUNE":
        return "06"
    elif mon == "JULY":
        return "07"
    elif mon == "AUG":
        return "08"
    elif mon == "SEPT":
        return "09"
    elif mon == "OCT":
        return "10"
    elif mon == "NOV":
        return "11"
    elif mon == "DEC":
        return "12"
    elif mon == "01":       #changes number to month
        return "JAN"
    elif mon == "02":
        return "FEB"
    elif mon == "03":
        return "MAR"
    elif mon == "04":
        return "APR"
    elif mon == "05":
        return "MAY"
    elif mon == "06":
        return "JUNE"
    elif mon == "07":
        return "JULY"
    elif mon == "08":
        return "AUG"
    elif mon == "09":
        return "SEPT"
    elif mon == "10":
        return "OCT"
    elif mon == "11":
        return "NOV"
    elif mon == "12":
        return "DEC"
    else:
        mon = "00"       #prints error message if month entry is invalid
        print("\n *Unknown Month* (check spelling)")
    return mon

def twoDigitDay(dayNum): #concatenates with 0 if only 1 digit
    if len(dayNum) != 2:
        dayNum = "0" + dayNum
    return dayNum

def format(date):
    date = date.strip()     #remove leading or trailing blanks
    while (date.find(" ")!= -1):   #while there are blanks
        date = date.replace(" ","")
    while (date.find(" -") != -1):      #while there is a blank before dash
            date.replace(" -", "-")
    return date
