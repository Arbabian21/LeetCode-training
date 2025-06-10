from multiprocessing import Queue

customQueue = Queue(maxsize=3)
customQueue.put(10)
customQueue.put(20)
customQueue.put(30)
print(customQueue.get())