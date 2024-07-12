#construir el diccionario para que con el país seleccionado se obtenga la población
def countries(country_dict):
  population_dict = {
      '2022': float(country_dict['2022 Population']),
      '2020': float(country_dict['2020 Population']),
      '2015': float(country_dict['2015 Population']),
      '2010': float(country_dict['2010 Population']),
      '2000': float(country_dict['2000 Population']),
      '1990': float(country_dict['1990 Population']),
      '1980': float(country_dict['1980 Population']),
      '1970': float(country_dict['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values

def world_population_pie(world):
  dictionary = {item['Country/Territory']: item['World Population Percentage'] for item in world}
  labels = dictionary.keys()
  values = dictionary.values()
  return labels, values

#Obtener el país mediante un input
def get_people_by_country(data, country):
  get_country = list(
      filter(lambda keys: keys['Country/Territory'] == country, data))
  return get_country
