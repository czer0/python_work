# Modifies program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. 
# prints each person’s name along with their favorite numbers



fav_numbers = {
    'ted': [str(5), str(6)],
    'alice': [str(7), str(8)],
    'jackson': [str(250), str(251)],
    'jenny': [str(12), str(13)],
    }


for names, numbers in fav_numbers.items():
    name = names
    print("\n" + name.title() + "'s favorite numbers are :")
    for number in numbers:
        print ("\t" + (number))

