# Makes a dictionary called favorite_places. Uses three
# names as keys in the dictionary, and stores three favorite places
# Loops through the dictionary, and prints each person’s 
# name and their favorite places


favorite_places = {
    'ixnok': ['moon', 'beach', 'woods'],
    'frank': ['serbia', 'italy', 'france'],
    'sally': ['south pole', 'plains of leng', 'ryleh'],
    }

for names, places in favorite_places.items():
    name = names
    print("\n" + name.title() + "'s favorite places are :")
    for place in places:
        print(place.title())
