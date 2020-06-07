# Python strings enable annotations placed before the opening quote: r for raw strings and
# u for Unicode strings.These designators are used both when writing code and displaying
# the value of strings in the interpreter.

mystring = u'This is Unicode!'
print(mystring)
print(str(mystring))

# The “raw” designator tells the interpreter not to transform any special characters inside
# the string. For example, the special string character \n typically stands for a newline, but
# there can be times where you don’t want such a transformation, such as in a DOS filename:
# filename = r'C:\temp\newfolder\robots.txt'.
# Another use-case for raw strings is regular expressions, due to their heavy use of otherwise
# special characters such as the backslash (\). In the regular expressions section, we
# feature a raw string regular expression, r'\w+@\w+\.\w+', which is easier to read than the
# normal (and thus escaped) string, '\\w+@\\w+\\.\\w+'.