count = 0
t = input()
for _ in range(t):
    x1, y1, x2, y2, x3, y3 = map(int, raw_input().split())
    d12 = (x1-x2)**2 + (y1-y2)**2
    d23 = (x3-x2)**2 + (y3-y2)**2
    d13 = (x1-x3)**2 + (y1-y3)**2
    if (d12 == d13+d23) or (d23 == d13+d12) or (d13 == d12+d23):
        count += 1
print count