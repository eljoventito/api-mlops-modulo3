import pandas as pd
import re
from sklearn.base import BaseEstimator, TransformerMixin
from app.core.config import cargar_config

# Cargar la configuración global
config = cargar_config()

COLUMNAS_MINIMAS_NECESARIAS = config["COLUMNAS_MINIMAS_NECESARIAS"]

# Extraer variables de la configuración YAML
bancos_comerciales_pld = config["bancos_comerciales_pld"]
bancos_comerciales_tc = config["bancos_comerciales_tc"]
cajas_ahorro_pld = config["cajas_ahorro_pld"]
cajas_ahorro_tc = config["cajas_ahorro_tc"]
retail_financieras_pld = config["retail_financieras_pld"]
retail_financieras_tc = config["retail_financieras_tc"]

FEATURES_TO_DROP = config["FEATURES_TO_DROP"]
limpiar_cats = config["limpiar_cats"]
NUMERICALS_LOG_VARS = config["NUMERICALS_LOG_VARS"]
CATEGORICAL_VARS_WITH_NA_FREQUENT = config["CATEGORICAL_VARS_WITH_NA_FREQUENT"]
CATEGORICAL_VARS_WITH_NA_MISSING = config["CATEGORICAL_VARS_WITH_NA_MISSING"]
NUMERICAL_VARS_WITH_NA = config["NUMERICAL_VARS_WITH_NA"]
BINARIZE_VARS = config["BINARIZE_VARS"]
QUAL_MAPPINGS = config["QUAL_MAPPINGS"]
valores_permitidos_cats = config["valores_permitidos_cats"]

pld_columns = bancos_comerciales_pld + cajas_ahorro_pld + retail_financieras_pld
tc_columns = bancos_comerciales_tc + cajas_ahorro_tc + retail_financieras_tc
col_drop = tc_columns + pld_columns


# 📌 Clase para limpiar valores categóricos
class LimpiarCategorias(BaseEstimator, TransformerMixin):
    def __init__(self, variables):
        self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for col in self.variables:
            X[col] = X[col].apply(lambda val: "Missing" if pd.isna(val) else re.sub(r'\W+', '_', str(val)))
        return X.astype("object")


# 📌 Clase para filtrar valores no permitidos
class ValueFilterTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, allowed_values):
        """
        Transformador que reemplaza valores no permitidos en las columnas con None 
        y genera un reporte de valores modificados.

        :param allowed_values: Diccionario con las listas de valores permitidos por columna.
        """
        self.allowed_values = allowed_values
        self.report = {}

    def fit(self, X, y=None):
        # Inicializar el reporte
        self.report = {col: {} for col in self.allowed_values.keys()}
        return self  # No necesita ajuste

    def transform(self, X):
        X = X.copy()  # Evitar modificar el DataFrame original
        for col, allowed in self.allowed_values.items():
            if col in X.columns:
                # Contar valores no permitidos antes de reemplazarlos
                mask_invalid = ~X[col].isin(allowed)  # Valores que NO están en la lista permitida
                counts = X.loc[mask_invalid, col].value_counts()

                # Guardar en el reporte
                self.report[col] = counts.to_dict()

                # Reemplazar valores no permitidos por None
                X.loc[mask_invalid, col] = None
        return X

    def get_report(self):
        """ Devuelve el reporte de valores eliminados en cada columna """
        return self.report


# 📌 Clase para calcular totales y entidades de deuda
class DeudaTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X["Bancos_PLD_Total"] = X[bancos_comerciales_pld].sum(axis=1)
        X["Cajas_PLD_Total"] = X[cajas_ahorro_pld].sum(axis=1)
        X["Retail_PLD_Total"] = X[retail_financieras_pld].sum(axis=1)
        X["PLD_Total"] = X[pld_columns].sum(axis=1)
        X["Bancos_TC_Total"] = X[bancos_comerciales_tc].sum(axis=1)
        X["Retail_TC_Total"] = X[retail_financieras_tc].sum(axis=1)
        X["TC_Total"] = X[tc_columns].sum(axis=1)
        X["Bancos_PLD_Entidades"] = (X[bancos_comerciales_pld] != 0).sum(axis=1)
        X["Cajas_PLD_Entidades"] = (X[cajas_ahorro_pld] != 0).sum(axis=1)
        X["Retail_PLD_Entidades"] = (X[retail_financieras_pld] != 0).sum(axis=1)
        X["PLD_Entidades"] = (X[pld_columns] != 0).sum(axis=1)
        X["Bancos_TC_Entidades"] = (X[bancos_comerciales_tc] != 0).sum(axis=1)
        X["Retail_TC_Entidades"] = (X[retail_financieras_tc] != 0).sum(axis=1)
        X["TC_Entidades"] = (X[tc_columns] != 0).sum(axis=1)
        X["TC_Entidades_Mas3"] = (X["TC_Entidades"] > 3).astype(int)
        X["Tiene_Deuda_PLD"] = (X["PLD_Entidades"] > 0).astype(int)
        return X.drop(columns=col_drop, errors="ignore")


# 📌 Clase para contar celulares
class CelularTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X["CANTIDAD_CELULARES"] = X[[col for col in X.columns if "CEL" in col]].notna().sum(axis=1)
        return X.drop(columns=["CELULAR1", "CELULAR2", "CELULAR3"], errors="ignore")


# 📌 Clase para convertir columnas específicas
class ConversionColumnas(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X["PROPENSION"] = X["PROPENSION"].str.split("_").str[1].astype(float)
        X["RANGO_RCI"] = X["RANGO_RCI"].str.split("_").str[0].astype(float)
        X["COMPETITIVIDAD"] = X["COMPETITIVIDAD"].map(lambda x: 0 if x == "Missing" else 1)
        return X


# 📌 Clase para mapear valores categóricos a numéricos
class CustomMapper(BaseEstimator, TransformerMixin):
    def __init__(self, mappings, default_value=-1):
        self.mappings = mappings
        self.default_value = default_value  

    def fit(self, X, y=None):
        return self  

    def transform(self, X):
        X = X.copy()
        for col, mapping in self.mappings.items():
            X[col] = X[col].apply(lambda x: self.clean_value(x, mapping))
        return X

    def clean_value(self, x, mapping):
        if pd.isna(x) or x in [None, "", " ", "  "]:
            x = "Missing"
        x = str(x).strip()
        return mapping.get(x, self.default_value)


# 📌 Función para transformar `MENSAJE_VARIACION`
def transformar_mensaje_variacion(X):
    X = X.copy()
    X["ESTADO_TASA"] = X["MENSAJE_VARIACION"].apply(
        lambda x: 2 if "MENOS_TASA" in str(x)
        else 1 if "MISMA_TASA" in str(x)
        else 3 if "NUEVA" in str(x)
        else 0
    )
    X["ESTADO_OFERTA"] = X["MENSAJE_VARIACION"].apply(
        lambda x: 0 if "MENOS_OFERTA" in str(x)
        else 1 if "MISMA_OFERTA" in str(x)
        else 3 if "NUEVA" in str(x)
        else 2
    )
    X["NUEVA_OFERTA"] = X["MENSAJE_VARIACION"].apply(
        lambda x: 1 if "NUEVA" in str(x) else 0
    )
    return X


def validar_cabeceras_dataframe(df: pd.DataFrame, lista_columnas: list):
    """
    Valida si un DataFrame contiene las cabeceras esperadas y devuelve un estado.
    """
    estado_bool = False
    columnas_df = set(df.columns)
    columnas_esperadas = set(lista_columnas)

    columnas_faltantes = columnas_esperadas - columnas_df
    columnas_adicionales = columnas_df - columnas_esperadas

    if not columnas_faltantes:
        estado = "✅ Todas las columnas requeridas están presentes."
        estado_bool = True
    else:
        estado = f"⚠️ Faltan columnas necesarias ({', '.join(columnas_faltantes)})"

    resultado = {
        "valido": len(columnas_faltantes) == 0,
        "estado": estado,
        "faltantes": list(columnas_faltantes),
        "adicionales": list(columnas_adicionales),
        "total_columnas_correctas": len(columnas_df & columnas_esperadas),
        "estado_bool": estado_bool
    }

    return resultado


def prediccion_o_inferencia(loaded_pipeline, loaded_model, datos_de_test):
    # Dropeamos
    datos_de_test = datos_de_test[COLUMNAS_MINIMAS_NECESARIAS]
    # Cast MSSubClass as object
    data_transform = loaded_pipeline.transform(datos_de_test)
    filter_transformer = loaded_pipeline.named_steps["filter_values"]

    report = filter_transformer.get_report()
    data_transform = pd.DataFrame(data_transform, columns=loaded_pipeline.named_steps["drop_features"].get_feature_names_out())
    expected_features = loaded_model.get_raw_model().feature_names_in_
    data_transform = data_transform[expected_features]
    predicciones = loaded_model.predict(data_transform)

    return predicciones, report, data_transform