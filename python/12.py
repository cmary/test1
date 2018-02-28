import gc
import sys
class Test(object):
	"""docstring for Test"""
	def __init__(self, func):
		print("----初始化---")
		print("func name is %s"%func.__name__)
		self.__func=func
	def __call__(self):
		print("---装饰器中的功能---")
		self.__func()

@Test
def test1():
	print("---test1------")

print(gc.collect())
gc.enable()
print(gc.get_count())

print(gc.get_threshold())


a=12345645678
b=a
print(sys.getrefcount(a))

test1()