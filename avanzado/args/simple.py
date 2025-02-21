def sum_nums(*args): # args is a tuple
    return sum(args)
    
print(sum_nums(2,2,23,4,231,312,13,213,123123,123,12,3123,13,123,123,12,312,312,31,2312,2))

def sens_info(**kwargs): # kwargs is a dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(sens_info(name="John", age=23, city="New York", job="Engineer"))
