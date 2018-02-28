class Person(object):
	"""docstring for Person"""
	def __getattribute__(self,obj):
		print("-----tets-=---")
		if obj.startswith("a"):
			return "hahah"
		else:
			return object.__getattribute__(self,obj)
		def test(self):
			print("heiheihei")

t=Person()
print(t.a)
print(t.d)