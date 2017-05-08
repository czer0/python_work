# Clinton Mackinnon 4/13/2017
# Demonstrates the various methods for striping whitespace

name = " dick\t butt\n "

name_left = " dick\t butt\n "
name_left = name.lstrip()

name_right = " dick\t butt\n "
name_right = name.rstrip()

name_both = " dick\t butt\n "
name_both = name.strip()

print(name + name_left + name_right + name_both)
