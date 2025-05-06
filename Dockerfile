# Imagen base optimizada
FROM python:3.10-slim

# Evitar prompts interactivos durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

# Setear el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . .

# Instalar dependencias
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Expone el puerto (usado por Railway vía la variable $PORT)
EXPOSE 8000
ENV PORT=8000

# Comando para ejecutar la API (como en railway.toml)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
