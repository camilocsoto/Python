import random

def insertion_sort(lista):
# complexity O(n**2)
    for i in range(1, len(lista)): #ordered list
        valor_actual = lista[i]
        posicion_actual = i

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual: #unordered sublist 
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual
    return lista
    


if __name__ == "__main__":
    length = int(input("type de lenght of the list:"))
    #the list must be sorted
    nums_list = [random.randint(1,1000) for _ in range(length)]
    print(nums_list)
    #execute order 66
    result = insertion_sort(nums_list)
    print(result)
    