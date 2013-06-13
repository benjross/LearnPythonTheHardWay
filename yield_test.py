x = 0
def createGenerator():
	mylist = range(3)
	for i in mylist:
		yield i*i
		yield "break"

g = createGenerator()
for i in g:
	print "i: ", i
	global x
	print "x: ", x
	x += 1
