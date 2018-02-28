def xier(alist):
	'''希尔排序'''
	n=len(alist)
	gap=n//2
	while gap>0:
		for j in range(gap,n):
			i=j
			while i>0:
				if alist[i] < alist[i-gap]:
					alist[i],alist[i-gap]=alist[i-gap],alist[i]
					i-=gap
				else:
					break
		gap //= 2
if __name__ == '__main__':
	li=[11,22,34,2,1,4,55,2,54,12,543,654,43,543]
	print(li)
	xier(li)
	print(li)
	print("finally")