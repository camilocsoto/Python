FROM python:3.8-alpine 
WORKDIR /app 
COPY requirements.txt /app 
RUN apk add --no-cache gcc musl-dev \     
    && pip install -r requirements.txt 
COPY middleware.py /app 
CMD ["python", "middleware.py"]