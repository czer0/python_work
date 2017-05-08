favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#~ You can use the sorted() function to get a copy of
#~ the keys in order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")


print("\n")

#~ The for statement here pulls each value from the dictionary 
#~ and stores it in the variable language. When these values are 
#~ printed, we get a list of all chosen languages
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("\n")

#~ The set() command is used here to pull out the unique languages 
#~ in favorite_languages.values(). The result is a nonrepetitive 
#~ list of languages that have been mentioned
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


