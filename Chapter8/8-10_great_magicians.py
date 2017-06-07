# prints a list of magician names

def make_great(magician_names):
    """Prints a list of magician names with "the Great" added"""
    while magician_names:
        names = magician_names.pop()
        print ("the Great " + names.title())
        
def show_magicians(magician_names):
    """Prints a list of magician names"""
    for names in magician_names:
        mn = names.title()
        print(mn)
            
magician_names = ['mandrake', 'merlin', 'elminster', 'rincewind']


show_magicians(magician_names)
make_great(magician_names)

