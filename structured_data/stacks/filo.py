# first in last out - last in first out
# hanoi tower ; 
from dataclasses import dataclass, field
@dataclass
class Stack:
    stack:list = field(default_factory=list)
    limit: int = 0
    
    def push(self, item):
        if self.limit == len(self.stack):
            print("stack overflow")
        else:
            # add an element to the top of the stack
            return self.stack.append(item)
    
    def pop(self):
        # remove the top element
        return self.stack.pop() if self.stack else None
    
    def peek(self):
        # return the top element without removing it
        print(self.stack[-1] if self.stack else None)
    
    def __str__(self):
        return str(self.stack)

if __name__ == "__main__":
    stack = Stack()
    stack.push("C3PO")
    stack.push("R2D2")
    stack.push("IG11")
    stack.peek()
    print(f"Stack after pushing: {stack}")
    
    