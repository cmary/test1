def kuaisu(alist,first,last):
	if first >= last:
		return
  
	mid=alist[first]
	low=first
	high=last
	while low < high:
		while low < high and alist[high] >=mid:
			high -= 1
		alist[low] = alist[high]
		while low < high and alist[low] < mid:
			low += 1
		alist[high]=alist[low]
	alist[low]=mid

	kuaisu(alist,first,low-1)
	kuaisu(alist,low+1,last)

if __name__ == '__main__':
	li=[11,22,33,22,1,3,4,8,9,54,676]
	print(li)
	kuaisu(li,0,len(li)-1)
	print(li)