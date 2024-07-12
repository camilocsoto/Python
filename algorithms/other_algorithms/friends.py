def calcular_dias(a, b):
    mayor = max(a, b) #el mcm siempre va a ser mayor o igual que los nums de entrada
    while mayor % a != 0 or mayor % b != 0: #evalua si a ó b son multiplos de la variable que va aumentando
        mayor =mayor + 1 #si no son multiplos, suma al que va a ser el mcm
    return mayor


if __name__ == "__main__": #ejecuta el archivo como un script

    a = int(input("Digíte 3 números que indiquen los días que vienen las personas a la u: "))
    b = int(input())
    c = int(input())

    #pasar como atributos los  3 o más nums entrada, se hace confuso y no funciona bien la lógica x'd
    mcm_ab = calcular_dias(a, b) # por eso solo acepta 2
    resultado = calcular_dias(mcm_ab, c)
    
    print(resultado)

# No sé si te dejen usar librerias que hagan que el ejercicio sea más sencillo