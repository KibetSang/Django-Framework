# Python features if and else statements. Python’s “else-if ” is actually
# spelled elif, just like in the Bourne family of shell script languages (sh, ksh, and bash).
# It’s so simple in Python we feel a single example conveys to you how they work.
def raw_input(''):
    pass
data = raw_input("Enter 'y' or 'n': ")
if data[0] == 'y':
 print("You typed 'y':")
elif data[0] == 'n':
 print( "You typed 'n'.")
else:
 print('Invalid key entered!')