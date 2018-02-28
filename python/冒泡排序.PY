
def paixu(list):
	n=len(list)
	for j in range(n-1):
		for i in range(n-1-j):
			if list[i]>list[i+1]:
				list[i],list[i+1]=list[i+1],list[i]

if __name__ == '__main__':
	a=[1,3,2,8,5,6,7,9,0]
	print(a)
	paixu(a)
	print(a)