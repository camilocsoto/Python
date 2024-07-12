class Piramide():
    def sum(self,lower, upper, margin=0):
        """
        Too many recursivity
        """
        spaces = " " *margin
        print(f"{spaces} {lower} {upper}")
        if lower > upper:
            print(spaces, 0)
            return 0
        else:
            #print(f"{spaces} {(lower+1)} {upper} {(margin+4)}")
            result = lower + self.sum((lower+1),upper,(margin+4))
            print(spaces, result)
            return result
if __name__ == "__main__":
    instaces = Piramide()
    instaces.sum(1, 5)
    
"""
Diccionarios: 
"""