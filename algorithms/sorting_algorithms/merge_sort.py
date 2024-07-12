import random

def merge_sort(list): #complexity O(n*ln(n))
    if len(list)>1:
        middle = len(list)//2
        left = list[:middle]
        right = list[middle:]
        print(f"{left} ***** {right}")
        merge_sort(left)
        merge_sort(right)
        print("ya hay un index por cada lista")
        
        #merge the indexes 
        l = 0 # left sublist 
        r = 0 # right sublist 
        k = 0 # final sublist 
        while l < len(left) and r < len(right): #continue if still are nums in the arrays
            if left[l] < right[r]: # if the first nums of the left list are smaller than right list
                list[k] =left[l]
                l += 1
            else:
                list[k] =right[r]
                r += 1
            k += 1 # it won't replace the nums that you organized
        
        while l < len(left): #if still are nums left over, you add it
            list[k] = left[l]
            l += 1
            k += 1
            
        while r < len(right):
            list[k] = right[r]
            r += 1
            k += 1
    return list


if __name__ == "__main__":
    length = int(input("type de lenght of the list:"))
    #the list must be sorted
    nums_list = [random.randint(1,1000) for _ in range(length)]
    print(nums_list)
    #execute order 66
    result = merge_sort(nums_list)
    print(result)
