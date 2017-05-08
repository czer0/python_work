#~ list of fruits, and a series of independent if 
#~ statements that check for certain fruits in the list

favorite_fruits = ['bananas', 'pears', 'peaches']

fruit = 'pears'
if fruit in favorite_fruits:
    print("You really like " + fruit.title() + "!")


fruit = 'plums'
if fruit not in favorite_fruits:
    print ("I wish we had some " + fruit.title())


fruit = "ham"
if fruit == 'apples':
    print("I like" + fruit.title())
elif fruit not in favorite_fruits:
    print("What the hell! " + fruit.title() + " is not in my list of fruit")

    
fruit = 'kiwi'
if fruit in favorite_fruits:
    print("This " + fruit.title() + " is in my list.")
else:
    print("This " + fruit.title() + " is not in my list")

if 'bananas' in favorite_fruits:
    print("I like Bananas!")
if 'pears' in favorite_fruits:
    print("I like Pears!")
if 'peaches' in favorite_fruits:
    print("I like Peaches!")
