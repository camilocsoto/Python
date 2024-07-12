import random
#O(n**2) no es un algoritmo muy bueno
def bubble_sourt(list):
    n = len(list) # size of the list
    
    for i in range(n): # put the index of the array 
        for j in range(0, n-i-1): # start over & over again from the beggin to the end. 
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j] #change the nums...
    
    return list

if __name__ == "__main__":
    length = int(input("type de lenght of the list:"))
    #the list must be sorted
    nums_list = [random.randint(1,1000) for _ in range(length)]
    print(nums_list)
    #execute order 66
    result = bubble_sourt(nums_list)
    print(result)
    