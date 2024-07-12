class singleNode():
    """
    a simple linked list, the structure is linear, it does not allow
    multiple direct connections from a single node to multiple nodes.
    """
    def __init__(self, value, next =None):
        self.value = value
        self.next = next
        self.head = None
    
    def create(self):
        """
        head instantiates the node constructor with next value

        """

        keep = input("type what you wanna keep: ")
        
        if self.head is None:
            self.head = singleNode(keep)
        else:
            probe = self.head
            while probe.next != None:
                probe = probe.next
            probe.next = singleNode(keep)
        return self.__str__()
        
    def search(self, item):

        probe = self.head
        while probe.next != None and item != probe.value:
            probe = probe.next
        # When the bucle is broken, follow this validation
        if probe != None:
            print(f"{item} has been found")
        else:
            print(f"{item} hasn't been found")
    
    def replace(self, new_item, item):

        probe = self.head
        # while it isn't the last node nor the value to be replace:
        while probe != None and probe.value != item:
            probe = probe.next
        if probe != None:
            probe.value = new_item
            print(f"{item} has been replaced by {new_item}")
        else: # it's None
            print(f"{item} hasn't been found")
            
    def erase_last_item(self):

        # if this is the last item, we erase it
        if self.head.next is None:    
            self.head = None
        else: #search the last node
            probe = self.head
            while probe.next.next != None:
                probe = probe.next
            rm_data = probe.next.value
        print(f"the last node was {rm_data}, and it has been deleted")
        
            
            
            
    def __str__(self):
        """
        Print all items in the linked list
        """

        probe = self.head
        while probe is not None:
            print(probe.value)
            probe = probe.next
        return ""

if __name__ == "__main__":
    head_tail = singleNode("ships")
    head_tail.create()
    head_tail.create()

    
    