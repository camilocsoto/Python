"""
create an array 
asign the a linkedlist the array
"""
class Arrays():
    def __init__(self, size, fill_values= None):
        self.items = list()
        for _ in range(size):
            self.items.append(fill_values)
        