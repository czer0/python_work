#~ list of toppings a customer has requested and 
#~ using a loop to announce each topping as it’s
#~ added to the pizza:

#~ requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

#~ for requested_topping in requested_toppings:
    #~ if requested_topping == 'green peppers':
        #~ print("Sorry, we are out of green peppers right now.")
    #~ else:
        #~ print("Adding " + requested_topping + ".")
    
#~ print("\nFinished making your pizza")


#~ checking that a list is not empty

#~ requested_toppings = []




#~ using multiple lists

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")  
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")
