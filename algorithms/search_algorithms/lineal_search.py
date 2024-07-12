import random

# The complexity is O(n)
def lineal_search(list, obective):
    match = False #O(1)
    for item in list: #O(n)
        if item == obective: #O(1)
            match = True
            break
    return match


if __name__ == "__main__":
    length = int(input("type de lenght of the list:"))
    objective = int(input("type de number value that you wanna know if it's in the array:"))
    nums_list = [random.randint(1,1000) for _ in range(length)]
    print(nums_list)
    #execute order 66
    result = lineal_search(nums_list, objective)
    print(f'the number {objective} {"exists" if result else "not exists"} in the list' )
