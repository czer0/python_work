#~ dictionary containing three major rivers and the country
#~ each river runs through
rivers = {
    'nile': 'egypt',
    'st. Lawrence': 'canada',
    'mississippi': 'the united states of america',
    }   

#~ loop to print a sentence about each river
for river, country in rivers.items():
    print("The " 
        + river.title() + 
        " runs through " 
        + country.title()
        ) 

print("\n")

#~ loop to print the name of each river included in the dictionary
for river in rivers.keys():
    print(river)

#~ loop to print the name of each country included in the dictionary  
for country in rivers.values():
    print(country)
