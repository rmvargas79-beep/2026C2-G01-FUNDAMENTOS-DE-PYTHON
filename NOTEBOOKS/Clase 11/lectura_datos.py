"""Módulo para leer la tabla de tipos de cambio del BCCR."""

import pandas as pd


URL_BCCR = (
    "https://gee.bccr.fi.cr/IndicadoresEconomicos/Cuadros/"
    "frmConsultaTCVentanilla.aspx"
)


def cargar_tabla_bccr(fuente=URL_BCCR):
    """Carga la tabla cruda del BCCR desde una dirección web o un HTML."""
    # TODO 1: use pd.read_html con fuente, encoding, decimal y thousands.
    # TODO 2: seleccione la tabla de índice 2 y devuelva una copia.
    #
    # Mientras completa ambos pasos, la función devuelve un DataFrame vacío
    # para que el proyecto pueda ejecutarse sin producir un error de sintaxis.
    return pd.DataFrame()
