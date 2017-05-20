responses = []

polling_active = True

while polling_active:
    prompt = "If you could visit one place in the world,"
    prompt += " \nwhere would you go?"
    prompt += "\nType 'done' to display results: "
    
    response = input(prompt)
    
    responses.append(response)
    
    if response == 'done':
        polling_active = False

while 'done' in responses:
    responses.remove('done')

print("\n-----poll results-----")
print(responses)
    
    

