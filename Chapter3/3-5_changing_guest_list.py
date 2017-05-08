# list, replacing the name of the guest who can’t make it with 
# the name of the new person being inviting

guests=['tom', 'dick', 'harry', 'frank']

print(guests[0].title() + " please come to my party." )
print(guests[1].title() + " please come to my party." )
print(guests[2].title() + " please come to my party." )
print(guests[3].title() + " please come to my party." )

not_attending = 'harry'
guests.remove(not_attending)

guests.insert(0, 'jim')

print("\n" + guests[0].title() + " please come to my party." )
print(guests[1].title() + " please come to my party." )
print(guests[2].title() + " please come to my party." )
print(guests[3].title() + " please come to my party." )
