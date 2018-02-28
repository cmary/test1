


def xuanze(list):
	n=len(list)
	for j in range(n-1):
		min_index=j
		for i in range(j+1,n):
			if list[min_index]>list[i]:
				min_index= i
		list[j],list[min_index]=list[min_index],list[j]

if __name__ == '__main__':
	li=[22,3,444,444,566,11,3,3,5,5,67,876,3223,34]
	print(li)
	xuanze(li)
	print(li)
