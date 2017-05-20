responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("If you could visit one place in the world,"
        + " \nwhere would you go? ")
     
    responses[name] = response
    
    end_poll = input("Type 'done' to display poll results." 
        + " press 'enter' key to continue: ")
    if end_poll == 'done':
        polling_active = False

print("\n-----poll results-----")
for name, response in responses.items():
    print(name + " would like to vist " + response + ".")
    
    

