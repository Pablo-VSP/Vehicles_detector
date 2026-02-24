# Imagen base
FROM python:3.11-slim

# Directorio dentro del contenedor
WORKDIR /app

# Copiar requirements primero (mejor cache)
COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Comando de ejecución
CMD ["python", "main.py"]