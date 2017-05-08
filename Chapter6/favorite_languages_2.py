favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#~ the code below tells Python to loop through each key-value 
#~ pair in the dictionary. As it works through each pair the key 
#~ is stored in the variable 'name', and the value is stored in 
#~ the variable 'language'.

for name, language in favorite_languages.items():
    print(name.title() + 
        "'s favorite language is " +
        language.title() + ".")

#~ the code below tells Python to pull all the keys from the dictionary
#~ favorite_languages and store them one at a time in the variable name

for name in favorite_languages.values():
    print(name.title())
