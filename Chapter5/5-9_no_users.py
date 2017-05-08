#~ Added an if test to 5-8_hello_admin.py to make sure the list of users is
#~ not empty

#~ usernames = [] ## for testing
usernames = ['admin', 'hank', 'jenny', 'bob', 'alice', 'ellen']
user = ['admin']

if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello " + user.title() + ", would you like to see a status report?")
        else:    
            print("Hello " + user.title() + ", thank you for logging in again") 
else:
    print("We need to fnd some users!")
