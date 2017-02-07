def cycle(l, i):
    if i not in visited:
        final.append(i)
        visited.add(i)
        cycle(l, l[i-1])
    

n = input()
a = map(int, raw_input().split())
# a = [2, 4, 5, 1, 7, 6, 3, 8]
visited = set()
total = []
for i in range(n):
    final = []
    if i+1 not in visited:
        cycle(a, i+1)
    if len(final) != 0:
        total.append(final)
        
print len(total)
for item in total:
    for i in item:
        print i,
    print item[0]
