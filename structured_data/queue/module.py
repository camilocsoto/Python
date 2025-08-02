from queue import Queue

q = Queue(maxsize=4)
q.put("C3PO")
q.put("R2D2")
q.put("IG11")
q.put("C1-1OP")
q.put("tre")

print(f"Queue after enqueueing: {list(q.queue)}")
