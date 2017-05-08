#~ simulation of how a website ensures unique usernames

current_users = ['admin', 'hank', 'jenny', 'bob', 'alice', 'ellen']
new_users = ['zim', 'ellen', 'hank', 'jackson']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("The username " + new_user + " is in use")
    else:
        print("the username " + new_user + " is available") 
