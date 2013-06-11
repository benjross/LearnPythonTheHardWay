c = 7

def test_global():
	global c
	c += 3

print "Before: ", c
test_global()
print "After: ", c

def test_bad_global():
	c += 3

#print "Before bad: ", c
#test_bad_global()
#print "After bad: ", c

# made it to "with"
