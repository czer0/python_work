# prints a list of magician names

def make_great(magician_names, great_names):
    """
    Prints a list of magician names with "the Great" added.
    Moves the new magician name to the great_names list.
    """
    while magician_names:
        names = magician_names.pop()
        print ("the Great " + names.title())
        great_names.append(names)
        
def show_magicians(magician_names):
    """Prints a list of magician names"""
    for names in magician_names:
        mn = names.title()
        print(mn)
            
magician_names = ['mandrake', 'merlin', 'elminster', 'rincewind']
great_names = []

show_magicians(magician_names)
make_great(magician_names, great_names)
show_magicians(great_names)



