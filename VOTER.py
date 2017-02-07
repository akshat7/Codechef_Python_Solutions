d = {}
l = []
final = set()
count = 0
n1, n2, n3 = map(int, raw_input().split())

for _ in range(n1+n2+n3):
	num = input()
	if num in l:
		final.add(num)
	else:
		l.append(num)
# for item in d:
# 	if d[item] > 1:
# 		final.append(item)
# 		count += 1

# print sorted(final)
# print final
print len(final)
for item in sorted(final):
	print item