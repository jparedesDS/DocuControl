import re
import numpy as np
import pandas as pd

def reemplazar_null(df):
    """
        Esta función toma un DataFrame como entrada y reemplaza los valores de la columna "Suplemento" de acuerdo con el mapeo proporcionado en el diccionario mapping

        Args:
            df (pandas.DataFrame): DataFrame que contiene "NULOS".

        Returns:
            pandas.DataFrame: DataFrame actualizado, si el valor no se encuentra en el mapeo o es NaN, se reemplaza con 'S00'.
    """
    mapping = {np.nan: 'S00', 'S01': 'S01', 'S02': 'S02', 'S03': 'S03',
               'S04': 'S04', 'S05': 'S05', 'S06': 'S06', 'S07': 'S07'}
    df['Supp.'] = df['Supp.'].map(mapping).fillna('S00')
    return df

def reconocer_tipo_proyecto(df):
    """
    Función para reconocer los 3 últimos números y modificar la columna 'TIPO' indicando qué tipo de proyecto es.

    Args:
        df (pandas.DataFrame): DataFrame que contiene la columna 'Material'.

    Returns:
        pandas.DataFrame: DataFrame actualizado con la columna 'Material' modificada.
    """
    # mapping (dict): Diccionario de mapeo para identificar el tipo de proyecto.
    mapping = {'411': 'TEMPERATURA', '412': 'TEMPERATURA',
               '610': 'BIMETÁLICOS', '640': 'TEMPERATURA',
               '710': 'NIVEL VIDRIO', '740': 'TUBERÍAS',
               '910': 'CAUDAL', '911': 'SALTOS MULTIPLES',
               '920': 'ORIFICIOS'}

    # Extraemos
    df['Material'] = df['PO'].str.extract(r'(\d{3}+\Z)', expand=False)

    # Reconocer los 3 últimos números y modifica la columna 'Material' usando el mapeo proporcionado
    df['Material'] = df['Material'].str[-3:].map(mapping)

    return df

def procesar_documento_y_fecha(df, receivedtime):
    """
    Función para cambiar el tipo de documento a entero y añadir la hora exacta recibida del email.

    Args:
        df (pandas.DataFrame): DataFrame que contiene las columnas 'Tipo de documento' y 'Fecha'.
        receivedtime (datetime): Hora exacta recibida del email.

    Returns:
        pandas.DataFrame: DataFrame actualizado con el tipo de documento cambiado a entero y la hora exacta añadida.
    """
    # mapping (dict): Diccionario de mapeo para identificar el tipo de documento
    mapping = {'PLG': 'Planos', 'DWG': 'Planos',
               'CAL': 'Cálculos', 'ESP': 'Cálculos y Planos',
               'CER': 'Certificado', 'NACE': 'Certificado',
               'DOS': 'Dossier', 'LIS': 'Listado',
               'ITP': 'Procedimientos', 'PRC': 'Procedimientos',
               'MAN': 'Manual', 'VDB': 'Listado',
               'PLN': 'PPI', 'PLD': 'Nameplate',
               'CAT': 'Catalogo', 'DL': 'Listado'}

    # Cambiar el tipo de documento usando el mapeo proporcionado
    df['Tipo de documento'] = df['Tipo de documento'].map(mapping)

    # Convertir la hora exacta recibida del email a formato de fecha y hora
    df['Fecha'] = pd.to_datetime(receivedtime, dayfirst=True)

    return df

def critico(df):
    """
    Función para cambiar el tipo de estado en un DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame que contiene la columna 'Return Status'.

    Returns:
        pandas.DataFrame: DataFrame actualizado con los tipos de estado modificados.
    """

    # mapping (dict): Diccionario de mapeo para identificar el estado del documento
    mapping = {'Planos': 'Sí',
               'Cálculos': 'Sí', 'Cálculos y Planos': 'Sí',
               'Certificado': 'No',
               'Dossier': 'No',
               'Procedimientos': 'No',
               'Manual': 'Sí',
               'PPI': 'Sí', 'Nameplate': 'No',
               'Catalogo': 'Sí', 'Listado': 'Sí',
               'Repuestos': 'No'}

    # Aplicar el mapeo para cambiar el tipo de estado en la columna 'Return Status'
    df['Crítico'] = df['Tipo de documento'].map(mapping)

    return df

def cambiar_tipo_estado(df):
    """
    Función para cambiar el tipo de estado en un DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame que contiene la columna 'Return Status'.

    Returns:
        pandas.DataFrame: DataFrame actualizado con los tipos de estado modificados.
    """

    # mapping (dict): Diccionario de mapeo para identificar el estado del documento
    mapping = {
        'A - REJECTED': 'Rechazado',
        'B - REVIEWED WITH MAJOR COMMENTS': 'Com. Mayores',
        'C - REVIEWED WITH MINOR COMMENTS': 'Com. Menores',
        'F - REVIEWED WITHOUT COMMENTS': 'Aprobado',
        'W - ISSUED FOR CERTIFICATION': 'Certificación',
        'M - VOID': 'Eliminado'}

    # Aplicar el mapeo para cambiar el tipo de estado en la columna 'Return Status'
    df['Return Status'] = df['Return Status'].map(mapping)

    return df