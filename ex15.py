from sys import argv

script, filename = argv

# txt is a file, not a string
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()

print "Type the filename agian:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
