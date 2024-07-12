
"""
Ayudame con un problema en python, recorre en el diccionario client1 y comparalo con el client2 así:
El diccionario client1 en su atributo "nums_faltantes" lo recorres ycomparas con el client2 en su atributo "nums_repetidos". Si hay un número o varios que coincidan, lo vas a agregar a una lista que diga change1
El diccionario client2 en su atributo "nums_faltantes" lo recorres y comparas con el client1 en su atributo "nums_repetidos". Si hay un número o varios que coincidan, lo vas a agregar a una lista que diga change2
Arma las listas change1 y change2 con sus datos correspondientes. Deben estar bien armadas.

Si change1 y change2 no están vacías: vas a hacer lo siguiente:
Tienes que, hacer change1 y change2 tengan la misma cantidad de números: si uno tiene más números, debes borrar los últimos números de la lista que más numeros tiene hasta que sean de la misma longitud.
Cuando change1 y change2 midan lo mismo debes hacer esto:
usar la lista change1 para:
Añadir el o los valores de change1 a client1[nums_repetidos]
eliminar el o los valores anteriores de:
client2[nums_repetidos]
client1[nums_faltantes]

Luego, vas a usar la lista change2 para:
Añadir el o los valores de change2 a client2[nums_repetidos]
eliminar el o los valores anteriores de:
client1[nums_repetidos]
client2[nums_faltantes]

Si se suma la longitud de client1['nums'] + client1['nums_repetidos'] debería dar 11
Si se suma la longitud de client2['nums'] + client2['nums_repetidos'] debería dar 11
Si se hace eso, el algoritmo quedó bien. 
"""
                
client1 = {'ip': '172.17.0.6', 'nums': [7, 10, 0, 5, 2], 'nums_faltantes': [1, 3, 4, 6, 8, 9], 'nums_repetidos': [0, 2, 5, 7, 10, 7]}
client2 = {'ip': '172.17.0.4', 'nums': [7, 8, 4, 6, 2, 3, 10, 0], 'nums_faltantes': [1, 5, 9], 'nums_repetidos': [3, 4, 3]}
def getClientsDictionaries(client1, client2):
    print("Entró al serverClient y recibió los diccionarios.")
    print(f'Antes -> client1: {client1} y client2: {client2}')
    
    change1 = []
    change2 = []

    # Crear lista change1
    for num in client1['nums_faltantes']:
        if num in client2['nums_repetidos']:
            change1.append(num)
    
    # Crear lista change2
    for num in client2['nums_faltantes']:
        if num in client1['nums_repetidos']:
            change2.append(num)
    
    # Ajustar longitudes de change1 y change2
    if len(change1) > len(change2):
        change1 = change1[:len(change2)]
    elif len(change2) > len(change1):
        change2 = change2[:len(change1)]

    # Aplicar cambios a los diccionarios
    for num in change1:
        client1['nums_repetidos'].append(num)
        client1['nums_faltantes'].remove(num)
        client2['nums_repetidos'].remove(num)
    
    for num in change2:
        client2['nums_repetidos'].append(num)
        client2['nums_faltantes'].remove(num)
        client1['nums_repetidos'].remove(num)
    
    # Verificar longitudes
    assert len(client1['nums']) + len(client1['nums_repetidos']) == 11
    assert len(client2['nums']) + len(client2['nums_repetidos']) == 11
    
    print(f'Después -> client1: {client1} y client2: {client2}')
    return client1, client2

if __name__ == "__main__":
    getClientsDictionaries(client1, client2)
    
#como hago para unir los arrays de client1 "nums_repetidos" y "nums" en un unico array