from app.schemas.predict import RegistroCliente, PrediccionConInputResponse
import joblib
import pandas as pd
import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
from app.core.config import cargar_config
from app.utils.preprocessors import (
    ValueFilterTransformer, LimpiarCategorias, DeudaTransformer, CelularTransformer,
    ConversionColumnas, CustomMapper, transformar_mensaje_variacion,
    validar_cabeceras_dataframe,
    prediccion_o_inferencia
)

# Parchear __main__ para que joblib pueda encontrar la clase
import __main__
__main__.ValueFilterTransformer = ValueFilterTransformer
__main__.LimpiarCategorias = LimpiarCategorias
__main__.DeudaTransformer = DeudaTransformer
__main__.CelularTransformer = CelularTransformer
__main__.ConversionColumnas = ConversionColumnas
__main__.CustomMapper = CustomMapper
__main__.transformar_mensaje_variacion = transformar_mensaje_variacion
__main__.CustomMapper = CustomMapper

config = cargar_config()
COLUMNAS_MINIMAS_NECESARIAS = config["COLUMNAS_MINIMAS_NECESARIAS"]

router = APIRouter()

# Cargar modelo y pipeline
pipeline_path = os.path.join("app", "models", "pipeline_preprocesamiento.pkl")
model_path = os.path.join("app", "models", "model_clasification.joblib")

loaded_pipeline = joblib.load(pipeline_path)
loaded_model = joblib.load(model_path)


class InputData(BaseModel):
    data: List[Dict[str, Any]]  # Lista de diccionarios con los datos de entrada


@router.post("/predict", response_model=PrediccionConInputResponse)
def predict_cliente(data: RegistroCliente):
    df = pd.DataFrame([data.model_dump(by_alias=True)])
    validacion = validar_cabeceras_dataframe(df, COLUMNAS_MINIMAS_NECESARIAS)
    if not validacion["valido"]:
        raise HTTPException(status_code=400, detail=validacion)

    pred, _, _ = prediccion_o_inferencia(loaded_pipeline, loaded_model, df[COLUMNAS_MINIMAS_NECESARIAS])

    return {
        "prediction": int(pred[0]),
        "input": data.model_dump(by_alias=True)}
