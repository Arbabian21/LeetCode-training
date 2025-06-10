import queue

customQueue = queue.Queue(maxsize=3)
print(customQueue.qsize())

customQueue.put(10)
customQueue.put(20)
customQueue.put(30)
print(customQueue.qsize())
print(customQueue.empty()) # is empty   
print(customQueue.full()) # is full
print(customQueue.get())
print(customQueue.qsize())