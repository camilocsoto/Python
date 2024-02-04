import csv

#funcion a ejecutar en el método main, buena práctica.
def read_csv(path):
  # abrir el csv para leer
  with open(path, 'r') as csv_file:
    read_file = csv.reader(csv_file, delimiter=',')
    header_file = next(read_file)
    data =[]
    for row in read_file:
      #union de tuplas = [('Rank', '21')...]
      union_key_value = zip(header_file, row)
      #convertir tupla en diccionario
      dictionary= {key: value for key, value in union_key_value}
      data.append(dictionary)
  return data
  