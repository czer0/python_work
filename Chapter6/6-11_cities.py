# Uses a dictionary called cities with the names of three cities as
# keys. Uses a nested dictionary of information about 
# each city which includes the country that the city is in, its 
# approximate population, and a fact about the city. The keys for each 
# city’s dictionary are country, population, and fact 
# Output prints the name of each city and all of the information stored 
# about it.

cities = {
    'halifax': {
        'country': 'canada',
        'population': '403,131',
        'fact': 'located in nova scotia',
            },
    'toronto': {
        'country': 'canada',
        'population': '2810000',
        'fact': 'located in ontario',
            },
    'vancouver': {
        'country': 'canada',
        'population': '2,463,431',
        'fact': 'located in british columbia',
            },
        }

for city, info in cities.items():
    country = info['country'] 
    pop = info['population']
    fact = info['fact']
    print("\nThe city of " + city.title() + ", " + country.title() + " has " + 
        str(pop) + " living in it as of 2016, and is " + fact + ".")
    
