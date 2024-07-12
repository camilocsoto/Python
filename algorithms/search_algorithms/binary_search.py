import random

def binary_search(list, start, final, objective):
    print(f"searchs {objective} between {start} and {final}")
    if start > final: # O(1)
        return False
    # if the num is in the middle
    middle = (start + final) //2
    if list[middle] == objective:
        return True
    elif list[middle] < list[objective]:
        #in the middle, there's no the objective. So, u move 1 position to count from these part
        return binary_search(list, middle+1, final, objective)
    else:
        return binary_search(list, start, middle-1, objective)

# CONSIDER:
# if u copy the list, it'll become O(n) because it has to travel one by one echar position of the list.
# u've got to travel the array with the index

if __name__ == "__main__":
    length = int(input("type de lenght of the list:"))
    objective = int(input("type de number value that you wanna know if it's in the array:"))
    #the list must be sorted
    nums_list = sorted([random.randint(1,1000) for _ in range(length)])
    print(nums_list)
    #execute order 66
    result = binary_search(nums_list, 0, len(nums_list), objective)
    print(f'the number {objective} {"exists" if result else "not exists"} in the list' )
    