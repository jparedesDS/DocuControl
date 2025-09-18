import re
import numpy as np
import pandas as pd

#ALL
def identificar_cliente_por_PO(df):
    """
    Función para identificar el cliente a través del número de pedido (PO) utilizando expresiones regulares.

    Args:
        df (pandas.DataFrame): DataFrame que contiene la columna 'PO'.

    Returns:
        pandas.DataFrame: DataFrame actualizado con la columna 'Cliente' identificada.
    """
    # mapping (dict): Diccionario de mapeo para identificar el cliente según el número de pedido.
    mapping = {'21472': 'TECHNIP/SYNKEDIA',
               '10121': 'DUQM', '10150': 'BAPCO',
               '10160': 'CRISP', '10230': 'MARJAN',
               '10318': 'RAS TANURA', '10330': 'NEW PTA COMPLEX',
               '10370': 'QATAR EPC3', '10380': 'YPF',
               '10400': 'ADNOC DALMA', '10430': 'QATAR EPC4',
               '23222': 'CQP', '23262': 'Certificado',
               '33138': 'DUQM', '70150': 'SEWA',
               '70215': 'CFE MERIDA', '70225': 'C.C. VALLADOLID',
               '70230': 'C.C. GONZALEZ ORTEGA', '70240': 'C.C. SAN LUIS',
               '80057': 'BU HASA', '80091': 'T.R. ENAP',
               '19085': 'CEPSA/T.R.', '30011': 'BP OIL ESPAÑA',
               '75001': 'TECNIMONT', '60001': 'CEPSA WOOD',
               '70112': 'CEPSA SAN ROQUE', '70801': 'CEPSA',
               '15282': 'ASTCOR', 'T.206': 'REPSOL PETRÓLEO',
               'BP-T2': 'CNTCC', 'EP24I': 'ALMARAZ/TRILLO',
               '49000': 'JIGPC/ARAMCO', 'PO 15': 'ASTCOR',
               'Q3710': 'INTECSA INDUSTRIAL', 'RFQ 1': 'BU HASA',
               '70292': 'LECTA', 'APEIS': 'KNPC',
               '***': 'CEPSA/AYESA', '30012': 'BP OIL REFINERIA',
               'EC24T': 'ALMARAZ/TRILLO', '10735': 'SULZER',
               '70700': 'CEPSA/WOOD', 'JUS&I': 'ARAMCO/HYUNDAI',
               '70113': 'CEPSA', '10620': 'QATARBOP/TR',
               'ADI-29': 'TECHNIP/SYNKEDIA', '10431': 'QATAREPC4/TR',
               'PO P7': 'TECHNIP/REPSOL', '12574': 'ALPARGATA',
               'ADI-2': 'TECHNIP/SYNKEDIA', '23000': 'TECHNIP/GALP',
               '45077': 'ARAMCO PORTAL', '45000': 'AYESA/REPSOL',
               '30015': 'BP OIL ESPAÑA', '19162': 'WISON/ARAMCO',
               '48550': 'WISON/ARAMCO', '20175': 'TECHNIP/REPSOL',
               'QR-DD': 'ASTCOR/WOOD', 'RFPP-': 'IDOM/REPSOL',
               '10120': 'TR/DUQM', 'SOCAR': 'SOCAR/EMERSON',
               '41650': 'SOCAR/EMERSON', 'P-P0C': 'SACYR/REPSOL',
               'SEG/B': 'SINOPEC/ARAMCO', 'SEG /': 'SINOPEC/ARAMCO',
               '10651': 'ARAMCO/RIYAS', '45124': 'ADNOC/YOKOGAWA',
               'O-23/': 'SINES/YOKOGAWA', 'O-24/': 'SENER/GATE',
               'GAT22': 'SENER/GATE', '45126': 'ADNOC/YOKOGAWA',
               'POPRI': 'REPSOL', '06000': 'CEPSA','5040-': 'MEDGAZ',
               'PO 45': 'ARAMCO', 'E2404': 'SENYANG', '5061-': 'MEDGAZ',
               '60002': 'MOEVE', 'TR-19': 'MOEVE', '19128': 'MOEVE',
               'D2632': 'MOEVE', 'D22471': 'MOEVE', '44000': 'PETRONASH',
               'PE-47': 'TECMACO'}

    # Definir la expresión regular para extraer los primeros 5 dígitos del número de pedido (PO)
    regex_pattern = r'^(\d{5})'

    # Aplicar la expresión regular para extraer los primeros 5 dígitos del PO y mapear el cliente
    df['Cliente'] = df['PO'].apply(lambda x: mapping[re.match(regex_pattern, x).group(1)] if re.match(regex_pattern, x) else '')

    return df

# MONITORING REPORT
def identificar_cliente_por_PO_MR(df):
    """
    Función para identificar el cliente a través del número de pedido (Nº PO) utilizando expresiones regulares para MONITORING REPORT

    Args:
        df (pandas.DataFrame): DataFrame que contiene la columna 'PO'.

    Returns:
        pandas.DataFrame: DataFrame actualizado con la columna 'Cliente' identificada.
    """
    # mapping (dict): Diccionario de mapeo para identificar el cliente según el número de pedido.
    mapping = mapping = {'21472': 'TECHNIP/SYNKEDIA',
               '10121': 'DUQM', '10150': 'BAPCO',
               '10160': 'CRISP', '10230': 'MARJAN',
               '10318': 'RAS TANURA', '10330': 'NEW PTA COMPLEX',
               '10370': 'QATAR EPC3', '10380': 'YPF',
               '10400': 'ADNOC DALMA', '10430': 'QATAR EPC4',
               '23222': 'CQP', '23262': 'Certificado',
               '33138': 'DUQM', '70150': 'SEWA',
               '70215': 'CFE MERIDA', '70225': 'C.C. VALLADOLID',
               '70230': 'C.C. GONZALEZ ORTEGA', '70240': 'C.C. SAN LUIS',
               '80057': 'BU HASA', '80091': 'T.R. ENAP',
               '19085': 'CEPSA/T.R.', '30011': 'BP OIL ESPAÑA',
               '75001': 'TECNIMONT', '60001': 'CEPSA WOOD',
               '70112': 'CEPSA SAN ROQUE', '70801': 'CEPSA',
               '15282': 'ASTCOR', 'T.206': 'REPSOL PETRÓLEO',
               'BP-T2': 'CNTCC', 'EP24I': 'ALMARAZ/TRILLO',
               '49000': 'JIGPC/ARAMCO', 'PO 15': 'ASTCOR',
               'Q3710': 'INTECSA INDUSTRIAL', 'RFQ 1': 'BU HASA',
               '70292': 'LECTA', 'APEIS': 'KNPC',
               '***': 'CEPSA/AYESA', '30012': 'BP OIL REFINERIA',
               'EC24T': 'ALMARAZ/TRILLO', '10735': 'SULZER',
               '70700': 'CEPSA/WOOD', 'JUS&I': 'ARAMCO/HYUNDAI',
               '70113': 'CEPSA', '10620': 'QATARBOP/TR',
               'ADI-29': 'TECHNIP/SYNKEDIA', '10431': 'QATAREPC4/TR',
               'PO P7': 'TECHNIP/REPSOL', '12574': 'ALPARGATA',
               'ADI-2': 'TECHNIP/SYNKEDIA', '23000': 'TECHNIP/GALP',
               '45077': 'ARAMCO PORTAL', '45000': 'AYESA/REPSOL',
               '30015': 'BP OIL ESPAÑA', '19162': 'WISON/ARAMCO',
               '48550': 'WISON/ARAMCO', '20175': 'TECHNIP/REPSOL',
               'QR-DD': 'ASTCOR/WOOD', 'RFPP-': 'IDOM/REPSOL',
               '10120': 'TR/DUQM', 'SOCAR': 'SOCAR/EMERSON',
               '41650': 'SOCAR/EMERSON', 'P-P0C': 'SACYR/REPSOL',
               'SEG/B': 'SINOPEC/ARAMCO', 'SEG /': 'SINOPEC/ARAMCO',
               '10651': 'ARAMCO/RIYAS', '45124': 'ADNOC/YOKOGAWA',
               'O-23/': 'SINES/YOKOGAWA', 'O-24/': 'SENER/GATE',
               'GAT22': 'SENER/GATE', '45126': 'ADNOC/YOKOGAWA',
               'POPRI': 'REPSOL', '06000': 'CEPSA','5040-': 'MEDGAZ',
               'PO 45': 'ARAMCO', 'E2404': 'SENYANG', '5061-': 'MEDGAZ',
               '60002': 'MOEVE', 'TR-19': 'MOEVE', '19128': 'MOEVE',
               'D2632': 'MOEVE', 'D22471': 'MOEVE', '44000': 'PETRONASH',
               'PE-47': 'TECMACO'}

    # Definir la expresión regular para extraer los primeros 5 dígitos del número de pedido (PO)
    df['Cliente'] = df['Nº PO'].apply(str)

    # Aplicar la expresión regular para extraer los primeros 5 dígitos del PO y mapear el cliente
    df['Cliente'] = df['Cliente'].str[:5].map(mapping)
    return df


# PRODOC / WOOD
def identificar_cliente_por_PO_PRODOC(df):
    """
    Función para identificar el cliente a través del número de pedido (PO) utilizando expresiones regulares.

    Args:
        df (pandas.DataFrame): DataFrame que contiene la columna 'PO'.

    Returns:
        pandas.DataFrame: DataFrame actualizado con la columna 'Cliente' identificada.
    """
    # mapping (dict): Diccionario de mapeo para identificar el cliente según el número de pedido.
    mapping = {'21472': 'TECHNIP/SYNKEDIA',
               '10121': 'DUQM', '10150': 'BAPCO',
               '10160': 'CRISP', '10230': 'MARJAN',
               '10318': 'RAS TANURA', '10330': 'NEW PTA COMPLEX',
               '10370': 'QATAR EPC3', '10380': 'YPF',
               '10400': 'ADNOC DALMA', '10430': 'QATAR EPC4',
               '23222': 'CQP', '23262': 'Certificado',
               '33138': 'DUQM', '70150': 'SEWA',
               '70215': 'CFE MERIDA', '70225': 'C.C. VALLADOLID',
               '70230': 'C.C. GONZALEZ ORTEGA', '70240': 'C.C. SAN LUIS',
               '80057': 'BU HASA', '80091': 'T.R. ENAP',
               '19085': 'CEPSA/T.R.', '30011': 'BP OIL ESPAÑA',
               '75001': 'TECNIMONT', '60001': 'CEPSA WOOD',
               '70112': 'CEPSA SAN ROQUE', '70801': 'CEPSA',
               '15282': 'ASTCOR', 'T.206': 'REPSOL PETRÓLEO',
               'BP-T2': 'CNTCC', 'EP24I': 'ALMARAZ/TRILLO',
               '49000': 'JIGPC/ARAMCO', 'PO 15': 'ASTCOR',
               'Q3710': 'INTECSA INDUSTRIAL', 'RFQ 1': 'BU HASA',
               '70292': 'LECTA', 'APEIS': 'KNPC',
               '***': 'CEPSA/AYESA', '30012': 'BP OIL REFINERIA',
               'EC24T': 'ALMARAZ/TRILLO', '10735': 'SULZER',
               '70700': 'CEPSA/WOOD', 'JUS&I': 'ARAMCO/HYUNDAI',
               '70113': 'CEPSA', '10620': 'QATARBOP/TR',
               'ADI-29': 'TECHNIP/SYNKEDIA', '10431': 'QATAREPC4/TR',
               'PO P7': 'TECHNIP/REPSOL', '12574': 'ALPARGATA',
               'ADI-2': 'TECHNIP/SYNKEDIA', '23000': 'TECHNIP/GALP',
               '45077': 'ARAMCO PORTAL', '45000': 'AYESA/REPSOL',
               '30015': 'BP OIL ESPAÑA', '19162': 'WISON/ARAMCO',
               '48550': 'WISON/ARAMCO', '20175': 'TECHNIP/REPSOL',
               'QR-DD': 'ASTCOR/WOOD', 'RFPP-': 'IDOM/REPSOL',
               '10120': 'TR/DUQM', 'SOCAR': 'SOCAR/EMERSON',
               '41650': 'SOCAR/EMERSON', 'P-P0C': 'SACYR/REPSOL',
               'SEG/B': 'SINOPEC/ARAMCO', 'SEG /': 'SINOPEC/ARAMCO',
               '10651': 'ARAMCO/RIYAS', '45124': 'ADNOC/YOKOGAWA',
               'O-23/': 'SINES/YOKOGAWA', 'O-24/': 'SENER/GATE',
               'GAT22': 'SENER/GATE', '45126': 'ADNOC/YOKOGAWA',
               'POPRI': 'REPSOL', '06000': 'CEPSA', '5040-': 'MEDGAZ',
               'PO 45': 'ARAMCO', 'E2404': 'SENYANG', '5061-': 'MEDGAZ',
               '60002': 'MOEVE', 'TR-19': 'MOEVE', '19128': 'MOEVE',
               'D2632': 'MOEVE', 'D22471': 'MOEVE', '44000': 'PETRONASH',
               'PE-47': 'TECMACO'}

    # Definir la expresión regular para extraer los primeros 5 dígitos del número de pedido (PO)
    regex_pattern = r'^(\d{5})'

    # Aplicar la expresión regular para extraer los primeros 5 dígitos del PO y mapear el cliente
    df['Cliente'] = df['P.O.'].apply(lambda x: mapping[re.match(regex_pattern, x).group(1)] if re.match(regex_pattern, x) else '')

    return df