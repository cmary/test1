from threading import Thread
import threading 
import time
def test1():
	print("------thread name is %s---"%threading.current_thread().name)
	g_num=100
	g_num+=1
	print("-----test1---g_num=%d"%g_num)
	time.sleep(1)
	print("-----test1---g_num=%d"%g_num)

def test2():
	print("------thread name is %s---"%threading.current_thread().name)
	time.sleep(1)
	g_num=100
	print("----test2----g_num=%d"%g_num)

p1=Thread(target=test1)
p1.start()

p2=Thread(target=test2)
p2.start()