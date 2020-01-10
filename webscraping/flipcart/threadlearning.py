import threading
import time



def sleeper(sec,name):
	print("my name is {} and i am going to sleep for 5 sec ".format(name))
	time.sleep(sec)
	print("I,{} woke up".format(name))

t=threading.Thread(target=sleeper,name="thread1",args=(5,"thread1"))
start=time.time()
t.start()
t.join()
end=time.time()
print("Time taken {}".format(end-start))
print("hellow")

thread_list=[]
start=time.time()
for thread in range(2,5):
	t=threading.Thread(target=sleeper,name="thread{}".format(thread),args=(5,"thread{}".format(thread)))
	thread_list.append(t)
	t.start()
print("hellow")
for wait_until in thread_list:
	wait_until.join()
end=time.time()
print("Time taken{}".format(end-start))



