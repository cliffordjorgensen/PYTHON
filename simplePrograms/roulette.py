#Cliff Jorgensen


#get number from user
pocket_number = int(input("enter pocket number: "))

if pocket_number == 0:
    print("green")
elif pocket_number > 36 or pocket_number < 0:
    print("entry is out of bounds")
    
#odd = red and even = black
elif pocket_number >= 1 and pocket_number <= 10:
        if pocket_number %2 == 0:
            print("black")
        else:
            print("red")
#odd = black and even = red 
elif pocket_number >= 11 and pocket_number <= 18:
        if pocket_number %2 == 0:
            print("red")
        else:
            print("black")
#odd = red and even = black           
elif pocket_number >= 19 and pocket_number <= 28:
        if pocket_number %2 == 0:
            print("black")
        else:
            print("red")
#odd = black and even = red
elif pocket_number >= 29 and pocket_number <= 36:
        if pocket_number %2 == 0:
            print("red")
        else:
            print("black")


