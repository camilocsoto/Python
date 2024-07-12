#Arhivo creador del contenedor, se ejecuta con otro archivo
#importar python 3.8
FROM python:3.8 
# espacio de trabajo llamado app
WORKDIR /app
# copiar el req local al req del contenedor
COPY requirements.txt /app/requirements.txt
#cuando el contenedor se ejecuta, instala todas las dependencias del req -r ...
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
#copia todos los archivos y los guarda en el contenedor
COPY . /app
#usa solo si el contenedor debe ejecutarse constantemente
CMD bash -c "while true; do sleep 1; done"