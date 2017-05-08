pets = {
    'sammy': {
        'animal type': 'hamster',
        'owner': 'jackson'
        },
    'lulu': {
        'animal type': 'cat',
        'owner': 'andy'
        },
    'eden': {
        'animal type': 'dog',
        'owner': 'chris'    
        },
    'doodle': {
        'animal type': 'cat',
        'owner': 'julia'
        },
      }  
for petname, petinfo in sorted(pets.items()):
        print("\nPet name: " + petname.title())
        animal = petinfo['animal type']
        owner = petinfo['owner']
        
        print("Pet type: " + animal.title())
        print("Pet owner: " + owner.title())
        
