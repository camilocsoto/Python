from collections import deque
from queue import LifoQueue

class Stack:
    def __init__(self, limit=0):
        self.stack = deque([])
        self.limit = limit
    
    def push(self, item):
        if self.limit == len(self.stack):
            print("stack overflow")
        else:
            self.stack.append(item)
    
    def pop(self):
        return self.stack.pop() if self.stack else None
    
    def peek(self):
        return self.stack[-1] if self.stack else None
    
    def __str__(self):
        return str(list(self.stack))

def Lifoqueue():
    stack = LifoQueue()
    stack.put("R2D2")
    stack.put("IG11")
    stack.get() #erase
    print(f"Stack after pushing: {list(stack.queue)}")
    print(f"Top element: {stack.get()}")
    print(f"Stack after popping: {list(stack.queue)}")

if __name__ == "__main__":
    stack = Stack()
    stack.push("C3PO")
    stack.push("R2D2")
    stack.push("IG11")
    stack.peek()
    print(f"Stack after pushing: {stack}")
    