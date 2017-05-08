#~ an if-elif-else chain that determines a person’s stage of life. 

#~ progression from lowest age to highest
#~ age = 65

#~ if age < 2:
    #~ print("This is a baby")
#~ elif age >= 2 and age < 4: 
    #~ print("This is a toddler")
#~ elif age >= 4 and age < 13:
    #~ print("this is a kid")
#~ elif age >= 13 and age < 20:
    #~ print("this is a teenager")     
#~ elif age >= 20 and age < 65:
    #~ print("this is an adult")
#~ elif age >= 65:
    #~ print("this is an elder")
    

#~ progression from highest age to lowest

age = 65

if age >= 65:
    print("This is an elder")
elif age >= 20 and age < 65: 
    print("This is an adult")
elif age >= 13 and age < 20:
    print("this is a teenager")
elif age >= 4 and age < 13:
    print("this is a kid")     
elif age >= 2 and age < 4:
    print("this is a toddler")
elif age <= 2:
    print("this is a baby")
    
