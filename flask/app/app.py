from flask import Flask, render_template, request

app = Flask(__name__)

#vista que carga desde la raíz
@app.route('/')
def index():
    return render_template('index.html') #renderiza lo que está en templates

#recibe los datos del formulario
@app.route('/getData', methods = ['GET', 'POST'])
def getData():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        print(f'los datos que llegaron son: {num1} y {num2}')
        return calculate(num1, num2)
    
def calculate(num1, num2):
    a = int(num1)
    b = int(num2)
    sum=a+b
    red=a-b
    mlt=a*b
    div=a/b
    sendData = {
        'suma':sum,
        'resta':red,
        'multiplicacion':mlt,
        'division':div
    }
    return render_template('index.html', data = sendData)



if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug=True, port=5000)