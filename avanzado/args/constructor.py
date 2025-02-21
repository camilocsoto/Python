class Employee():
    def __init__(self,name, *args, **kwargs):
        self.name = name
        self.skills = args
        self.info = kwargs
        
        
    def print_info(self):
        print(f"Name: {self.name}", "\n", f"Skills: {self.skills}", "\n", f"Info: {self.info}", end="\n\n")
        
    # unpackage
    def add_hobbies(self, *args):
        self.other_info = args
        print(self.other_info)
        
emp1 = Employee("John", "Python", "Java", "C++", age=23, city="New York", job="Engineer", area="cloud",experiance=2)
print(emp1.print_info())

# unpackage the tuple.
hobbies = ("read scifi books", "study new technologies", "play chess")
emp1.add_hobbies(*hobbies)
print(emp1.other_info)
