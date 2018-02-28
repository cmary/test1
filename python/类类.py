
def function():
	a=0
	b=1
	for x in range(10):
		temp = yield b 
		print (temp)
		a,b=b,a+b


# def test1():
# 	while True:
# 		print("----1-----")
# 		yield None
# def test2():
# 	while True:
# 		print("----2-----")
# 		yield None
# t1=test1()
# t2=test2()
# while True:
# 	t1.__next__()
# 	t2.__next__()
