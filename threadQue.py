import thread
import Queue
import time

import common
import util

q = Queue.Queue()

def work(s):
	gp = common.Grouppackage()
	while True:
		if q.empty():
			continue
		data = q.get()
		print 'work:', data
		gp.parsepackage(data)

def work0(s):
	while True:
		if q.empty():
			continue
		data = q.get()
		print 'work:', data


if __name__ == '__main__':
	thread.start_new_thread(work0, (None,))
	for i in range(0, 10):
		q.put(i)
	time.sleep(2)
