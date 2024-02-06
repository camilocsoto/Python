import requests

def http():
    r = requests.get('https://api.escuelajs.co/api/v1/products') # Consume api de un server
    print(r.status_code)
    # easy way: print(list(r))
    categories = r.json() #se parsea a los diccionarios a json
    for category in categories:
        print(category['description'])
