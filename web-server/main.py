import request
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
# crear una instancia
app = FastAPI()
#crear primer endpoint
# decorador: Indica la ruta con que la web va a acceder.
@app.get('/') 
def getList():
    return [1,2,3,4,5]

#crear segundo recurso /endpoint
@app.get('/contact', response_class=HTMLResponse) # decorador: ruta sin extensión
async def getContact():
    return """
            <html>
                <head>
                    <title>Some HTML in here</title>
                </head>
                <body>
                    <h1>Look ma! HTML!</h1>
                </body>
            </html>
           """

def run():
    request.http()

if __name__ == "__main__":
    run()