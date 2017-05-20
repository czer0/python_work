prompt = "\nWhat would you like on your pizza? "
prompt += "\nType 'quit' to exit: "

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        break
    else:
        print("\nI will add " + message + " to your pizza.")
  
