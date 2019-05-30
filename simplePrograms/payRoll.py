#Cliff Jorgensen

#program calculates a weekly paycheck based on hours worked.

print()
#variables to define paycheck factors
income_tax = 0.14
social_sec = 0.06
union_dues = 10.0
pay_rate = 20.00
gross_pay = 0.0
net_pay = 0.0
over_t = 0.0

#prompts user for hours worked
print("Enter 0 to quit \n") 
hrs_worked = float(input("Enter hours worked: "))
print("\nCurrent pay rate = %s per hour\n" % pay_rate)

#loop remains active until 0 is entered
while hrs_worked > 0:
    
#calculates earnings for any entry up to 40 hours
    if  hrs_worked <= 40:
        print("Now processing %s hours worked. \n" % hrs_worked)
        gross_pay = pay_rate * hrs_worked
        income_tax = pay_rate * hrs_worked * income_tax
        social_sec = pay_rate * hrs_worked * social_sec
        net_pay = gross_pay - (income_tax + social_sec + union_dues)
        over_t = 0
        
#prints calculated paycheck variables 
        print("Gross Pay: $%.2f \n" % gross_pay)
        print("Over-Time: $%.2f \n" % over_t)
        print("Income Tax withholding: $%.2f \n" % income_tax)
        print("Social Security withholding: $%.2f \n" % social_sec)
        print("Union Dues withhoding: $%.2f \n" % union_dues)
        print("Net Pay: $%.2f \n\n" % net_pay)
        print("Enter 0 to quit \n\n")
        hrs_worked = float(input("Enter hours worked: "))
        print(pay_rate)
#reset variables for another entry
        income_tax = 0.14
        social_sec = 0.06
        union_dues = 10.0
        pay_rate = 16.78
        gross_pay = 0.0
        net_pay = 0.0
        over_t = 0.0
        print()
        
#calculates earnings for any entry over 40 hours, calculates overtime.        
    elif hrs_worked > 40:
        print("\nNow processing %s hours worked.\n" % hrs_worked)
        over_t = (hrs_worked - 40)*(pay_rate * 1.5)
        gross_pay = pay_rate * 40
        gross_total = gross_pay + over_t
        income_tax = gross_total * income_tax
        social_sec = gross_total * social_sec
        net_pay = gross_total - (income_tax + social_sec + union_dues)
        print("pay rate: ", pay_rate,"/ hour\n")
        
#prints the calculated paycheck variables
        print("Gross Pay: $%.2f \n" % gross_pay)
        print(hrs_worked - 40,"Hours", "Over-Time: $%.2f \n" % over_t)
        print("Gross Pay Total: $%.2f \n" % gross_total)
        print("Income Tax withholding: $%.2f \n" % income_tax)
        print("Social Security withholding: $%.2f \n" % social_sec)
        print("Union Dues withhoding: $%.2f \n" % union_dues)
        print("Net Pay: $%.2f \n\n" % net_pay)
        print("Enter 0 to quit \n\n")
        hrs_worked = float(input("Enter hours worked: "))
        
#reset variables for another entry
        income_tax = 0.14
        social_sec = 0.06
        union_dues = 10.00
        pay_rate = 16.78
        gross_pay = 0.00
        net_pay = 0.0
        over_t = 0.0
        print()
        
#prints error message if input is zero or negative    
print("Error")

