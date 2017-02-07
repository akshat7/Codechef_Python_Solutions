import re

t = input()
for _ in range(t):
	s = raw_input()
	pattern = r'(101)|(010)'
	if re.search(pattern, s):
		print "Good"
	else:
		print "Bad"