from threading import Thread
import time
def test():
	print("-------test-------多线程")
	time.sleep(1)
def test1():
	print("-------test1-------多线程")
	time.sleep(1)
def test2():
	print("-------test2-------多线程")
	time.sleep(1)
for x in range(1,5):
	t=Thread(target=test)
	a=Thread(target=test1)
	b=Thread(target=test2)
	t.start()
	a.start()
	b.start()