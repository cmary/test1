def charu(alist):
	n=len(alist)
	for j in range(1,n):
		i=j
		while i > 0:
			if alist[i] < alist[i-1]:
				alist[i], alist[i-1] = alist[i-1], alist[i]
				i -= 1
			else:
				break

if __name__ == '__main__':
	li=[22,33,55555,11,23,432,54234,3213,324,11,8,44]
	print(li)
	charu(li)
	print(li)