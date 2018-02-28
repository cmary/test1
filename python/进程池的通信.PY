from multiprocessing import Pool,Process,Manager
from multiprocessing import Queue
import time

def write(q):
	for value in ['a','b','c','d']:
		time.sleep(1)
		print("put %s to queue "%value)
		q.put(value)
		

def read(q):
	while True:
		if not q.empty():
			value=q.get(True)
			print("get %s from queue"%value)
			time.sleep(1)
		else:
			break

if __name__ == '__main__':
	q=Manager().Queue()
	po=Pool()
	# pw=Process(target=write,args=(q,))
	# pr=Process(target=read,args=(q,))
	# pw.start()
	# pw.join()
	# pr.start()
	# pr.join()
	po.apply(write,(q,))
	po.apply(read,(q,))
	po.close()
	po.join()
	print("-------over------")


