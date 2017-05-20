prompt = "\nPlease enter your age for ticket priceing."
prompt += "\nEnter age: "

active = True
while active:

    age = input(prompt)
    
    if age == 'quit':
        active = False
    elif int(age) <= 3:
        print("\n Age 3 or younger" 
            + ", your ticket is free ")
    elif int(age) > 3 and int(age) <= 12:
        print("\n You are " + str(age) + 
            " which is between the age of 4 and 12 " + 
            ", your ticket is 10$ ") 
    elif int(age) > 12:
        print("\n You are older than 12" + 
        ", your ticket is 15$ ") 
    
