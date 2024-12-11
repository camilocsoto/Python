import time

# implementación iterativa
def factorial(n):
    response =1
    while response>1:
        response *=n
        n -= 1
    return response

# implementación recursiva
def recursive_factorial(n):
    #caso base
    if n == 1:
        return 0
    return n*(recursive_factorial(n-1))

if __name__ == "__main__":
    n = 10
    # iterativo
    start_time =time.time()
    print(factorial(n))
    final_time =time.time()
    print(f"iterative takes {final_time - start_time}")
    # recursive
    start_time =time.time()
    print(recursive_factorial(n))
    final_time =time.time()
    print(f"recursive takes {final_time - start_time}")
    
    
    
    