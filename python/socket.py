# import time
# start_time=time.time()
# for a in range(0,1000):
# 	for b in range(0,1000):
# 		for c in range(0,1000):
# 			if a+b+c == 1000 and a**2+b**2==c**2:
# 				print(a,b,c)
# end_time=time.time()
# print("time:%d" %(end_time-start_time))
# print("finlish")

import time
start_time=time.time()
for a in range(0,1000):
	for b in range(0,1000):
		c=1000-a-b
		if a**2+b**2==c**2:
			print(a,b,c)
end_time=time.time()
print("time:%d" %(end_time-start_time))
print("finlish")