from fastapi import APIRouter
from fastapi.responses import HTMLResponse

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
                👉 Accede a la documentación interactiva Swagger: 
                <a href="/docs" target="_blank">/docs</a>
            </p>

            <h3>🧪 Datos de Ejemplo para el endpoint <code>/api/predict</code></h3>

            <h4>🟥 Clase 0:</h4>
            <pre style="background:#f4f4f4; padding:10px; border-radius:5px; overflow-x:auto;">
{
  "DNI": "35500",
  "BASE": "2025_01",
  "CELULAR1": "949372003",
  "CELULAR2": null,
  "CELULAR3": null,
  "12M_MONTO": 8400.0,
  "12M_TASA": 0.799,
  "18M_MONTO": 10900.0,
  "18M_TASA": 0.799,
  "24M_MONTO": 10900.0,
  "24M_TASA": 0.799,
  "36M_MONTO": 10900.0,
  "36M_TASA": 0.799,
  "EDAD": 32.0,
  "MARCA_LABORAL": "2.DEPEN+INDEPEN",
  "DEPARTAMENTO": "LIMA",
  "PROVINCIA": "LIMA",
  "DISTRITO_INEI": "LIMA",
  "LIMAS": "LIMA CENTRO",
  "PROPENSION": "PROPENSION 2",
  "PLD_NACION": 0.0,
  "PLD_BCP": 0.0,
  "PLD_BBVA": 0.0,
  "PLD_SAGA": 0.0,
  "PLD_SCOTIA": 0.0,
  "PLD_C_HUANCAYO": 0.0,
  "PLD_CREDISCOTIA": 0.0,
  "PLD_INTERBANK": 0.0,
  "PLD_C_AREQUIPA": 0.0,
  "PLD_C_CUSCO": 0.0,
  "PLD_MIBANCO": 0.0,
  "PLD_RIPLEY": 0.0,
  "PLD_C_PIURA": 0.0,
  "PLD_EFECTIVA": 0.0,
  "PLD_PICHINCHA": 0.0,
  "PLD_CONFIANZA": 0.0,
  "TC_BCP": 0.0,
  "TC_SAGA": 0.0,
  "TC_INTERBANK": 0.0,
  "TC_BBVA": 0.0,
  "TC_OH": 0.0,
  "TC_RIPLEY": 0.0,
  "TC_SCOTIA": 0.0,
  "TC_CREDISCOTIA": 0.0,
  "TC_PICHINCHA": 0.0,
  "TC_CENCOSUD": 0.0,
  "MENSAJE_TASA": "NO APLICA A EXCEPCION DE TASA",
  "COMPETITIVIDAD": null,
  "PRINCIPALIDAD_CONSUMO": "SIN DEUDA CONSUMO",
  "MENSAJE_VARIACION": "MISMA OFERTA Y MISMA TASA",
  "ULTIMA_AGRUPACION": "CONTACTO NO EFECTIVO",
  "ULTIMO_RESULTADO": "NEGATIVO",
  "ULTIMO_MOTIVO": "SIN REBATE - NO INTERESADO CORTA LLAMADA",
  "RANGO_RCI": "1. <0%,10%>",
  "ESTADO_CIVIL": "Soltero",
  "GENERO": "M",
  "veces_acepto_producto": null,
  "tiempo_desde_ultima_conversion": null,
  "tiempo_desde_ultima_negacion": null,
  "intentos_totales": null,
  "meses_gestionados": null,
  "dias_ultima_gestion": null,
  "ultima_gestion": "NO GESTIONADO",
  "veces_sin_respuesta": null,
  "veces_solicitud_seguimiento": null,
  "promedio_dias_entre_gestiones": null,
  "max_intentos_en_un_mes": null,
  "veces_respuesta_positiva": null,
  "veces_respuesta_negativa": null,
  "_merge_variables": 0.0
}
            </pre>

            <h4>🟩 Clase 1:</h4>
            <pre style="background:#f4f4f4; padding:10px; border-radius:5px; overflow-x:auto;">
{
  "DNI": "3606",
  "BASE": "2025_01",
  "CELULAR1": "942638015",
  "CELULAR2": "942660839",
  "CELULAR3": null,
  "12M_MONTO": 6000.0,
  "12M_TASA": 0.7,
  "18M_MONTO": 8000.0,
  "18M_TASA": 0.7,
  "24M_MONTO": 9500.0,
  "24M_TASA": 0.7,
  "36M_MONTO": 11600.0,
  "36M_TASA": 0.7,
  "EDAD": 39.0,
  "MARCA_LABORAL": "4.INFORMAL",
  "DEPARTAMENTO": "LIMA",
  "PROVINCIA": "LIMA",
  "DISTRITO_INEI": "SANTA ROSA",
  "LIMAS": "LIMA NORTE",
  "PROPENSION": "PROPENSION 1",
  "PLD_NACION": 0.0,
  "PLD_BCP": 0.0,
  "PLD_BBVA": 0.0,
  "PLD_SAGA": 0.0,
  "PLD_SCOTIA": 0.0,
  "PLD_C_HUANCAYO": 0.0,
  "PLD_CREDISCOTIA": 0.0,
  "PLD_INTERBANK": 0.0,
  "PLD_C_AREQUIPA": 0.0,
  "PLD_C_CUSCO": 0.0,
  "PLD_MIBANCO": 0.0,
  "PLD_RIPLEY": 0.0,
  "PLD_C_PIURA": 0.0,
  "PLD_EFECTIVA": 0.0,
  "PLD_PICHINCHA": 0.0,
  "PLD_CONFIANZA": 0.0,
  "TC_BCP": 3441.0,
  "TC_SAGA": 0.0,
  "TC_INTERBANK": 882.0,
  "TC_BBVA": 0.0,
  "TC_OH": 0.0,
  "TC_RIPLEY": 0.0,
  "TC_SCOTIA": 0.0,
  "TC_CREDISCOTIA": 0.0,
  "TC_PICHINCHA": 0.0,
  "TC_CENCOSUD": 0.0,
  "MENSAJE_TASA": "NO APLICA A EXCEPCION DE TASA",
  "COMPETITIVIDAD": "OFERTA MAYOR A ALGUNA DEUDA",
  "PRINCIPALIDAD_CONSUMO": "DEUDA EN BANCOS GRANDES",
  "MENSAJE_VARIACION": "CON MAS OFERTA Y MENOS TASA",
  "ULTIMA_AGRUPACION": "CONTACTO NO EFECTIVO",
  "ULTIMO_RESULTADO": "NEGATIVO",
  "ULTIMO_MOTIVO": "SIN REBATE - NO INTERESADO CORTA LLAMADA",
  "RANGO_RCI": "4. [30%,60%]",
  "ESTADO_CIVIL": "Casado",
  "GENERO": "M",
  "veces_acepto_producto": 0.0,
  "tiempo_desde_ultima_conversion": null,
  "tiempo_desde_ultima_negacion": 21.0,
  "intentos_totales": 124.0,
  "meses_gestionados": 1.0,
  "dias_ultima_gestion": 5.0,
  "ultima_gestion": "NO CONTACTO",
  "veces_sin_respuesta": 120.0,
  "veces_solicitud_seguimiento": 0.0,
  "promedio_dias_entre_gestiones": 0.0,
  "max_intentos_en_un_mes": 124.0,
  "veces_respuesta_positiva": 0.0,
  "veces_respuesta_negativa": 4.0,
  "_merge_variables": 1.0
}
            </pre>

            <p style="margin-top:40px;">🔁 Copia y pega uno de estos JSON en el Swagger o Postman para hacer una predicción.</p>
        </body>
    </html>
    """
