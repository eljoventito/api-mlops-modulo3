from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from app.routes import predict, postgresql  # tus rutas reales

router = APIRouter()



@router.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>API Módulo 3 - MLOps</title>
        </head>
        <body style="font-family: Arial; max-width: 900px; margin: auto;">
            <h1>🚀 API Módulo 3 – Bootcamp de MLOps - DataPath</h1>
            <h2>📍 Luis Daniel Villacorta Tito</h2>
            <p>Este proyecto despliega un modelo de Machine Learning mediante <strong>FastAPI</strong>, integrado con <strong>PostgreSQL</strong>, y publicado en <strong>Railway</strong>.</p>

            <p>
                Puedes acceder a la documentación Swagger de la API aquí 👉
                <a href="/docs" target="_blank">/docs</a>
            </p>


            <p style="margin-top:30px;">🔄 Haz tus pruebas en Swagger o con Postman para ver la predicción del modelo.</p>
        </body>
    </html>
    """
