""" This is a greedy algorithm.
We're trying to steal from the British Museum, and we need to take the most expensive items.
But we cannot divide them into smaller parts; we can only take them or leave them.

"""
def knapsack(values, occuped_space, size_package, n):
    print("u started the func")
    if n==0 or size_package==0: #if there're no more items or nothing else fits in the package...
        print("there're no more items or nothing else fits in the package...")
        return 0
    
    # if the item doesn't fit in the package, then go to the next item
    if occuped_space[n-1] > size_package:
        print("the item doesn't fit in the package, then go to the next item")
        return knapsack(values, occuped_space, size_package, n-1)
    
    # if the item fits in the package:
    print("the item fits in the package:")
    # evaluate the best combination to add it to the package and then go to the next item
    return max(values[n-1] + knapsack(values, occuped_space, size_package-occuped_space[n-1], n-1),
                knapsack(values, occuped_space, size_package, n-1) )    

if __name__ == "__main__":
    values = [60,100,120] # each item we can steal are here
    occuped_space = [10, 25, 40] #represent the cm**2 
    size_package = 30
    n =len(values)
    result = knapsack(values, occuped_space, size_package, n)
    print(result)