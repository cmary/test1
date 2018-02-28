
def test(fn):
	def test_un():
		print("_1"*20)
		return fn()
	return test_un

def test1(fn):
	def nv():
		print("_2"*30)
		return fn()
	return nv

@test
@test1
def test3():
	print("_3"*20)
	  


rt=test3()
print(rt)
