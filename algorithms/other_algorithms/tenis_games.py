
def main():
    a=0.001
    if a > 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(main())
"""
#read the problem right here: 
scanner = input("digita la cantidad de participantes:")
p = int(scanner)
games = 0

while p > 1:
    if p % 2 != 0:
        aux = p-1
        aux = aux / 2
        games =games + aux
        p = aux + 1
    else: 
        p = p/2
        games =games + p
print(games)

"""