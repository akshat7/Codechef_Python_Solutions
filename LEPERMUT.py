def local_inversion(n, A):
	count = 0
	for i in range(n-1):
		if A[i] > A[i+1]:
			count += 1
	return count

def inversion(n, A, loc_inv):
	count = 0
	for i in range(n-1):
		for j in range(i+1, n):
			if A[i] > A[j]:
				count += 1
				if count > loc_inv:
					return False
	return True

t = input()
for _ in range(t):
	n = input()
	A = map(int, raw_input().split())
	loc_inv = local_inversion(n, A)
	inv_bool = inversion(n, A, loc_inv)
	if inv_bool == True:
		print "YES"

	else:
		print "NO"