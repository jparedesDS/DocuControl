import re
import numpy as np
import pandas as pd

def reconocer_tipo_proyecto(df):
    """
    Reconoce el tipo de proyecto basado en el número de pedido ('PO') y lo asigna a la columna 'Material'.

    Args:
        df (pandas.DataFrame): DataFrame que contiene la columna 'PO'.

    Returns:
        pandas.DataFrame: DataFrame actualizado con la columna 'Material' indicando el tipo de proyecto.
    """
    mapping = {'214726C': 'CAUDAL', '7070000087': 'TEMPERATURA',
               }

    # Asignamos el tipo de proyecto según el número de pedido
    df['Material'] = df['PO'].map(mapping).fillna(df['PO'])  # Si no se encuentra en el mapeo, deja el código original

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
               'ITP': 'PPI', 'PRC': 'Procedimientos',
               'MAN': 'Manual', 'VDB': 'Listado',
               'PLN': 'PPI', 'PLD': 'Nameplate',
               'CAT': 'Catalogo', 'DL': 'Listado',
               'SPL': 'Repuestos', 'WD': 'Soldadura',
               'VDDL': 'Listado', 'IND': 'Indice',
               'NDE': 'Procedimientos', 'PH': 'Procedimientos',
               'DD': 'Dossier'}

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
               'Repuestos': 'No',
               'Indice': 'No'}

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
        'Code 1': 'Com. Mayores',
        'Code 2': 'Com. Menores',
        'Code 3': 'Aprobado',
        'Code 4': 'Informativo',
        'Code 5': 'Rechazado'}

    # Aplicar el mapeo para cambiar el tipo de estado en la columna 'Return Status'
    df['Estado'] = df['Estado'].map(mapping)

    return df

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