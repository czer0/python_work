people = {
    'cconnors': {
    'first name': 'carolyn',
    'last name': 'connors',
    'age': '38',
    'city': 'halifax',
      },
    'jconnors': {
    'first name': 'jackson',
    'last name': 'connors',
    'age': '7',
    'city': 'halifax',
      },    
    'cmackinnon': {
    'first name': 'clinton',
    'last name': 'mackinnon',
     'age': '41',
     'city': 'halifax',
      },    
        }

for user, info in people.items():
    user = user 
    firstname = info['first name']
    lastname = info['last name']
    age = info['age']
    city = info['city']
    print("Collected infomation for the account " + user + " owned by " + firstname + " " + lastname)
    print("Age:" + age + "\nCity: " + city)
