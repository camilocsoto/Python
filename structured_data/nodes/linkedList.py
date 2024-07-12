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

class linkedList():
    def __init__(self):
        self.first = None
        self.size = 0 #it starts with it
        
    def addNodes(self, value):
        """
        if: self.size or self.time are empty, create the first node
        else: traverse the linked list until find the last node; there, the new node will be created 
        """
        node = singleNode(value)
        if self.size == 0:
            self.first = node
        else:
            current = self.first # this changes in each iteration
            while current.next !=None: #traverse all the linked list
                current = current.next 
            #when the last node is found, add it
            current.next =node
        #outside the if statement, always has to add 1 to the variable
        self.size +=1
    
    def size(self):
        return str(self.size)
    
    def delete(self, value):
        """
        first if: control who evaluates the fist item
        while: search if the next item is the same as that has been asked.
        """
        current = self.first
        
        if current.value == value:
            self.first = current.next
            self.size -= 1
            return self.printer()
        
        while current.next.value is not None:
            if current.next.value ==value:
                #when it's found:
                deletedNode = current.next # it's next to the item to be erase
                # the selected node won't be connected  to the linked list anymore
                current.next = deletedNode 
                self.size -=1
                print(f"node {value} deleted")
                return current.next
            else:
                current = current.next
            print((f"{value} wasn't deleted"))
            return current
        
        
    def search(self, value):
        current = self.first
        while current is not None:
            if current.value == value:
                print(f"{current.value} was found")
                return current.value
            current = current.next
        print(f"{value} wasn't found")
        return value
        
    def clean(self):
        self.first, self.size = None, 0
    
    def printer(self):
        current = self.first
        while current:
            print(current.value)
            current = current.next
    
if __name__=="__main__":
    ships = linkedList()
    ships.addNodes("Venator")
    ships.addNodes("X-wing")
    ships.addNodes("Tie-figther")
    ships.addNodes("Stelar destructor")
    ships.printer()
    ships.search("Naboo fighter")
    ships.delete("X-wing")
    