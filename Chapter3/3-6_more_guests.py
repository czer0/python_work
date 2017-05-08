# invitation for three more to dinner

guests=['tom', 'dick', 'harry', 'frank']
print(guests[0].title() + " please come to my party.")
print(guests[1].title() + " please come to my party.")
print(guests[2].title() + " please come to my party.")
print(guests[3].title() + " please come to my party.")

guests.insert(4, 'bob')
guests.insert(0, 'sally')
guests.insert(3, 'hank')
guests.append('jim')

print("\n" + guests[0].title() + " please come to my party.")
print(guests[1].title() + " please come to my party.")
print(guests[2].title() + " please come to my party.")
print(guests[3].title() + " please come to my party.")
print(guests[4].title() + " please come to my party.")
print(guests[5].title() + " please come to my party.")

print("\nWe have found a larger dinner table.")
