from threading import Thread,Lock
import time
g_num=0
def test1():
	global g_num
	for x in range(10):
		mutex.acquire()
		g_num+=1
		mutex.release()
		print("test1-----g_num=%d"%g_num)
		time.sleep(1)

def test2():
	global g_num
	for x in range(10):
		mutex.acquire()
		g_num+=1
		mutex.release()
		print("test2-----g_num=%d"%g_num)
		time.sleep(1)

mutex=Lock()
p1=Thread(target=test1)
p1.start()

p2=Thread(target=test2)
p2.start()
