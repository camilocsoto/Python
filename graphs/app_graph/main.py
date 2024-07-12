import read_csv as csv
import extension
import charts
import pandas as pd

# filtrar a partir de un modulo externo

def exec():

  #trae toda la info en un diccionario
  data = csv.read_csv('world_population.csv')
  # trae el país a gráficar
  country = input('Type country => ')
  #filtra el  pais con todos sus datos correspondientes.
  setter = extension.get_people_by_country(data, country)
  #valida que si exista (diferente de null)
  if len(setter) > 0:
    # trae el diccionario con todos los datos del pais
    country = setter[0]
    #trae ciertas columnas del diccionario
    keys, values_b = extension.countries(country)  
    #genera el gráfico
    charts.graph_barchart(country['Country/Territory'], keys, values_b)

    # * * * * pie chart * * * * * * *
    # Forma 1: CHINGO DE MÓDULOS!!!
    labels, values = extension.world_population_pie(data)
    charts.graph_piechart(labels, values)
    # Forma 2: PANDAS!!!
    dataframe = pd.read_csv('world_population.csv')
    dataframe = dataframe[dataframe['Continent'] == 'Africa'] #confuse!

    countries = dataframe['Country/Territory'].values
    percentages = dataframe['World Population Percentage'].values
    charts.graph_piechart(countries, percentages)
if __name__ == '__main__':
  print('starting...')
  exec()
  print('ended...')
 