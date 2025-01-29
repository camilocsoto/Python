# create a cyrcular node structure 
class singleNode():
    """
    una lista enlazada simple, la estructura es lineal, no permite 
    múltiples conexiones directas desde un solo nodo a varios nodos.
    """
    def __init__(self, value, next =None):
        self.value = value
        self.next = next
    def __str__(self):
        return self.value

class CircularlinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 #it starts with it
        
    def addNodes(self, value):
        """
        if: self.size or self.time are empty, create the head node
        else: traverse the linked list until find the last node; there, the new node will be created 
        """
        node = singleNode(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size +=1
    
    def size(self):
        return str(self.size)
  