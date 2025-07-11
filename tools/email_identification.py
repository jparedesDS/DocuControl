import pandas as pd

# Añadimos los contactos de email
email_TO = ';santos-sanchez@eipsa.es;'
email_TO_CC = ';jesus-martinez@eipsa.es;ernesto-carrillo@eipsa.es;'
email_LB = ';luis-bravo@eipsa.es;'
email_AC = ';ana-calvo@eipsa.es;'
email_SS = ';sandra-sanz@eipsa.es;'
email_JV = ';jorge-valtierra@eipsa.es;'
email_CC = ';carlos-crespohor@eipsa.es;'

def email_employee(df):
    """
        Función para identificar el empleado encargado del documento

        Args:
            df (pandas.DataFrame): DataFrame que contiene el Tipo de documento pasado a la nueva columna df2['EMAIL'].

        Returns:
            pandas.DataFrame: DataFrame actualizado con los tipos de documento indicándonos quien es el responsable del documento
    """

    mapping = {'PLG': '', 'DWG': '', 'CAL': '', 'ESP': '', 'CER': email_JV, 'NACE': '', 'LIS': email_JV, 'ITP': '',
               'PRC': email_JV, 'MAN': email_JV, 'VDB': '', 'PLN': '', 'PLD': '', 'CAT': email_JV, 'DL': '', 'DOS': email_JV, 'SPL': email_JV, 'WD': '', 'DD': email_JV}

    df['EMAIL'] = df['EMAIL'].map(mapping)
    df = df['EMAIL'].apply(pd.Series)
    return df

def get_responsable_email(numero_pedido):
    """
            Función para identificar al responsable del pedido

            Args:
                df (pandas.DataFrame): DataFrame que contiene ['Nº pedido'] volcamos la columna a ['Responsable_email'] y transformamos con mapping

            Returns:
                pandas.DataFrame: DataFrame con columna ['Responsable_email'] en la que se encuentra el email del responsable del pedido
    """
    email_mapping = {'P-21/003': email_LB,
                     'P-22/001': email_LB, 'P-22/002': email_LB, 'P-22/003': email_AC, 'P-22/004': email_AC,
                     'P-22/005': email_AC, 'P-22/006': email_LB, 'P-22/007': email_LB, 'P-22/008': email_AC,
                     'P-22/009': email_LB, 'P-22/010': email_AC, 'P-22/011': email_LB, 'P-22/012': email_AC,
                     'P-22/013': email_LB, 'P-22/014': email_AC, 'P-22/015': email_LB, 'P-22/016': email_LB,
                     'P-22/017': email_AC, 'P-22/018': email_AC, 'P-22/019': email_AC, 'P-22/020': email_LB,
                     'P-22/021': email_AC, 'P-22/022': email_AC, 'P-22/023': email_AC, 'P-22/024': email_AC,
                     'P-22/025': email_LB, 'P-22/026': email_LB, 'P-22/027': email_LB, 'P-22/028': email_AC,
                     'P-22/029': email_LB, 'P-22/030': email_LB, 'P-22/031': email_AC, 'P-22/032': email_AC,
                     'P-22/033': email_LB, 'P-22/034': email_LB, 'P-22/035': email_AC, 'P-22/036': email_AC,
                     'P-22/037': email_LB, 'P-22/038': email_AC, 'P-22/039': email_AC, 'P-22/040': email_LB,
                     'P-22/041': email_LB, 'P-22/042': email_AC, 'P-22/043': email_AC, 'P-22/044': email_AC,
                     'P-22/045': email_AC, 'P-22/046': email_AC, 'P-22/047': email_SS, 'P-22/048': email_LB,
                     'P-22/049': email_LB, 'P-22/050': email_LB, 'P-22/051': email_AC, 'P-22/052': email_AC,
                     'P-22/053': email_SS, 'P-22/054': email_SS, 'P-22/055': email_AC, 'P-22/056': email_AC,
                     'P-22/057': email_AC, 'P-22/058': email_AC, 'P-22/059': email_AC, 'P-22/060': email_AC,
                     'P-22/061': email_LB, 'P-22/062': email_SS, 'P-22/063': email_SS, 'P-22/064': email_LB,
                     'P-22/065': email_AC, 'P-22/066': email_AC, 'P-22/067': email_AC, 'P-22/068': email_AC,
                     'P-22/069': email_AC, 'P-22/070': email_SS, 'P-22/071': email_AC, 'P-22/072': email_LB,
                     'P-22/073': email_AC, 'P-22/074': email_LB, 'P-22/075': email_SS, 'P-22/076': email_LB,
                     'P-22/077': email_AC, 'P-22/078': email_AC, 'P-22/079': email_AC, 'P-22/080': email_SS,
                     'P-22/081': email_AC, 'P-22/082': email_LB, 'P-22/083': email_AC, 'P-22/084': email_LB,
                     'P-22/085': email_LB, 'P-22/086': email_LB, 'P-22/087': email_LB, 'P-22/088': email_LB,
                     'P-22/089': email_LB, 'P-22/090': email_LB, 'P-22/091': email_LB, 'P-22/092': email_LB,
                     'P-22/093': email_LB, 'P-22/094': email_LB, 'P-22/095': email_LB, 'P-22/096': email_LB,
                     'P-22/097': email_LB, 'P-22/098': email_LB, 'P-22/099': email_LB, 'P-22/100': email_LB,
                     'P-22/101': email_LB, 'P-22/102': email_LB, 'P-22/103': email_LB, 'P-22/104': email_LB,
                     'P-22/105': email_LB,
                     'P-23/001': email_LB, 'P-23/002': email_LB, 'P-23/003': email_LB, 'P-23/004': email_AC,
                     'P-23/005': email_AC, 'P-23/006': email_AC, 'P-23/007': email_LB, 'P-23/008': email_AC,
                     'P-23/009': email_AC, 'P-23/010': email_AC, 'P-23/011': email_SS, 'P-23/012': email_AC,
                     'P-23/013': email_LB, 'P-23/014': email_SS, 'P-23/015': email_AC, 'P-23/016': email_AC,
                     'P-23/017': email_SS, 'P-23/018': email_AC, 'P-23/019': email_LB, 'P-23/020': email_AC,
                     'P-23/021': email_LB, 'P-23/022': email_LB, 'P-23/023': email_AC, 'P-23/024': email_LB,
                     'P-23/025': email_LB, 'P-23/026': email_SS, 'P-23/027': email_LB, 'P-23/028': email_LB,
                     'P-23/029': email_LB, 'P-23/030': email_LB, 'P-23/031': email_AC, 'P-23/032': email_AC,
                     'P-23/033': email_AC, 'P-23/034': email_SS, 'P-23/035': email_AC, 'P-23/036': email_AC,
                     'P-23/037': email_LB, 'P-23/038': email_LB, 'P-23/039': email_LB, 'P-23/040': email_AC,
                     'P-23/041': email_AC, 'P-23/042': email_LB, 'P-23/043': email_LB, 'P-23/044': email_LB,
                     'P-23/045': email_AC, 'P-23/046': email_SS, 'P-23/047': email_AC, 'P-23/048': email_SS,
                     'P-23/049': email_LB, 'P-23/050': email_LB, 'P-23/051': email_AC, 'P-23/052': email_AC,
                     'P-23/053': email_AC, 'P-23/054': email_AC, 'P-23/055': email_AC, 'P-23/056': email_SS,
                     'P-23/057': email_LB, 'P-23/058': email_AC, 'P-23/059': email_LB, 'P-23/060': email_AC,
                     'P-23/061': email_LB, 'P-23/062': email_AC, 'P-23/063': email_AC, 'P-23/064': email_AC,
                     'P-23/065': email_AC, 'P-23/066': email_AC, 'P-23/067': email_AC, 'P-23/068': email_AC,
                     'P-23/069': email_AC, 'P-23/070': email_AC, 'P-23/071': email_AC, 'P-23/072': email_LB,
                     'P-23/073': email_AC, 'P-23/074': email_SS, 'P-23/075': email_LB, 'P-23/076': email_LB,
                     'P-23/077': email_AC, 'P-23/078': email_AC, 'P-23/079': email_LB, 'P-23/080': email_AC,
                     'P-23/081': email_AC, 'P-23/082': email_AC, 'P-23/083': email_AC, 'P-23/084': email_AC,
                     'P-23/085': email_AC, 'P-23/086': email_AC, 'P-23/087': email_AC, 'P-23/088': email_AC,
                     'P-23/089': email_SS, 'P-23/090': email_AC, 'P-23/091': email_AC, 'P-23/092': email_LB,
                     'P-23/093': email_AC, 'P-23/094': email_LB, 'P-23/095': email_AC, 'P-23/096': email_AC,
                     'P-23/097': email_AC, 'P-23/098': email_LB, 'P-23/099': email_LB, 'P-23/100': email_AC,
                     'P-23/101': email_AC, 'P-23/102': email_AC, 'P-23/103': email_LB, 'P-23/104': email_AC,
                     'P-23/105': email_SS, 'P-24/001': email_LB, 'P-24/002': email_LB, 'P-24/003': email_LB,
                     'P-24/004': email_AC, 'P-24/005': email_AC, 'P-24/006': email_AC, 'P-24/007': email_AC,
                     'P-24/008': email_AC, 'P-24/009': email_AC, 'P-24/010': email_AC, 'P-24/011': email_AC,
                     'P-24/012': email_SS, 'P-24/013': email_AC, 'P-24/014': email_AC, 'P-24/015': email_SS,
                     'P-24/016': email_AC, 'P-24/017': email_AC, 'P-24/018': email_AC, 'P-24/019': email_AC,
                     'P-24/020': email_AC, 'P-24/021': email_AC, 'P-24/022': email_AC, 'P-24/023': email_AC,
                     'P-24/024': email_AC, 'P-24/025': email_AC, 'P-24/026': email_AC, 'P-24/027': email_AC,
                     'P-24/028': email_AC, 'P-24/029': email_AC, 'P-24/030': email_AC, 'P-24/031': email_AC,
                     'P-24/032': email_AC, 'P-24/033': email_AC, 'P-24/034': email_AC, 'P-24/035': email_AC,
                     'P-24/036': email_AC, 'P-24/037': email_AC, 'P-24/038': email_AC, 'P-24/039': email_AC,
                     'P-24/040': email_AC, 'P-24/041': email_AC, 'P-24/042': email_AC, 'P-24/043': email_AC,
                     'P-24/044': email_AC, 'P-24/045': email_AC, 'P-24/046': email_AC, 'P-24/047': email_AC,
                     'P-24/048': email_AC, 'P-24/049': email_AC, 'P-24/050': email_AC, 'P-24/051': email_AC,
                     'P-24/052': email_AC, 'P-24/053': email_AC, 'P-24/054': email_AC, 'P-24/055': email_AC,
                     'P-24/056': email_AC, 'P-24/057': email_AC, 'P-24/058': email_AC, 'P-24/059': email_AC,
                     'P-24/060': email_AC, 'P-24/061': email_AC, 'P-24/062': email_AC, 'P-24/063': email_AC,
                     'P-24/064': email_AC, 'P-24/065': email_AC, 'P-24/066': email_LB, 'P-24/067': email_AC,
                     'P-24/068': email_AC, 'P-24/069': email_LB, 'P-24/070': email_LB, 'P-24/071': email_AC,
                     'P-24/072': email_AC, 'P-24/073': email_AC, 'P-24/074': email_AC, 'P-24/075': email_AC,
                     'P-24/076': email_AC, 'P-24/077': email_AC, 'P-24/078': email_AC, 'P-24/079': email_SS,
                     'P-24/080': email_SS, 'P-24/081': email_AC, 'P-24/082': email_AC, 'P-24/083': email_AC,
                     'P-24/084': email_AC, 'P-24/085': email_LB, 'P-24/086': email_CC, 'P-24/087': email_AC,
                     'P-24/088': email_AC, 'P-24/089': email_AC, 'P-24/090': email_AC, 'P-24/091': email_AC,
                     'P-24/092': email_SS, 'P-24/093': email_LB, 'P-24/094': email_LB, 'P-24/095': email_AC,
                     'P-24/096': email_CC, 'P-24/097': email_AC, 'P-24/098': email_CC, 'P-24/099': email_CC,
                     'P-24/100': email_SS, 'P-25/001': email_AC, 'P-25/002': email_AC, 'P-25/003': email_SS,
                     'P-25/004': email_AC, 'P-25/005': email_SS, 'P-25/006': email_CC, 'P-25/007': email_SS,
                     'P-25/008': email_AC, 'P-25/009': email_AC, 'P-25/010': email_AC, 'P-25/011': email_AC,
                     'P-25/012': email_AC, 'P-25/013': email_AC, 'P-25/014': email_AC, 'P-25/015': email_SS,
                     'P-25/016': email_AC, 'P-25/017': email_AC, 'P-25/018': email_AC, 'P-25/019': email_CC,
                     'P-25/020': email_AC, 'P-25/021': email_AC, 'P-25/022': email_AC, 'P-25/023': email_SS,
                     'P-25/024': email_SS, 'P-25/025': email_AC, 'P-25/026': email_LB, 'P-25/027': email_LB,
                     'P-25/028': email_LB, 'P-25/029': email_AC, 'P-25/030': email_SS, 'P-25/031': email_SS,
                     'P-25/032': email_AC, 'P-25/033': email_AC, 'P-25/034': email_CC, 'P-25/035': email_AC, }

    for key in email_mapping:
        if key in numero_pedido:
            return email_mapping[key]

    return None
