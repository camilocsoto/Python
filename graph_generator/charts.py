import matplotlib.pyplot as mat

def generate_pie_chart(): # 
    labels = ['a', 'b', 'c']
    values = [20,42,38]
    fig, ax = mat.subplots()
    ax.pie(values, labels=labels)
    #don't show, it's to save in a folder mat.show()
    mat.savefig('pie.png')
    mat.close()
