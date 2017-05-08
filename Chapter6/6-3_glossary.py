glossary = {
    'tuple': 'a list of immutable (unchangeing) values in python',
    'string': 'a series of characters',
    'key-value pair': 'a set of values associated with each other',
    'dictionary': 'in Python is a collection of key-value pairs',   
    'boolean values': 'are either true or false',
    'list': 'is a collection of items in a particular order'
    }

print("Tuple:\n\t" + 
    glossary['tuple'] + 
    "."  
    )
print("\nString:\n\t" +
    glossary['string'] +
    "."
    )
print("\nKey-value pair:\n\t" +
    glossary['key-value pair'] +
    "."
    )
print("\nDictionary:\n\t" +
    glossary['dictionary'] +
    "."
    )
print("\nBoolean values:\n\t" +
    glossary['boolean values'] +
    "."
    )
print("\nList:\n\t" +
    glossary['list'] +
    "."
    )
    
for word, meaning in glossary.items:
    print(word.title + "\n" + meaning)
