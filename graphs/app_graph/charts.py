import matplotlib.pyplot as matplot


def graph_barchart(name, label, value):
  #son dos valores del método, fx es la figura y ax son coordenadas.
  fx, ax = matplot.subplots()
  ax.bar(label, value)  # las coordenadas vab a ser en un diargrana de barras(x,y)
  matplot.savefig(f'./imgs/{name}.png')
  matplot.close()


def graph_piechart(labels, values):
  fx, ax = matplot.subplots()
  ax.pie(values, labels=labels)  #this is the way
  ax.axis('equal')  #this is the way
  matplot.savefig('./imgs/pie.png')
  matplot.close()


