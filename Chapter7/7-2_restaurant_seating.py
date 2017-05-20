seating = input("Number of dinner guests: ")
seating = int(seating)



if seating >= 8:
    print("I am sorry but will need to wait for a table.")
else:
    print("I have a table that just opened for a party of " + 
        str(seating))
