# first in first out - last in last out
# enqueue: add an element to the end of the queue
# dequeue: remove the first element from the queue

queue = []
# tail -> head
queue.append("C3PO") 
queue.append("R2D2")
queue.append("IG11")
queue.pop(0)  # dequeue the front

# head <- tail
reversed_queue = []
queue.insert(0, "C3PO") 
queue.insert(0, "R2D2")
queue.insert(0, "IG11")
queue.pop() # dequeue the front
