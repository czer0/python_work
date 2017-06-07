# prints a list of magician names

def print_names(names):
    """Prints a list of magician names"""
    for name in names:
        mn = name.title()
        print(mn)

magician_names = ['mandrake', 'merlin', 'elminster', 'rincewind']
print_names(magician_names)
