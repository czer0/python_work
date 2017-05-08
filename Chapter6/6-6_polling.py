favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'hank': 'none',
    'sally': 'none',
    'bill': 'none', 
    }


for name, language in sorted(favorite_languages.items()):
    if language == 'none':
        print(
            name.title() + 
            ", please take our poll."
            )
    else:
        print(
            name.title() + 
            ", thank you for taking our poll." +
            " Your favourite language is " + 
            language.title()
            )
 
