FROM python:3.10

WORKDIR /web-server

COPY requirements.txt /web/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /web/requirements.txt

COPY . /web-server

CMD ["uvicorn", "main:web", "--host", "0.0.0.0", "--port", "80"]