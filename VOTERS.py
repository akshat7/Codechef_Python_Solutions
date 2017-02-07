from sys import stdin
_ = raw_input()
final = []
b = map(int, stdin.readlines())
b.sort()
p = -1
for item in b:
	if item == p:
		final.append(item)
		p = -1
	else:
		p = item
print len(final)
for item in final:
	print item