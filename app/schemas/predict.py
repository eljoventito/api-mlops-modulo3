from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PrediccionConInputResponse(BaseModel):
    input: Dict[str, Any]
    prediction: float


class RegistroCliente(BaseModel):
    DNI: Optional[str]
    BASE: Optional[str]
    CELULAR1: Optional[str]
    CELULAR2: Optional[str]
    CELULAR3: Optional[str]

    MONTO_12M: float = Field(..., alias="12M_MONTO")
    TASA_12M: float = Field(..., alias="12M_TASA")
    MONTO_18M: float = Field(..., alias="18M_MONTO")
    TASA_18M: float = Field(..., alias="18M_TASA")
    MONTO_24M: float = Field(..., alias="24M_MONTO")
    TASA_24M: float = Field(..., alias="24M_TASA")
    MONTO_36M: float = Field(..., alias="36M_MONTO")
    TASA_36M: float = Field(..., alias="36M_TASA")

    EDAD: float
    MARCA_LABORAL: str
    DEPARTAMENTO: str
    PROVINCIA: str
    DISTRITO_INEI: str
    LIMAS: str
    PROPENSION: Optional[str]

    PLD_NACION: Optional[float]
    PLD_BCP: Optional[float]
    PLD_BBVA: Optional[float]
    PLD_SAGA: Optional[float]
    PLD_SCOTIA: Optional[float]
    PLD_C_HUANCAYO: Optional[float]
    PLD_CREDISCOTIA: Optional[float]
    PLD_INTERBANK: Optional[float]
    PLD_C_AREQUIPA: Optional[float]
    PLD_C_CUSCO: Optional[float]
    PLD_MIBANCO: Optional[float]
    PLD_RIPLEY: Optional[float]
    PLD_C_PIURA: Optional[float]
    PLD_EFECTIVA: Optional[float]
    PLD_PICHINCHA: Optional[float]
    PLD_CONFIANZA: Optional[float]

    TC_BCP: Optional[float]
    TC_SAGA: Optional[float]
    TC_INTERBANK: Optional[float]
    TC_BBVA: Optional[float]
    TC_OH: Optional[float]
    TC_RIPLEY: Optional[float]
    TC_SCOTIA: Optional[float]
    TC_CREDISCOTIA: Optional[float]
    TC_PICHINCHA: Optional[float]
    TC_CENCOSUD: Optional[float]

    MENSAJE_TASA: Optional[str]
    COMPETITIVIDAD: Optional[str]
    PRINCIPALIDAD_CONSUMO: Optional[str]
    MENSAJE_VARIACION: Optional[str]
    ULTIMA_AGRUPACION: Optional[str]
    ULTIMO_RESULTADO: Optional[str]
    ULTIMO_MOTIVO: Optional[str]
    RANGO_RCI: Optional[str]
    ESTADO_CIVIL: Optional[str]
    GENERO: Optional[str]

    veces_acepto_producto: Optional[int]
    tiempo_desde_ultima_conversion: Optional[int]
    tiempo_desde_ultima_negacion: Optional[int]
    intentos_totales: Optional[int]
    meses_gestionados: Optional[int]
    dias_ultima_gestion: Optional[int]
    ultima_gestion: Optional[str]
    veces_sin_respuesta: Optional[int]
    veces_solicitud_seguimiento: Optional[int]
    promedio_dias_entre_gestiones: Optional[float]
    max_intentos_en_un_mes: Optional[int]
    veces_respuesta_positiva: Optional[int]
    veces_respuesta_negativa: Optional[int]

    MERGE_VARIABLES: int = Field(..., alias="_merge_variables")

    class Config:
        populate_by_name = True
        extra = "allow"
