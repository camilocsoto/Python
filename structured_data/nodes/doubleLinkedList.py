# qué es object como argumento de None
# la clase doubleLinkedList hereda de Node?
# no entiendo nada del constructor de la clase Node
class Node():
    def __init__(self, data, previous = None, next =None):
        self.data = data
        self.previous = previous
        self.next = next #for the first Node
        
class DoubleLink():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, data):
        #create the first Node
        newNode = Node(data)
        if self.head is None and self.tail is None:
            self.head = self.tail = Node(data)
        # add a last node
        else:
            newNode.previous = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        print("it has been added successfully")
        
    def delete(self, data):
        # NO HAY Nodo(s) en la DobleLinkedList
        if self.head is None and self.tail is None:
            return False
        # SI HAY Nodo(s) en la DobleLinkedList
        else:
            probe = self.head
            # UNICO Nodo
            if probe.previous is None and probe.next is None:
                self.head = None
                self.tail = None
                self.size -= 1
                return True
            # VARIOS Nodos
            else:
                while probe:
                    # Encontrado
                    if probe.data == data:
                        # PRIMER Nodo de la DobleLinkedList
                        if probe.previous is None and probe.next != None:
                            self.head = probe.next
                            probe = probe.next
                            probe.previous = None 
                        # ENTRE Nodos de la DobleLinkedList
                        elif probe.previous != None and probe.next != None:
                            probe.previous.next = probe.next
                            probe.next.previous = probe.previous
                        # ULTIMO Nodo de la DobleLinkedList
                        else:
                            self.tail = probe.previous
                            probe.previous.next = None
                        self.size -= 1
                        return True
                    probe = probe.next


    def __str__(self):
        probe =self.head
        result = "* "
        while probe:
            result += str(probe.data) + "<--> "
            probe = probe.next
        result += " *"
        return result
        
if __name__ == "__main__":
    execute = DoubleLink()
    i = 1
    while i < 3:
        value = input("type the thing that you wanna keep: ")
        print(execute.append(value))
        i+=1
   
    print(execute.__str__())