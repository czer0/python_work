favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    print("\n" +name.title() + " knows " + str(len(languages)) + " language(s).")
    print(name.title() + "'s favorite languages are:")
    for language in languages:
            print("\t" + language.title())
