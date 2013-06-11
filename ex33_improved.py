def loop(end, inc = 1):
	i = 0
	numbers = []

	while i < end:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + inc
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	return numbers;

numbers = loop(6)

print "The numbers: "

for num in numbers:
	print num

numbers = loop(6, 2)

print "The numbers: "

for num in numbers:
	print num
