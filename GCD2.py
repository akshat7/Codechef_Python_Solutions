def gcd(a, b):
	if (b==0):
		return a
	else:
		return gcd(b,a%b)

t = input()
for _ in range(t):
	a, b = map(int, raw_input().split())
	print gcd(a, b)