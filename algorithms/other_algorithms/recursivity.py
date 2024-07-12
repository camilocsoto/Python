def multiple_recursion(n):
    if n ==0 or n ==1:
        return 0
    return multiple_recursion(n-1)+multiple_recursion(n-2)
# inviable O(2**n)

if __name__ == "__main__":
    print(multiple_recursion(2))