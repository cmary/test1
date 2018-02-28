from multiprocessing import Process
import time

j=0
def test():
	i=0
	while i<10:
	 	print("-----test-------")
	 	time.sleep(0.1)
	 	i=i+1

if __name__ == '__main__':
	p = Process(target = test)
	p.start()
	while j<10:
		print("----mian----")
		time.sleep(1)
		j+=1


