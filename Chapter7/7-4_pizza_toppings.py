
prompt = "\nWhat would you like on your pizza? "
prompt += "\nType 'quit' to exit: "

#~ message = ""
#~ while message != 'quit':
    #~ message = input(prompt)
    #~ print("I will add " + message + " to your pizza.")
        
    #~ if message == 'quit':
        #~ print(message)

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print("\nI will add " + message + " to your pizza.")
