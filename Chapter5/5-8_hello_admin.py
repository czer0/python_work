#~ loop through a list of usernames, and print a greeting to
#~ each user

usernames = ['admin', 'hank', 'jenny', 'bob', 'alice', 'ellen']

for user in usernames:
    if user == "admin":
        print("Hello " + user.title() + ", would you like to see a status report?")
    else:
        print("Hello " + user.title() + ", thank you for logging in again") 


