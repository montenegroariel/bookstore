# Usa una imagen oficial de Python ligera
FROM python:3.11-slim

# Configura variables de entorno para evitar que Python escriba archivos .pyc
# y para que la salida de la consola sea fluida (sin buffers)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /code

# Copia primero solo el archivo de requerimientos para aprovechar la caché de Docker
COPY ./requirements.txt /code/requirements.txt

# Instala las dependencias
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copia el resto del código de la aplicación
COPY ./app /code/app

# Expone el puerto en el que correrá FastAPI
EXPOSE 8000

# Comando para iniciar la aplicación usando Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]