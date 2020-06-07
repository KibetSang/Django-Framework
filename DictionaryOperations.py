# Dictionaries are Python’s sole mapping type.They are mutable, unordered, resizable mappings
# of keys to values, and are sometimes alternatively called hash tables (“hashes”) or
# associative arrays.The syntax is otherwise similar to sequences, but instead of an index to
# access the value, you use a key, and rather than square brackets (lists) or parentheses
# (tuples), they are defined with curly braces ({ }).
# Dictionaries are by far the most important data structure in the language.They are the
# secret sauce for most of Python’s objects. Regardless of what types of objects they are or
# how you use them, there’s a high likelihood that under the covers, there’s a dictionary
# managing that object’s attributes.Without further ado, let’s take a look at what they are
# and what they can do.

book={'Name': 'CSS Programming', 'Year': 2010}
print(book)
print(book.get('Name','Year'=='2010'))


# So what did we do? Here’s a summary:
# 1. Create initial dictionary with a string and an integer; both keys are strings.
# 2. Dump out the object.
# 3. Check to see if the dictionary has a particular key (twice; once yes, once no).
# 4. Use the get method to fetch a value using the given key (gets default here).
# 5. Assign a new key-value pair.
# 6. Perform the same get call but with success this time.
# 7. Iterate through the dictionary and display each key-value pair.
