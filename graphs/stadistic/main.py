
from statistics import median, mean, mode, stdev, variance
import csv

# read sales from csv.
monthly_sales = {}
with open('monthly_sales.csv', mode='r') as csv_file:
    read_file = csv.DictReader(csv_file, delimiter=',')
    #header_file = next(read_file)
    for row in read_file:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(sales)

# mean - promedio
print(f"Mean: {mean(sales)}")

#median - mediana: en un set de datos ordenados, es el la mitad.
print(f"Median: {median(sales)}")

#mode - moda: es el que más se repite
print(f"mode: {mode(sales)}")

#stdev - desviación estandar: cuantifica la disperción, y es la formula larga de la varianza.
print(f"stdev: {stdev(sales)}")

# variance - varianza: es la media de los cuadrados de las diferencias entre cada punto y la media.
print(f"variance: {variance(sales)}")

assert type(sales) == list, "sales should be a list"