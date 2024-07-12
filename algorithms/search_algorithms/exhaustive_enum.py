def exhaustive_enumeration(objective): # The complexity of this algorithm is O(n)
    counter = 0
    
    while counter**2 < objective:
        counter +=1
    
    if counter**2 == objective:
        return f"the num {objective} has the root square {counter}"
    else:
        return approximation_sol(objective)
    
def approximation_sol(objective): # other algorithm
    epsilon = 0.1 #this means that the approximation will be valid if it is less than 10% 
    next_step = epsilon**2 # How many steps do we want to advance the next numbero in each iteration
    starts_with = 0.0
    # abs() is like |-2|
    while abs(starts_with**2-objective) >= epsilon and starts_with <= objective:
    # if the residue is bigger than the 10% valid ||| don't go with negative values
        starts_with += next_step
    
    if abs(starts_with**2-objective) >= epsilon:
        return f"the value {objective} has no an approximation of square root"
    else:
        return f"the num {objective} has the root square {starts_with}"
# =========================================================================================
"""
the previous functions can be better with the binay search:
objective: it's the num you wanna know if has a square root
"""
def binary_search(objective):
    print(f"iniciate the binary search")
    epsilon = 0.0001 #the error range is 1%
    down = 0.0
    upside = max(1.0, objective)
    response = (down + upside) /2
    
    
    while abs(response**2 - objective) >= epsilon:
        print(f"iniciate the binary search, where: epsilon={epsilon}; down={down}; upside={upside}; resp={response}")
        if response**2 < objective:
            down = response
        else:
            upside = response
            
        response = (upside + down) / 2
    return f"the num {objective} has the root square {response}"
    
    

if __name__ == "__main__":
    objective = int(input("type a num to know if it has a square root "))
    # result = exhaustive_enumeration(objective)
    result = binary_search(objective)
    print(result)