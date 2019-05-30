#Cliff Jorgensen
'''This program prompts user for their height, weight, age.
calculates the calories needed to maintain current weight
calculates the time required to burn a specified number of calories'''


def main():
    start = input("Start program? y/n  ")       #prompts user to start program
    if start == "y":
        print("\n******CALORIE COUNTER******")  
    else:
        print("\n***Goodbye***\n")              #exits program 
        exit(main(exit(main)))
    
    while start == "y":         #loop that prompts user for height/weight/age
        
        #variables to hold user input
        user_height = int(input("\nplease enter HEIGHT (inches): "))
        user_weight = int(input("please enter WEIGHT (lbs): "))
        user_age = int(input("please enter AGE: "))
        
        #calculate and print calories required to maintain weight
        print("\nCalories needed to maintain current weight = ", end = ' ')
        print("%.3f"% calories.standardCalBurn(user_weight, user_height, user_age))
        
        #prompt user for number of calories to burn
        cal_burned = int(input("\nHow many calories would you like to burn? "))
        
        #print menu options 
        print("\n1. Minutes of running to burn %d calories. "% cal_burned)
        print("2. Minutes of jogging to burn %d calories. "% cal_burned)                
        print("3. Minutes of walking to burn %d calories. "% cal_burned)

        #prompt user for menu selection
        menu = int(input("\nEnter menu choice. (1-3) or 0 to restart "))

        while menu == 1 or 2 or 3:  #loop executes 

    #if branch checks user selection and implements calories.py module where true
            if menu == 1:
                print("%.2f" % calories.timeRequiredRun(cal_burned, user_weight))
                
            elif menu == 2:
                print("%.2f" % calories.timeRequiredJog(cal_burned, user_weight))
                
            elif menu == 3:
                print("%.2f" % calories.timeRequiredWalk(cal_burned, user_weight))
                
            elif menu == 0:
                end_prgm = input("\nWould you like to restart? y/n  ")
                if end_prgm == "y":
                    main()
            #reprompt user if menu selection is out of range        
            menu = int(input("\nEnter menu choice.(1-3) or 0 to restart "))
           
    return

import calories     #imports calories function module

main()      #Calls main program. 

