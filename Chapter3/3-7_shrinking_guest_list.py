# removal of guests from list


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


print("\nOur larger table will not arrive on time. This means we will not have space available for more than two guests.\n")


remove_guest = guests.pop()
print(remove_guest.title() + " I am sorry to inform you that your invitaion has been recinded.")
remove_guest = guests.pop()
print(remove_guest.title() + " I am sorry to inform you that your invitaion has been recinded.")

remove_guest = guests.pop()
print(remove_guest.title() + " I am sorry to inform you that your invitaion has been recinded.")

remove_guest = guests.pop()
print(remove_guest.title() + " I am sorry to inform you that your invitaion has been recinded.")

remove_guest = guests.pop()
print(remove_guest.title() + " I am sorry to inform you that your invitaion has been recinded.")

remove_guest = guests.pop()
print(remove_guest.title() + " I am sorry to inform you that your invitaion has been recinded.")

print("\n" + guests[0].title() + " I am pleased to inform you that your invitaion is still in place.")
print(guests[1].title() + " I am pleased to inform you that your invitaion is still in place.\n")

del(guests[1])
del(guests[0])

print(guests)

