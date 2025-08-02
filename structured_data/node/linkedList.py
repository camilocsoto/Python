"""_summary_
    First create a node, then asign it into the linked list class
    Returns:
        _type_: _description_
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:    
    """ Still NOT linking them """
    value:str
    next: Optional['Node'] = None
    
    
@dataclass
class ChainNode:
    """Linking them!"""
    head: Optional['Node'] = None
    
    def traverseChain(self):
        if self.head is None:
            raise ValueError("The chain is empty")
        actual =self.head #change the node.
        while actual is not None:
            print(f'{actual.value} -> ', end ='')
            actual = actual.next # kept the ref of next Node in ram
            
    def add_begin(self, neoNode: Node):
        """1. create the node 2. asign neoNode ref to the past head. 3. change self.head to the neoNode"""
        if self.head is None:
            self.head = neoNode
            return self.head
        # neo node ref is the past head.
        neoNode.next = self.head
        self.head = neoNode # new head
        return self.head
    
    def add_middle(self, type_add: str, oldNode: Node, neoNode: Node):
        """1. create the node 2. search the old node. 3. change self.head to the neoNode"""
        if self.head is None:
            raise ValueError('chain is empty, use add_begin first.')
        if type_add == 'after_node':
            self.after_node(oldNode, neoNode)
        if type_add == 'before_node':
            self.before_node(oldNode, neoNode)
    
    def after_node(self, oldNode: Node, neoNode: Node):
        actual = self.head
        while actual is not None:
            if actual.value == oldNode.value: 
                # has been found
                neoNode.next = actual.next
                oldNode.next = neoNode
                break 
            else: actual = actual.next
    
    def before_node(self, oldNode: Node, neoNode: Node):
        actual = self.head
        while actual is not None:
            if actual is oldNode:
                self.add_begin(neoNode)
                break
            if actual.next is oldNode:
                neoNode.next = oldNode
                actual.next = neoNode
                break            
            else: actual = actual.next

    def add_end(self, neoNode: Node):
        if self.head is None:
            raise ValueError('chain is empty, use add_begin first.')
        actual = self.head
        while actual.next is not None:
            actual = actual.next # traverse the chain
            # out of the while to get the last node.
        actual.next = neoNode
        return actual.next.next # return the new node ref
    
    def delete_begin(self):
        actual = self.head
        if actual is None:
            raise ValueError("chain is empty, use add_beggin first!")
        future_head = actual.next # keep the second planet
        self.head = future_head #reasign head.
        print(f'planet {actual.value} has been destroyed!!')
        actual.next, actual.value = None, "" #erase head and next planet
        
    def delete_end(self):        
        actual = self.head
        if actual is None:
            raise ValueError("chain is empty, use add_beggin first!")
        # just 1 nodes:
        if actual.next is None:            
            print(f'the planet {actual.value} has been destroyed!!')
            actual.next = None
            return
        
        penultimate_planet:Node = actual.next
        
        while penultimate_planet.next is not None:
            actual = penultimate_planet
            # arrive at the end of the chain
        actual.next = None
        
        

if __name__=="__main__":
    # 1. create an individual node. 2. Create the chain    
    Alderahan = Node("Alderahan")
    empire = ChainNode()
    empire.add_begin(Alderahan)
    empire.add_begin(Node("Corusant"))
    empire.add_end(Node("Naboo"))
    empire.add_begin(Node("Mandalor"))
    empire.delete_begin()
    empire.delete_end()
    empire.add_middle(type_add='before_node', oldNode=Alderahan, neoNode=Node("Pantora"))
    empire.traverseChain()  
    
    