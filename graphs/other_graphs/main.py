from bokeh.plotting import figure, output_file, show
import webbrowser, os

def exec():
    output_file("simple_graph.html")
    fig = figure()
    question = int(input("How many values do  you want to see in the graph?"))
    x_vals = list(range(question))
    y_vals = [y**2 for y in x_vals]
    fig.line(x_vals, y_vals, line_width=2)
    show(fig)
    
    #open the browser:
    filePath = os.path.abspath("simple_graph.html")
    print(f"open in the browser: {filePath}")
    
    filepath = os.path.abspath("simple_graph.html") # it should works on windows
    # Convertir la ruta a la forma compatible con WSL
    filepath_wsl = filepath.replace('/home', 'wsl.localhost/Ubuntu/home') #to open it in wsl2
    return webbrowser.open(f'file://{filepath_wsl}')
    
    
    

if __name__=="__main__":
    exec()
    