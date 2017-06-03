def describe_city(city_name, city_country = 'canada'):
    """Displays city name and country."""
    print("\n" + city_name.title() + " is located in " + city_country.title()) 

describe_city('reykjavik', 'iceland')
describe_city('halifax')
describe_city('toronto')
