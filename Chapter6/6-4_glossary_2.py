glossary = {
    'tuple': 'a list of immutable (unchangeing) values in python',
    'string': 'a series of characters',
    'key-value pair': 'a set of values associated with each other',
    'dictionary': 'in Python is a collection of key-value pairs',   
    'boolean values': 'are either true or false',
    'list': 'is a collection of items in a particular order',
    'del': 'in python is used to delete a key-pair value',
    'sorted()': 'tells Python to list all keys in the dictionary' 
        ' and sort that list in order',
    'set': 'is similar to a list except that each item in the' 
        ' set must be unique',
    }

for word, meaning in glossary.items():
    print(word.title() + "\n" + "\t" + meaning)
