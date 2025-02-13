import csv
"""
  Returns:
      with open(path, mode='a') as csv_file: agrega texto a un txt
      with open(path, mode='w') as csv_file: sobreescribe texto a un txt
      with open(path, mode='r', new_line = new_line) as csv_file: lee el texto a un txt
  Do:
    txt_file.write(\n\n): salto de linea
"""
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
  