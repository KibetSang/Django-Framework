# String Method Description
# count Number of occurrences of substring in string
# find Search for substring [also see index, rfind, rindex]
# join Merge substrings into single delimited string
# replace Search and replace (sub)string
# split Split delimited string into substrings [also see splitlines]
# startswith Does string start with substring [also see endswith]
# strip Remove leading and trailing whitespace [also see rstrip, lstrip]
# title Title-case string [also see capitalize, swapcase]
# upper UPPERCASE string [also see lower]
# isupper Is string all UPPERCASE? [also see islower, and so forth]


s = 'Django is cool' # 1
words = s.split() # 2
print(words)
words=''.join(words) # 3
print(words)
words='::'.join(words) # 4
print(words)
s=''.join(words) # 5
s=s.upper() # 6
print(s)
s.upper().isupper() # 7
s=s.title() # 8
print(s)
s.capitalize() # 9
print(s)
s=s.count('o') # 10
print(s)
s=s.find('go') # 11
s.find('xxx') # 11
s.startswith('Python') # 12
s.replace('Django', 'Python') # 13
