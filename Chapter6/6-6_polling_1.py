
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

poll = [
    'phil',
    'hank',
    'sally',
    'bill', 
    ]
    
    
for name in favorite_languages.keys():
    if name in poll:
        print(
        name.title() + 
        ", thank you for taking our poll"
        )
    else:
        print(
        name.title() + 
        ", please take our poll."
        )
