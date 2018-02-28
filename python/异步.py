from multiprocessing import Pool
import time
import os

def test():
	print("---进程池中的进程----pid=%d,ppid=%d---" %(os.getpid(),os.getppid()))
	for x in range(3):
		print("-----%d-----" %x)
		time.sleep(1)
	return "haha"

def test2(args):
	print("-----callback---func---pid=%d" %os.getpid())
	print("-----callback----func--args=%s" %args)
	print(args)


def main():
	pool=Pool(2)
	p=pool.apply_async(func=test,callback=test2)
	time.sleep(5)
	print("------主进程------pid=%d" %os.getpid())

if __name__ == '__main__':
	main()