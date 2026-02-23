# Imagen base
FROM python:3.11-slim

# Directorio dentro del contenedor
WORKDIR /app

# Copiar requirements primero (mejor cache)
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Comando de ejecución
CMD ["python", "main.py"]