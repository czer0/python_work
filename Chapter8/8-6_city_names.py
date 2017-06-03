def city_country(city_name, city_country):
    """Displays city name and country."""
    place_formatted = '"' + city_name + ', ' + city_country + '"'
    return place_formatted.title()
    
place = city_country('halifax', 'canada')
print(place)
