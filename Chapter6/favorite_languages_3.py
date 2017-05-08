favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#~ creates the list 'friends' that we want to print a message to.
#~ Inside the loop, we print each person’s name
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    #~ check to see whether the name we are working with is in the list 
    #~ 'friends'. If it is, we print a special greeting, including a 
    #~ reference to their language choice
    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is " +
            #~ we use the name of the dictionary and the current value 
            #~ of 'name' as the key. Everyone’s name is printed, but our 
            #~ 'friends' list recieves a special message:
            favorite_languages[name].title() + "!")

#~ using the keys() method to fnd out if a particular person
#~ was polled.
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
