#this thing prints a triangle
def printer():
    draw = "* "
    spaces = " "
    tower, empty = 0, 10    
    while tower < 5:
        tower += 1
        empty -=2
        print(f"{spaces*(empty//2)}{draw*tower}{spaces*(empty//2)}")
        
def _typedates():
    _ranges = range(1, 100,2)
    for i in _ranges:
        print(i)

if __name__  == "__main__":
    printer()
    _typedates()