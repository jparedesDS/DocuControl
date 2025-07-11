# Imports
import numpy as np
import pandas as pd

def apply_reclamaciones(df):

    mapping = {'5022_20-1043010910-00018': 2, 'V-23Q8LA02A-2206-3000-PAFE0165N-DWG-001': 3,
               'V-23Q8LA02A-2206-3000-PAFE0735-DWG-001': 1, 'V-23Q8LA02A-2206-3000-PAFE0710-DWG-001': 1,
               'V-23Q8LA02A-2206-3000-PAFE0703-DWG-001': 1, 'VD-CI0021-010': 2,
               '3998_18-1037010710-00025': 2, '3998_18-1037010710-00002': 2,
               'VD-CI0021-025': 1, 'V-23BLFE01A-2206-400-10TE1502-CAL-001': 1,
               'VD-CI0021-008': 1, 'V-23BLFE01A-2206-400-10TE1501-CAL-001': 1,
               'V-23BLFE01A-2206-400-15TE1510-CAL-001': 1, 'V-23BLFE01A-2206-400-15TE1510-DWG-001': 1,
               'V-1040010640-0028': 1, 'V-1040010640-0026': 1,
               'V-1040010640-0003': 1, '3998_18-1037010640-00022': 2,
               '3998_18-1037010640-00020': 2, '3998_18-1037010640-00015': 1,
               '3998_18-1037010640-00029': 1, 'VD-CI0021-014': 1,
               'VD-CI0021-003': 2, 'VD-CI0021-006': 2,
               'VD-CI0021-019': 2, 'VD-CI0021-007': 2,
               'VD-CI0021-002': 2, 'VD-CI0021-017': 2,
               'VD-CI0021-001': 1,
               '5022_20-1043010710-00004': 2, '3998_18-1062010640-00015': 1,
               '3998_18-1062010910-00009': 1, '3998_18-1062010910-00006': 1,
               '3998_18-1062010910-00013': 1, '3998_18-1062010910-00001': 2,
               '3998_18-1062010910-00002': 2, 'P-24-089-DWG_R0': 1,
               '3998_18-1037010910-00002': 1, '5022_20-1043010710-00011': 1,
               }

    # Extraemos
    df['Reclamaciones'] = df['Nº Doc. Cliente']

    # Reconocer los 3 últimos números y modifica la columna 'Material' usando el mapeo proporcionado
    df['Reclamaciones'] = df['Reclamaciones'].map(mapping).fillna(0)


# Diccionario de mapeo para la función get_responsable_email()
def apply_responsable(df):

    mapping = {'P-22/001': "LB", 'P-21/009': 'RM', 'P-21/028': 'AC', 'P-21/030': 'LB', 'P-21/038': 'RP',
                   'P-21/056': 'AC', 'P-21/057': 'LB', 'P-21/060': 'AC',
                   'P-21/039': 'AC', 'P-21/040': 'AC', 'P-21/053': 'LB', 'P-21/055': 'AC',
                   'P-21/003': "LB", 'P-22/002': "LB", 'P-22/003': "AC", 'P-22/004': "AC",
                   'P-22/005': "AC", 'P-22/006': "LB", 'P-22/007': "LB", 'P-22/008': "AC",
                   'P-22/009': "LB", 'P-22/010': "AC", 'P-22/011': "LB", 'P-22/012': "AC",
                   'P-22/013': "LB", 'P-22/014': "AC", 'P-22/015': "LB", 'P-22/016': "LB",
                   'P-22/017': "AC", 'P-22/018': "AC", 'P-22/019': "AC", 'P-22/020': "LB",
                   'P-22/021': "AC", 'P-22/022': "AC", 'P-22/023': "AC", 'P-22/024': "AC",
                   'P-22/025': "LB", 'P-22/026': "LB", 'P-22/027': "LB", 'P-22/028': "AC",
                   'P-22/029': "LB", 'P-22/030': "LB", 'P-22/031': "AC", 'P-22/032': "AC",
                   'P-22/033': "LB", 'P-22/034': "LB", 'P-22/035': "AC", 'P-22/036': "AC",
                   'P-22/037': "LB", 'P-22/038': "AC", 'P-22/039': "AC", 'P-22/040': "LB",
                   'P-22/041': "LB", 'P-22/042': "AC", 'P-22/043': "AC", 'P-22/044': "AC",
                   'P-22/045': "AC", 'P-22/046': "AC", 'P-22/047': "SS", 'P-22/048': "LB",
                   'P-22/049': "LB", 'P-22/050': "LB", 'P-22/051': "AC", 'P-22/052': "AC",
                   'P-22/053': "SS", 'P-22/054': "SS", 'P-22/055': "AC", 'P-22/056': "AC",
                   'P-22/057': "AC", 'P-22/058': "AC", 'P-22/059': "AC", 'P-22/060': "AC",
                   'P-22/061': "LB", 'P-22/062': "SS", 'P-22/063': "SS", 'P-22/064': "LB",
                   'P-22/065': "AC", 'P-22/066': "AC", 'P-22/067': "AC", 'P-22/068': "AC",
                   'P-22/069': "AC", 'P-22/070': "SS", 'P-22/071': "AC", 'P-22/072': "LB",
                   'P-22/073': "AC", 'P-22/074': "LB", 'P-22/075': "SS", 'P-22/076': "LB",
                   'P-22/077': "AC", 'P-22/078': "AC", 'P-22/079': "AC", 'P-22/080': "SS",
                   'P-22/081': "AC", 'P-22/082': "LB", 'P-22/083': "AC", 'P-22/084': "LB",
                   'P-22/085': "LB", 'P-22/086': "LB", 'P-22/087': "LB", 'P-22/088': "LB",
                   'P-22/089': "LB", 'P-22/090': "LB", 'P-22/091': "LB", 'P-22/092': "LB",
                   'P-22/093': "LB", 'P-22/094': "LB", 'P-22/095': "LB", 'P-22/096': "LB",
                   'P-22/097': "LB", 'P-22/098': "LB", 'P-22/099': "LB", 'P-22/100': "LB",
                   'P-22/101': "LB", 'P-22/102': "LB", 'P-22/103': "LB", 'P-22/104': "LB",
                   'P-22/105': "LB",
                   'P-23/001': "LB", 'P-23/002': "LB", 'P-23/003': "LB", 'P-23/004': "AC",
                   'P-23/005': "AC", 'P-23/006': "AC", 'P-23/007': "LB", 'P-23/008': "AC",
                   'P-23/009': "AC", 'P-23/010': "AC", 'P-23/011': "SS", 'P-23/012': "AC",
                   'P-23/013': "LB", 'P-23/014': "SS", 'P-23/015': "AC", 'P-23/016': "AC",
                   'P-23/017': "SS", 'P-23/018': "AC", 'P-23/019': "LB", 'P-23/020': "AC",
                   'P-23/021': "LB", 'P-23/022': "LB", 'P-23/023': "AC", 'P-23/024': "LB",
                   'P-23/025': "LB", 'P-23/026': "SS", 'P-23/027': "LB", 'P-23/028': "LB",
                   'P-23/029': "LB", 'P-23/030': "LB", 'P-23/031': "AC", 'P-23/032': "AC",
                   'P-23/033': "AC", 'P-23/034': "SS", 'P-23/035': "AC", 'P-23/036': "AC",
                   'P-23/037': "LB", 'P-23/038': "LB", 'P-23/039': "LB", 'P-23/040': "AC",
                   'P-23/041': "AC", 'P-23/042': "LB", 'P-23/043': "LB", 'P-23/044': "LB",
                   'P-23/045': "AC", 'P-23/046': "SS", 'P-23/047': "AC", 'P-23/048': "SS",
                   'P-23/049': "LB", 'P-23/050': "LB", 'P-23/051': "AC", 'P-23/052': "AC",
                   'P-23/053': "AC", 'P-23/054': "AC", 'P-23/055': "AC", 'P-23/056': "SS",
                   'P-23/057': "LB", 'P-23/058': "AC", 'P-23/059': "LB", 'P-23/060': "AC",
                   'P-23/061': "LB", 'P-23/062': "AC", 'P-23/063': "AC", 'P-23/064': "AC",
                   'P-23/065': "AC", 'P-23/066': "AC", 'P-23/067': "AC", 'P-23/068': "AC",
                   'P-23/069': "AC", 'P-23/070': "AC", 'P-23/071': "AC", 'P-23/072': "LB",
                   'P-23/073': "AC", 'P-23/074': "SS", 'P-23/075': "LB", 'P-23/076': "LB",
                   'P-23/077': "AC", 'P-23/078': "AC", 'P-23/079': "LB", 'P-23/080': "AC",
                   'P-23/081': "AC", 'P-23/082': "AC", 'P-23/083': "AC", 'P-23/084': "AC",
                   'P-23/085': "AC", 'P-23/086': "AC", 'P-23/087': "AC", 'P-23/088': "AC",
                   'P-23/089': "SS", 'P-23/090': "AC", 'P-23/091': "AC", 'P-23/092': "LB",
                   'P-23/093': "AC", 'P-23/094': "LB", 'P-23/095': "AC", 'P-23/096': "AC",
                   'P-23/097': "AC", 'P-23/098': "LB", 'P-23/099': "LB", 'P-23/100': "AC",
                   'P-23/101': "AC", 'P-23/102': "AC", 'P-23/103': "LB", 'P-23/104': "AC",
                   'P-23/105': "SS", 'P-24/001': "LB", 'P-24/002': "LB", 'P-24/003': "LB",
                   'P-24/004': "AC", 'P-24/005': "AC", 'P-24/006': "AC", 'P-24/007': "AC",
                   'P-24/008': "AC", 'P-24/009': "AC", 'P-24/010': "AC", 'P-24/011': "AC",
                   'P-24/012': "SS", 'P-24/013': "AC", 'P-24/014': "AC", 'P-24/015': "SS",
                   'P-24/016': "AC", 'P-24/017': "AC", 'P-24/018': "AC", 'P-24/019': "AC",
                   'P-24/020': "AC", 'P-24/021': "AC", 'P-24/022': "AC", 'P-24/023': "AC",
                   'P-24/024': "AC", 'P-24/025': "AC", 'P-24/026': "SS", 'P-24/027': "AC",
                   'P-24/028': "AC", 'P-24/029': "AC", 'P-24/030': "AC", 'P-24/031': "AC",
                   'P-24/032': "AC", 'P-24/033': "AC", 'P-24/034': "AC", 'P-24/035': "AC",
                   'P-24/036': "AC", 'P-24/037': "AC", 'P-24/038': "AC", 'P-24/039': "AC",
                   'P-24/040': "LB", 'P-24/041': "SS", 'P-24/042': "SS", 'P-24/043': "AC",
                   'P-24/044': "AC", 'P-24/045': "AC", 'P-24/046': "AC", 'P-24/047': "AC",
                   'P-24/048': "CCH", 'P-24/049': "AC", 'P-24/050': "AC", 'P-24/051': "AC",
                   'P-24/052': "AC", 'P-24/053': "AC", 'P-24/054': "AC", 'P-24/055': "AC",
                   'P-24/056': "AC", 'P-24/057': "AC", 'P-24/058': "AC", 'P-24/059': "AC",
                   'P-24/060': "AC", 'P-24/061': "AC", 'P-24/062': "AC", 'P-24/063': "AC",
                   'P-24/064': "AC", 'P-24/065': "AC", 'P-24/066': "LB", 'P-24/067': "AC",
                   'P-24/068': "AC", 'P-24/069': "LB", 'P-24/070': "LB", 'P-24/071': "AC",
                   'P-24/072': "AC", 'P-24/073': "AC", 'P-24/074': "AC", 'P-24/075': "AC",
                   'P-24/076': "AC", 'P-24/077': "AC", 'P-24/078': "AC", 'P-24/079': "SS",
                   'P-24/080': "SS", 'P-24/081': "AC", 'P-24/082': "AC", 'P-24/083': "AC",
                   'P-24/084': "AC", 'P-24/085': "LB", 'P-24/086': "CC", 'P-24/087': "AC",
                   'P-24/088': "AC", 'P-24/089': "AC", 'P-24/090': "AC", 'P-24/091': "AC",
                   'P-24/092': 'SS', 'P-24/093': 'LB', 'P-24/094': 'LB', 'P-24/095': 'AC',
                   'P-24/096': 'CC', 'P-24/097': 'AC', 'P-24/098': 'CC', 'P-24/099': 'CC',
                   'P-24/100': 'SS', 'P-25/001': "AC", 'P-25/002': "AC", 'P-25/003': "SS",
                   'P-25/004': "AC", 'P-25/005': "SS", 'P-25/006': "CC", 'P-25/007': "SS",
                   'P-25/008': "AC", 'P-25/009': "AC", 'P-25/010': "AC", 'P-25/011': "AC",
                   'P-25/012': "SS", 'P-25/013': "AC", 'P-25/014': "AC", 'P-25/015': "SS",
                   'P-25/016': "AC", 'P-25/017': "AC", 'P-25/018': "AC", 'P-25/019': "CC",
                   'P-25/020': "AC", 'P-25/021': "AC", 'P-25/022': "AC", 'P-25/023': "SS",
                   'P-25/024': "SS", 'P-25/025': "SS", 'P-25/026': "LB", 'P-25/027': "LB",
                   'P-25/028': "LB", 'P-25/029': "AC", 'P-25/030': "SS", 'P-25/031': "SS",
                   'P-25/032': "AC", 'P-25/033': "AC", 'P-25/034': "AC", 'P-25/035': "AC",}
    # Extraemos
    df['Resp.'] = df['Nº Pedido']

    # Reconocer los 3 últimos números y modifica la columna 'Material' usando el mapeo proporcionado
    df['Resp.'] = df['Resp.'].str[:8].map(mapping)


def process_vddl(df):

    mapping = {
        'P-22/001-S00': '', 'P-22/002-S00': '', 'P-22/003-S00': '', 'P-22/004-S00': '', 'P-22/005-S00': '',
        'P-22/006-S00': '', 'P-22/007-S00': '', 'P-22/008-S00': '', 'P-22/009-S00': '', 'P-22/010-S00': '',
        'P-22/011-S00': '', 'P-22/012-S00': '', 'P-22/013-S00': '', 'P-22/014-S00': '', 'P-22/015-S00': '',
        'P-22/016-S00': '', 'P-22/017-S00': '', 'P-22/018-S00': '', 'P-22/019-S00': '', 'P-22/020-S00': '',
        'P-22/021-S00': '', 'P-22/022-S00': '', 'P-22/023-S00': '', 'P-22/024-S00': '', 'P-22/025-S00': '',
        'P-22/026-S00': '', 'P-22/027-S00': '', 'P-22/028-S00': '', 'P-22/029-S00': '', 'P-22/030-S00': '',
        'P-22/031-S00': '', 'P-22/032-S00': '', 'P-22/033-S00': '', 'P-22/034-S00': '', 'P-22/035-S00': '',
        'P-22/036-S00': '', 'P-22/037-S00': '', 'P-22/038-S00': '', 'P-22/039-S00': '', 'P-22/040-S00': '',
        'P-22/041-S00': '', 'P-22/042-S00': '', 'P-22/043-S00': '', 'P-22/044-S00': '', 'P-22/045-S00': '',
        'P-22/046-S00': '', 'P-22/047-S00': '', 'P-22/048-S00': '', 'P-22/049-S00': '', 'P-22/050-S00': '',
        'P-22/051-S00': '', 'P-22/052-S00': '', 'P-22/053-S00': '', 'P-22/054-S00': '', 'P-22/055-S00': '',
        'P-22/056-S00': '', 'P-22/057-S00': '', 'P-22/058-S00': '', 'P-22/059-S00': '', 'P-22/060-S00': '',
        'P-22/061-S00': '', 'P-22/062-S00': '', 'P-22/063-S00': '', 'P-22/064-S00': '', 'P-22/065-S00': '',
        'P-22/066-S00': '', 'P-22/067-S00': '', 'P-22/068-S00': '', 'P-22/069-S00': '', 'P-22/070-S00': '',
        'P-22/071-S00': '', 'P-22/072-S00': '', 'P-22/073-S00': '', 'P-22/074-S00': '22-11-2023', 'P-22/075-S00': '',
        'P-22/076-S00': '', 'P-22/077-S00': '', 'P-22/078-S00': '', 'P-22/079-S00': '', 'P-22/080-S00': '',
        'P-22/081-S00': '', 'P-22/082-S00': '', 'P-22/083-S00': '', 'P-22/084-S00': '', 'P-22/085-S00': '',
        'P-22/086-S00': '', 'P-22/087-S00': '', 'P-22/088-S00': '', 'P-22/089-S00': '', 'P-22/090-S00': '',
        'P-22/091-S00': '', 'P-22/092-S00': '', 'P-22/093-S00': '', 'P-22/094-S00': '', 'P-22/095-S00': '',
        'P-22/096-S00': '', 'P-22/097-S00': '', 'P-22/098-S00': '', 'P-22/099-S00': '', 'P-22/100-S00': '',
        'P-22/101-S00': '', 'P-22/102-S00': '', 'P-22/103-S00': '', 'P-22/104-S00': '', 'P-22/105-S00': '',
        'P-23/001-S00': '23-01-2023', 'P-23/002-S00': '03-01-2023', 'P-23/003-S00': '05-01-2023', 'P-23/004-S00': '',
        'P-23/005-S00': '',
        'P-23/006-S00': '', 'P-23/007-S00': '', 'P-23/008-S00': '', 'P-23/009-S00': '', 'P-23/010-S00': '',
        'P-23/011-S00': '', 'P-23/012-S00': '', 'P-23/013-S00': '', 'P-23/014-S00': '', 'P-23/015-S00': '',
        'P-23/016-S00': '', 'P-23/017-S00': '', 'P-23/018-S00': '', 'P-23/019-S00': '', 'P-23/020-S00': '',
        'P-23/021-S00': '', 'P-23/022-S00': '', 'P-23/023-S00': '', 'P-23/024-S00': '', 'P-23/025-S00': '',
        'P-23/026-S00': '', 'P-23/027-S00': '14-03-2023', 'P-23/028-S00': '', 'P-23/029-S00': '', 'P-23/030-S00': '',
        'P-23/031-S00': '', 'P-23/032-S00': '', 'P-23/033-S00': '', 'P-23/034-S00': '16-06-2023', 'P-23/035-S00': '',
        'P-23/036-S00': '', 'P-23/037-S00': '', 'P-23/038-S00': '', 'P-23/039-S00': '', 'P-23/040-S00': '',
        'P-23/041-S00': '', 'P-23/042-S00': '', 'P-23/043-S00': '', 'P-23/044-S00': '04/05/2023', 'P-23/045-S00': '',
        'P-23/046-S00': '', 'P-23/047-S00': '', 'P-23/048-S00': '22/05/2023', 'P-23/049-S00': '', 'P-23/050-S00': '',
        'P-23/051-S00': '', 'P-23/052-S00': '', 'P-23/053-S00': '', 'P-23/054-S00': '', 'P-23/055-S00': '',
        'P-23/056-S00': '', 'P-23/057-S00': '', 'P-23/058-S00': '', 'P-23/059-S00': '', 'P-23/060-S00': '',
        'P-23/061-S00': '', 'P-23/062-S00': '', 'P-23/063-S00': '', 'P-23/064-S00': '', 'P-23/065-S00': '',
        'P-23/066-S00': '', 'P-23/067-S00': '', 'P-23/068-S00': '', 'P-23/069-S00': '', 'P-23/070-S00': '',
        'P-23/071-S00': '', 'P-23/072-S00': '', 'P-23/073-S00': '', 'P-23/074-S00': '07-08-2023', 'P-23/075-S00': '',
        'P-23/076-S00': '', 'P-23/077-S00': '', 'P-23/078-S00': '', 'P-23/079-S00': '', 'P-23/080-S00': '',
        'P-23/081-S00': '', 'P-23/082-S00': '', 'P-23/083-S00': '', 'P-23/084-S00': '', 'P-23/085-S00': '',
        'P-23/086-S00': '', 'P-23/087-S00': '', 'P-23/088-S00': '', 'P-23/089-S00': '', 'P-23/090-S00': '',
        'P-23/091-S00': '', 'P-23/092-S00': '', 'P-23/093-S00': '', 'P-23/094-S00': '', 'P-23/095-S00': '',
        'P-23/096-S00': '', 'P-23/097-S00': '', 'P-23/098-S00': '', 'P-23/099-S00': '', 'P-23/100-S00': '',
        'P-23/101-S00': '', 'P-23/102-S00': '', 'P-23/103-S00': '', 'P-23/104-S00': '', 'P-23/105-S00': '04-05-2023',
        'P-24/001-S00': '', 'P-24/002-S00': '', 'P-24/003-S00': '', 'P-24/004-S00': '', 'P-24/005-S00': '',
        'P-24/006-S00': '', 'P-24/007-S00': '', 'P-24/008-S00': '', 'P-24/009-S00': '', 'P-24/010-S00': '',
        'P-24/011-S00': '', 'P-24/012-S00': '', 'P-24/013-S00': '', 'P-24/014-S00': '', 'P-24/015-S00': '',
        'P-24/016-S00': '', 'P-24/017-S00': '', 'P-24/018-S00': '', 'P-24/019-S00': '', 'P-24/020-S00': '',
        'P-24/021-S00': '', 'P-24/022-S00': '', 'P-24/023-S00': '', 'P-24/024-S00': '', 'P-24/025-S00': '',
        'P-24/026-S00': '', 'P-24/027-S00': '', 'P-24/028-S00': '',
        'P-24/029-S00': '', 'P-24/030-S00': '', 'P-24/031-S00': '', 'P-24/032-S00': '', 'P-24/033-S00': '',
        'P-24/034-S00': '', 'P-24/035-S00': '', 'P-24/036-S00': '', 'P-24/037-S00': '', 'P-24/038-S00': '',
        'P-24/039-S00': '', 'P-24/040-S00': '03/06/2024', 'P-24/041-S00': '', 'P-24/042-S00': '', 'P-24/043-S00': '',
        'P-24/044-S00': '', 'P-24/045-S00': '', 'P-24/046-S00': '', 'P-24/047-S00': '', 'P-24/048-S00': '',
        'P-24/049-S00': '', 'P-24/050-S00': '', 'P-24/051-S00': '', 'P-24/052-S00': '', 'P-24/053-S00': '',
        'P-22/001-S01': '', 'P-22/002-S01': '',
        'P-22/003-S01': '', 'P-22/004-S01': '', 'P-22/005-S01': '', 'P-22/006-S01': '', 'P-22/007-S01': '',
        'P-22/008-S01': '', 'P-22/009-S01': '', 'P-22/010-S01': '', 'P-22/011-S01': '', 'P-22/012-S01': '',
        'P-22/013-S01': '', 'P-22/014-S01': '', 'P-22/015-S01': '', 'P-22/016-S01': '', 'P-22/017-S01': '',
        'P-22/018-S01': '', 'P-22/019-S01': '', 'P-22/020-S01': '', 'P-22/021-S01': '', 'P-22/022-S01': '',
        'P-22/023-S01': '', 'P-22/024-S01': '', 'P-22/025-S01': '', 'P-22/026-S01': '', 'P-22/027-S01': '',
        'P-22/028-S01': '', 'P-22/029-S01': '', 'P-22/030-S01': '', 'P-22/031-S01': '', 'P-22/032-S01': '',
        'P-22/033-S01': '', 'P-22/034-S01': '', 'P-22/035-S01': '', 'P-22/036-S01': '', 'P-22/037-S01': '',
        'P-22/038-S01': '', 'P-22/039-S01': '', 'P-22/040-S01': '', 'P-22/041-S01': '', 'P-22/042-S01': '',
        'P-22/043-S01': '', 'P-22/044-S01': '', 'P-22/045-S01': '', 'P-22/046-S01': '', 'P-22/047-S01': '',
        'P-22/048-S01': '', 'P-22/049-S01': '', 'P-22/050-S01': '', 'P-22/051-S01': '', 'P-22/052-S01': '',
        'P-22/053-S01': '', 'P-22/054-S01': '', 'P-22/055-S01': '', 'P-22/056-S01': '', 'P-22/057-S01': '',
        'P-22/058-S01': '', 'P-22/059-S01': '', 'P-22/060-S01': '', 'P-22/061-S01': '', 'P-22/062-S01': '',
        'P-22/063-S01': '', 'P-22/064-S01': '', 'P-22/065-S01': '', 'P-22/066-S01': '', 'P-22/067-S01': '',
        'P-22/068-S01': '', 'P-22/069-S01': '', 'P-22/070-S01': '', 'P-22/071-S01': '', 'P-22/072-S01': '',
        'P-22/073-S01': '', 'P-22/074-S01': '', 'P-22/075-S01': '', 'P-22/076-S01': '', 'P-22/077-S01': '',
        'P-22/078-S01': '', 'P-22/079-S01': '', 'P-22/080-S01': '', 'P-22/081-S01': '', 'P-22/082-S01': '',
        'P-22/083-S01': '', 'P-22/084-S01': '', 'P-22/085-S01': '', 'P-22/086-S01': '', 'P-22/087-S01': '',
        'P-22/088-S01': '', 'P-22/089-S01': '', 'P-22/090-S01': '', 'P-22/091-S01': '', 'P-22/092-S01': '',
        'P-22/093-S01': '', 'P-22/094-S01': '', 'P-22/095-S01': '', 'P-22/096-S01': '', 'P-22/097-S01': '',
        'P-22/098-S01': '', 'P-22/099-S01': '', 'P-22/100-S01': '', 'P-22/101-S01': '', 'P-22/102-S01': '',
        'P-22/103-S01': '', 'P-22/104-S01': '', 'P-22/105-S01': '', 'P-23/001-S01': '', 'P-23/002-S01': '',
        'P-23/003-S01': '', 'P-23/004-S01': '', 'P-23/005-S01': '', 'P-23/006-S01': '', 'P-23/007-S01': '',
        'P-23/008-S01': '', 'P-23/009-S01': '', 'P-23/010-S01': '', 'P-23/011-S01': '', 'P-23/012-S01': '',
        'P-23/013-S01': '', 'P-23/014-S01': '', 'P-23/015-S01': '', 'P-23/016-S01': '', 'P-23/017-S01': '',
        'P-23/018-S01': '', 'P-23/019-S01': '', 'P-23/020-S01': '', 'P-23/021-S01': '', 'P-23/022-S01': '',
        'P-23/023-S01': '', 'P-23/024-S01': '', 'P-23/025-S01': '', 'P-23/026-S01': '', 'P-23/027-S01': '',
        'P-23/028-S01': '', 'P-23/029-S01': '', 'P-23/030-S01': '', 'P-23/031-S01': '', 'P-23/032-S01': '',
        'P-23/033-S01': '', 'P-23/034-S01': '', 'P-23/035-S01': '', 'P-23/036-S01': '', 'P-23/037-S01': '09-02-2024',
        'P-23/038-S01': '', 'P-23/039-S01': '', 'P-23/040-S01': '', 'P-23/041-S01': '', 'P-23/042-S01': '',
        'P-23/043-S01': '', 'P-23/044-S01': '', 'P-23/045-S01': '', 'P-23/046-S01': '', 'P-23/047-S01': '',
        'P-23/048-S01': '', 'P-23/049-S01': '', 'P-23/050-S01': '', 'P-23/051-S01': '', 'P-23/052-S01': '',
        'P-23/053-S01': '', 'P-23/054-S01': '', 'P-23/055-S01': '', 'P-23/056-S01': '', 'P-23/057-S01': '',
        'P-23/058-S01': '', 'P-23/059-S01': '', 'P-23/060-S01': '', 'P-23/061-S01': '', 'P-23/062-S01': '',
        'P-23/063-S01': '', 'P-23/064-S01': '', 'P-23/065-S01': '', 'P-23/066-S01': '', 'P-23/067-S01': '',
        'P-23/068-S01': '', 'P-23/069-S01': '', 'P-23/070-S01': '', 'P-23/071-S01': '', 'P-23/072-S01': '',
        'P-23/073-S01': '', 'P-23/074-S01': '', 'P-23/075-S01': '', 'P-23/076-S01': '', 'P-23/077-S01': '',
        'P-23/078-S01': '', 'P-23/079-S01': '', 'P-23/080-S01': '', 'P-23/081-S01': '', 'P-23/082-S01': '',
        'P-23/083-S01': '', 'P-23/084-S01': '', 'P-23/085-S01': '', 'P-23/086-S01': '', 'P-23/087-S01': '',
        'P-23/088-S01': '', 'P-23/089-S01': '', 'P-23/090-S01': '', 'P-23/091-S01': '', 'P-23/092-S01': '',
        'P-23/093-S01': '', 'P-23/094-S01': '', 'P-23/095-S01': '', 'P-23/096-S01': '', 'P-23/097-S01': '',
        'P-23/098-S01': '', 'P-23/099-S01': '', 'P-23/100-S01': '', 'P-23/101-S01': '', 'P-23/102-S01': '',
        'P-23/103-S01': '', 'P-23/104-S01': '', 'P-23/105-S01': '', 'P-24/001-S01': '', 'P-24/002-S01': '',
        'P-24/003-S01': '', 'P-24/004-S01': '', 'P-24/005-S01': '', 'P-24/006-S01': '', 'P-24/007-S01': '',
        'P-24/008-S01': '', 'P-24/009-S01': '', 'P-24/010-S01': '', 'P-24/011-S01': '', 'P-24/012-S01': '',
        'P-24/013-S01': '', 'P-24/014-S01': '', 'P-24/015-S01': '', 'P-24/016-S01': '', 'P-24/017-S01': '',
        'P-24/018-S01': '', 'P-24/019-S01': '', 'P-24/020-S01': '', 'P-24/021-S01': '', 'P-24/022-S01': '',
        'P-24/023-S01': '', 'P-24/024-S01': '', 'P-24/025-S01': '', 'P-24/026-S01': '', 'P-24/027-S01': '',
        'P-24/028-S01': '',
        'P-24/029-S01': '', 'P-24/030-S01': '', 'P-24/031-S01': '', 'P-24/032-S01': '', 'P-24/033-S01': '',
        'P-24/034-S01': '', 'P-24/035-S01': '', 'P-24/036-S01': '', 'P-24/037-S01': '', 'P-24/038-S01': '',
        'P-24/039-S01': '', 'P-24/040-S01': '', 'P-24/041-S01': '', 'P-24/042-S01': '', 'P-24/043-S01': '',
        'P-24/044-S01': '', 'P-24/045-S01': '', 'P-24/046-S01': '', 'P-24/047-S01': '', 'P-24/048-S01': '',
        'P-24/049-S01': '', 'P-24/050-S01': '', 'P-24/051-S01': '', 'P-24/052-S01': '', 'P-24/053-S01': '',
        'P-22/001-S02': '', 'P-22/002-S02': '', 'P-22/003-S02': '', 'P-22/004-S02': '',
        'P-22/005-S02': '', 'P-22/006-S02': '', 'P-22/007-S02': '', 'P-22/008-S02': '', 'P-22/009-S02': '',
        'P-22/010-S02': '', 'P-22/011-S02': '', 'P-22/012-S02': '', 'P-22/013-S02': '', 'P-22/014-S02': '',
        'P-22/015-S02': '', 'P-22/016-S02': '', 'P-22/017-S02': '', 'P-22/018-S02': '', 'P-22/019-S02': '',
        'P-22/020-S02': '', 'P-22/021-S02': '', 'P-22/022-S02': '', 'P-22/023-S02': '', 'P-22/024-S02': '',
        'P-22/025-S02': '', 'P-22/026-S02': '', 'P-22/027-S02': '', 'P-22/028-S02': '', 'P-22/029-S02': '',
        'P-22/030-S02': '', 'P-22/031-S02': '', 'P-22/032-S02': '', 'P-22/033-S02': '', 'P-22/034-S02': '',
        'P-22/035-S02': '', 'P-22/036-S02': '', 'P-22/037-S02': '', 'P-22/038-S02': '', 'P-22/039-S02': '',
        'P-22/040-S02': '', 'P-22/041-S02': '', 'P-22/042-S02': '', 'P-22/043-S02': '', 'P-22/044-S02': '',
        'P-22/045-S02': '', 'P-22/046-S02': '', 'P-22/047-S02': '', 'P-22/048-S02': '', 'P-22/049-S02': '',
        'P-22/050-S02': '', 'P-22/051-S02': '', 'P-22/052-S02': '', 'P-22/053-S02': '', 'P-22/054-S02': '',
        'P-22/055-S02': '', 'P-22/056-S02': '', 'P-22/057-S02': '', 'P-22/058-S02': '', 'P-22/059-S02': '',
        'P-22/060-S02': '', 'P-22/061-S02': '', 'P-22/062-S02': '', 'P-22/063-S02': '', 'P-22/064-S02': '',
        'P-22/065-S02': '', 'P-22/066-S02': '', 'P-22/067-S02': '', 'P-22/068-S02': '', 'P-22/069-S02': '',
        'P-22/070-S02': '', 'P-22/071-S02': '', 'P-22/072-S02': '', 'P-22/073-S02': '', 'P-22/074-S02': '',
        'P-22/075-S02': '', 'P-22/076-S02': '', 'P-22/077-S02': '', 'P-22/078-S02': '', 'P-22/079-S02': '',
        'P-22/080-S02': '', 'P-22/081-S02': '', 'P-22/082-S02': '', 'P-22/083-S02': '', 'P-22/084-S02': '',
        'P-22/085-S02': '', 'P-22/086-S02': '', 'P-22/087-S02': '', 'P-22/088-S02': '', 'P-22/089-S02': '',
        'P-22/090-S02': '', 'P-22/091-S02': '', 'P-22/092-S02': '', 'P-22/093-S02': '', 'P-22/094-S02': '',
        'P-22/095-S02': '', 'P-22/096-S02': '', 'P-22/097-S02': '', 'P-22/098-S02': '', 'P-22/099-S02': '',
        'P-22/100-S02': '', 'P-22/101-S02': '', 'P-22/102-S02': '', 'P-22/103-S02': '', 'P-22/104-S02': '',
        'P-22/105-S02': '', 'P-23/001-S02': '', 'P-23/002-S02': '', 'P-23/003-S02': '', 'P-23/004-S02': '',
        'P-23/005-S02': '', 'P-23/006-S02': '', 'P-23/007-S02': '', 'P-23/008-S02': '', 'P-23/009-S02': '',
        'P-23/010-S02': '', 'P-23/011-S02': '', 'P-23/012-S02': '', 'P-23/013-S02': '', 'P-23/014-S02': '',
        'P-23/015-S02': '', 'P-23/016-S02': '', 'P-23/017-S02': '', 'P-23/018-S02': '', 'P-23/019-S02': '',
        'P-23/020-S02': '', 'P-23/021-S02': '', 'P-23/022-S02': '', 'P-23/023-S02': '', 'P-23/024-S02': '',
        'P-23/025-S02': '', 'P-23/026-S02': '', 'P-23/027-S02': '', 'P-23/028-S02': '', 'P-23/029-S02': '',
        'P-23/030-S02': '', 'P-23/031-S02': '', 'P-23/032-S02': '', 'P-23/033-S02': '', 'P-23/034-S02': '',
        'P-23/035-S02': '', 'P-23/036-S02': '', 'P-23/037-S02': '', 'P-23/038-S02': '', 'P-23/039-S02': '',
        'P-23/040-S02': '', 'P-23/041-S02': '', 'P-23/042-S02': '', 'P-23/043-S02': '', 'P-23/044-S02': '',
        'P-23/045-S02': '', 'P-23/046-S02': '', 'P-23/047-S02': '', 'P-23/048-S02': '', 'P-23/049-S02': '',
        'P-23/050-S02': '', 'P-23/051-S02': '', 'P-23/052-S02': '', 'P-23/053-S02': '', 'P-23/054-S02': '',
        'P-23/055-S02': '', 'P-23/056-S02': '', 'P-23/057-S02': '', 'P-23/058-S02': '', 'P-23/059-S02': '',
        'P-23/060-S02': '', 'P-23/061-S02': '', 'P-23/062-S02': '', 'P-23/063-S02': '', 'P-23/064-S02': '',
        'P-23/065-S02': '', 'P-23/066-S02': '', 'P-23/067-S02': '', 'P-23/068-S02': '', 'P-23/069-S02': '',
        'P-23/070-S02': '', 'P-23/071-S02': '', 'P-23/072-S02': '', 'P-23/073-S02': '', 'P-23/074-S02': '',
        'P-23/075-S02': '', 'P-23/076-S02': '', 'P-23/077-S02': '', 'P-23/078-S02': '', 'P-23/079-S02': '',
        'P-23/080-S02': '', 'P-23/081-S02': '', 'P-23/082-S02': '', 'P-23/083-S02': '', 'P-23/084-S02': '',
        'P-23/085-S02': '', 'P-23/086-S02': '', 'P-23/087-S02': '', 'P-23/088-S02': '', 'P-23/089-S02': '',
        'P-23/090-S02': '', 'P-23/091-S02': '', 'P-23/092-S02': '', 'P-23/093-S02': '', 'P-23/094-S02': '',
        'P-23/095-S02': '', 'P-23/096-S02': '', 'P-23/097-S02': '', 'P-23/098-S02': '', 'P-23/099-S02': '',
        'P-23/100-S02': '', 'P-23/101-S02': '', 'P-23/102-S02': '', 'P-23/103-S02': '', 'P-23/104-S02': '',
        'P-23/105-S02': '', 'P-24/001-S02': '', 'P-24/002-S02': '', 'P-24/003-S02': '', 'P-24/004-S02': '',
        'P-24/005-S02': '', 'P-24/006-S02': '', 'P-24/007-S02': '', 'P-24/008-S02': '', 'P-24/009-S02': '',
        'P-24/010-S02': '', 'P-24/011-S02': '', 'P-24/012-S02': '', 'P-24/013-S02': '', 'P-24/014-S02': '',
        'P-24/015-S02': '', 'P-24/016-S02': '', 'P-24/017-S02': '', 'P-24/018-S02': '', 'P-24/019-S02': '',
        'P-24/020-S02': '', 'P-24/021-S02': '', 'P-24/022-S02': '', 'P-24/023-S02': '', 'P-24/024-S02': '',
        'P-24/025-S02': '', 'P-24/026-S02': '', 'P-24/027-S02': '', 'P-24/028-S02': '',
        'P-24/029-S02': '', 'P-24/030-S02': '', 'P-24/031-S02': '', 'P-24/032-S02': '', 'P-24/033-S02': '',
        'P-24/034-S02': '', 'P-24/035-S02': '', 'P-24/036-S02': '', 'P-24/037-S02': '', 'P-24/038-S02': '',
        'P-24/039-S02': '', 'P-24/040-S02': '', 'P-24/041-S02': '', 'P-24/042-S02': '', 'P-24/043-S02': '',
        'P-24/044-S02': '', 'P-24/045-S02': '', 'P-24/046-S02': '', 'P-24/047-S02': '', 'P-24/048-S02': '',
        'P-24/049-S02': '', 'P-24/050-S02': '', 'P-24/051-S02': '', 'P-24/052-S02': '', 'P-24/053-S02': '',
        'P-22/001-S03': '',
        'P-22/002-S03': '', 'P-22/003-S03': '', 'P-22/004-S03': '', 'P-22/005-S03': '', 'P-22/006-S03': '',
        'P-22/007-S03': '', 'P-22/008-S03': '', 'P-22/009-S03': '', 'P-22/010-S03': '', 'P-22/011-S03': '',
        'P-22/012-S03': '', 'P-22/013-S03': '', 'P-22/014-S03': '', 'P-22/015-S03': '', 'P-22/016-S03': '',
        'P-22/017-S03': '', 'P-22/018-S03': '', 'P-22/019-S03': '', 'P-22/020-S03': '', 'P-22/021-S03': '',
        'P-22/022-S03': '', 'P-22/023-S03': '', 'P-22/024-S03': '', 'P-22/025-S03': '', 'P-22/026-S03': '',
        'P-22/027-S03': '', 'P-22/028-S03': '', 'P-22/029-S03': '', 'P-22/030-S03': '', 'P-22/031-S03': '',
        'P-22/032-S03': '', 'P-22/033-S03': '', 'P-22/034-S03': '', 'P-22/035-S03': '', 'P-22/036-S03': '',
        'P-22/037-S03': '', 'P-22/038-S03': '', 'P-22/039-S03': '', 'P-22/040-S03': '', 'P-22/041-S03': '',
        'P-22/042-S03': '', 'P-22/043-S03': '', 'P-22/044-S03': '', 'P-22/045-S03': '', 'P-22/046-S03': '',
        'P-22/047-S03': '', 'P-22/048-S03': '', 'P-22/049-S03': '', 'P-22/050-S03': '', 'P-22/051-S03': '',
        'P-22/052-S03': '', 'P-22/053-S03': '', 'P-22/054-S03': '', 'P-22/055-S03': '', 'P-22/056-S03': '',
        'P-22/057-S03': '', 'P-22/058-S03': '', 'P-22/059-S03': '', 'P-22/060-S03': '', 'P-22/061-S03': '',
        'P-22/062-S03': '', 'P-22/063-S03': '', 'P-22/064-S03': '', 'P-22/065-S03': '', 'P-22/066-S03': '',
        'P-22/067-S03': '', 'P-22/068-S03': '', 'P-22/069-S03': '', 'P-22/070-S03': '', 'P-22/071-S03': '',
        'P-22/072-S03': '', 'P-22/073-S03': '', 'P-22/074-S03': '', 'P-22/075-S03': '', 'P-22/076-S03': '',
        'P-22/077-S03': '', 'P-22/078-S03': '', 'P-22/079-S03': '', 'P-22/080-S03': '', 'P-22/081-S03': '',
        'P-22/082-S03': '', 'P-22/083-S03': '', 'P-22/084-S03': '', 'P-22/085-S03': '', 'P-22/086-S03': '',
        'P-22/087-S03': '', 'P-22/088-S03': '', 'P-22/089-S03': '', 'P-22/090-S03': '', 'P-22/091-S03': '',
        'P-22/092-S03': '', 'P-22/093-S03': '', 'P-22/094-S03': '', 'P-22/095-S03': '', 'P-22/096-S03': '',
        'P-22/097-S03': '', 'P-22/098-S03': '', 'P-22/099-S03': '', 'P-22/100-S03': '', 'P-22/101-S03': '',
        'P-22/102-S03': '', 'P-22/103-S03': '', 'P-22/104-S03': '', 'P-22/105-S03': '', 'P-23/001-S03': '',
        'P-23/002-S03': '', 'P-23/003-S03': '', 'P-23/004-S03': '', 'P-23/005-S03': '', 'P-23/006-S03': '',
        'P-23/007-S03': '', 'P-23/008-S03': '', 'P-23/009-S03': '', 'P-23/010-S03': '', 'P-23/011-S03': '',
        'P-23/012-S03': '', 'P-23/013-S03': '', 'P-23/014-S03': '', 'P-23/015-S03': '', 'P-23/016-S03': '',
        'P-23/017-S03': '', 'P-23/018-S03': '', 'P-23/019-S03': '', 'P-23/020-S03': '', 'P-23/021-S03': '',
        'P-23/022-S03': '', 'P-23/023-S03': '', 'P-23/024-S03': '', 'P-23/025-S03': '', 'P-23/026-S03': '',
        'P-23/027-S03': '', 'P-23/028-S03': '', 'P-23/029-S03': '', 'P-23/030-S03': '', 'P-23/031-S03': '',
        'P-23/032-S03': '', 'P-23/033-S03': '', 'P-23/034-S03': '', 'P-23/035-S03': '', 'P-23/036-S03': '',
        'P-23/037-S03': '', 'P-23/038-S03': '', 'P-23/039-S03': '', 'P-23/040-S03': '', 'P-23/041-S03': '',
        'P-23/042-S03': '', 'P-23/043-S03': '', 'P-23/044-S03': '05-01-2023', 'P-23/045-S03': '', 'P-23/046-S03': '',
        'P-23/047-S03': '', 'P-23/048-S03': '', 'P-23/049-S03': '', 'P-23/050-S03': '', 'P-23/051-S03': '',
        'P-23/052-S03': '', 'P-23/053-S03': '', 'P-23/054-S03': '', 'P-23/055-S03': '', 'P-23/056-S03': '',
        'P-23/057-S03': '', 'P-23/058-S03': '', 'P-23/059-S03': '', 'P-23/060-S03': '', 'P-23/061-S03': '',
        'P-23/062-S03': '', 'P-23/063-S03': '', 'P-23/064-S03': '', 'P-23/065-S03': '', 'P-23/066-S03': '',
        'P-23/067-S03': '', 'P-23/068-S03': '', 'P-23/069-S03': '', 'P-23/070-S03': '', 'P-23/071-S03': '',
        'P-23/072-S03': '', 'P-23/073-S03': '', 'P-23/074-S03': '19-09-2024', 'P-23/075-S03': '', 'P-23/076-S03': '',
        'P-23/077-S03': '', 'P-23/078-S03': '', 'P-23/079-S03': '', 'P-23/080-S03': '', 'P-23/081-S03': '',
        'P-23/082-S03': '', 'P-23/083-S03': '', 'P-23/084-S03': '', 'P-23/085-S03': '', 'P-23/086-S03': '',
        'P-23/087-S03': '', 'P-23/088-S03': '', 'P-23/089-S03': '', 'P-23/090-S03': '', 'P-23/091-S03': '',
        'P-23/092-S03': '', 'P-23/093-S03': '', 'P-23/094-S03': '', 'P-23/095-S03': '', 'P-23/096-S03': '',
        'P-23/097-S03': '', 'P-23/098-S03': '', 'P-23/099-S03': '', 'P-23/100-S03': '', 'P-23/101-S03': '',
        'P-23/102-S03': '', 'P-23/103-S03': '', 'P-23/104-S03': '', 'P-23/105-S03': '', 'P-24/001-S03': '',
        'P-24/002-S03': '', 'P-24/003-S03': '', 'P-24/004-S03': '', 'P-24/005-S03': '', 'P-24/006-S03': '',
        'P-24/007-S03': '', 'P-24/008-S03': '', 'P-24/009-S03': '', 'P-24/010-S03': '', 'P-24/011-S03': '',
        'P-24/012-S03': '', 'P-24/013-S03': '', 'P-24/014-S03': '', 'P-24/015-S03': '', 'P-24/016-S03': '',
        'P-24/017-S03': '', 'P-24/018-S03': '', 'P-24/019-S03': '', 'P-24/020-S03': '', 'P-24/021-S03': '',
        'P-24/022-S03': '', 'P-24/023-S03': '', 'P-24/024-S03': '', 'P-24/025-S03': '', 'P-24/026-S03': '',
        'P-24/027-S03': '', 'P-24/028-S03': '',
        'P-24/029-S03': '', 'P-24/030-S03': '', 'P-24/031-S03': '', 'P-24/032-S03': '', 'P-24/033-S03': '',
        'P-24/034-S03': '', 'P-24/035-S03': '', 'P-24/036-S03': '', 'P-24/037-S03': '', 'P-24/038-S03': '',
        'P-24/039-S03': '', 'P-24/040-S03': '', 'P-24/041-S03': '', 'P-24/042-S03': '', 'P-24/043-S03': '',
        'P-24/044-S03': '', 'P-24/045-S03': '', 'P-24/046-S03': '', 'P-24/047-S03': '', 'P-24/048-S03': '',
        'P-24/049-S03': '', 'P-24/050-S03': '', 'P-24/051-S03': '', 'P-24/052-S03': '', 'P-24/053-S03': '',
        'P-22/001-S04': '', 'P-22/002-S04': '', 'P-22/003-S04': '',
        'P-22/004-S04': '', 'P-22/005-S04': '', 'P-22/006-S04': '', 'P-22/007-S04': '', 'P-22/008-S04': '',
        'P-22/009-S04': '', 'P-22/010-S04': '', 'P-22/011-S04': '', 'P-22/012-S04': '', 'P-22/013-S04': '',
        'P-22/014-S04': '', 'P-22/015-S04': '', 'P-22/016-S04': '', 'P-22/017-S04': '', 'P-22/018-S04': '',
        'P-22/019-S04': '', 'P-22/020-S04': '', 'P-22/021-S04': '', 'P-22/022-S04': '', 'P-22/023-S04': '',
        'P-22/024-S04': '', 'P-22/025-S04': '', 'P-22/026-S04': '', 'P-22/027-S04': '', 'P-22/028-S04': '',
        'P-22/029-S04': '', 'P-22/030-S04': '', 'P-22/031-S04': '', 'P-22/032-S04': '', 'P-22/033-S04': '',
        'P-22/034-S04': '', 'P-22/035-S04': '', 'P-22/036-S04': '', 'P-22/037-S04': '', 'P-22/038-S04': '',
        'P-22/039-S04': '', 'P-22/040-S04': '', 'P-22/041-S04': '', 'P-22/042-S04': '', 'P-22/043-S04': '',
        'P-22/044-S04': '', 'P-22/045-S04': '', 'P-22/046-S04': '', 'P-22/047-S04': '', 'P-22/048-S04': '',
        'P-22/049-S04': '', 'P-22/050-S04': '', 'P-22/051-S04': '', 'P-22/052-S04': '', 'P-22/053-S04': '',
        'P-22/054-S04': '', 'P-22/055-S04': '', 'P-22/056-S04': '', 'P-22/057-S04': '', 'P-22/058-S04': '',
        'P-22/059-S04': '', 'P-22/060-S04': '', 'P-22/061-S04': '', 'P-22/062-S04': '', 'P-22/063-S04': '',
        'P-22/064-S04': '', 'P-22/065-S04': '', 'P-22/066-S04': '', 'P-22/067-S04': '', 'P-22/068-S04': '',
        'P-22/069-S04': '', 'P-22/070-S04': '', 'P-22/071-S04': '', 'P-22/072-S04': '', 'P-22/073-S04': '',
        'P-22/074-S04': '', 'P-22/075-S04': '', 'P-22/076-S04': '', 'P-22/077-S04': '', 'P-22/078-S04': '',
        'P-22/079-S04': '', 'P-22/080-S04': '', 'P-22/081-S04': '', 'P-22/082-S04': '', 'P-22/083-S04': '',
        'P-22/084-S04': '', 'P-22/085-S04': '', 'P-22/086-S04': '', 'P-22/087-S04': '', 'P-22/088-S04': '',
        'P-22/089-S04': '', 'P-22/090-S04': '', 'P-22/091-S04': '', 'P-22/092-S04': '', 'P-22/093-S04': '',
        'P-22/094-S04': '', 'P-22/095-S04': '', 'P-22/096-S04': '', 'P-22/097-S04': '', 'P-22/098-S04': '',
        'P-22/099-S04': '', 'P-22/100-S04': '', 'P-22/101-S04': '', 'P-22/102-S04': '', 'P-22/103-S04': '',
        'P-22/104-S04': '', 'P-22/105-S04': '', 'P-23/001-S04': '', 'P-23/002-S04': '', 'P-23/003-S04': '',
        'P-23/004-S04': '', 'P-23/005-S04': '', 'P-23/006-S04': '', 'P-23/007-S04': '', 'P-23/008-S04': '',
        'P-23/009-S04': '', 'P-23/010-S04': '', 'P-23/011-S04': '', 'P-23/012-S04': '', 'P-23/013-S04': '',
        'P-23/014-S04': '', 'P-23/015-S04': '', 'P-23/016-S04': '', 'P-23/017-S04': '', 'P-23/018-S04': '',
        'P-23/019-S04': '', 'P-23/020-S04': '', 'P-23/021-S04': '', 'P-23/022-S04': '', 'P-23/023-S04': '',
        'P-23/024-S04': '', 'P-23/025-S04': '', 'P-23/026-S04': '', 'P-23/027-S04': '', 'P-23/028-S04': '',
        'P-23/029-S04': '', 'P-23/030-S04': '', 'P-23/031-S04': '', 'P-23/032-S04': '', 'P-23/033-S04': '',
        'P-23/034-S04': '', 'P-23/035-S04': '', 'P-23/036-S04': '', 'P-23/037-S04': '', 'P-23/038-S04': '',
        'P-23/039-S04': '', 'P-23/040-S04': '', 'P-23/041-S04': '', 'P-23/042-S04': '', 'P-23/043-S04': '',
        'P-23/044-S04': '29-04-2024', 'P-23/045-S04': '', 'P-23/046-S04': '', 'P-23/047-S04': '', 'P-23/048-S04': '',
        'P-23/049-S04': '', 'P-23/050-S04': '', 'P-23/051-S04': '', 'P-23/052-S04': '', 'P-23/053-S04': '',
        'P-23/054-S04': '', 'P-23/055-S04': '', 'P-23/056-S04': '', 'P-23/057-S04': '', 'P-23/058-S04': '',
        'P-23/059-S04': '', 'P-23/060-S04': '', 'P-23/061-S04': '', 'P-23/062-S04': '', 'P-23/063-S04': '',
        'P-23/064-S04': '', 'P-23/065-S04': '', 'P-23/066-S04': '', 'P-23/067-S04': '', 'P-23/068-S04': '',
        'P-23/069-S04': '', 'P-23/070-S04': '', 'P-23/071-S04': '', 'P-23/072-S04': '', 'P-23/073-S04': '',
        'P-23/074-S04': '', 'P-23/075-S04': '', 'P-23/076-S04': '', 'P-23/077-S04': '', 'P-23/078-S04': '',
        'P-23/079-S04': '', 'P-23/080-S04': '', 'P-23/081-S04': '', 'P-23/082-S04': '', 'P-23/083-S04': '',
        'P-23/084-S04': '', 'P-23/085-S04': '', 'P-23/086-S04': '', 'P-23/087-S04': '', 'P-23/088-S04': '',
        'P-23/089-S04': '', 'P-23/090-S04': '', 'P-23/091-S04': '', 'P-23/092-S04': '', 'P-23/093-S04': '',
        'P-23/094-S04': '', 'P-23/095-S04': '', 'P-23/096-S04': '', 'P-23/097-S04': '', 'P-23/098-S04': '',
        'P-23/099-S04': '', 'P-23/100-S04': '', 'P-23/101-S04': '', 'P-23/102-S04': '', 'P-23/103-S04': '',
        'P-23/104-S04': '', 'P-23/105-S04': '', 'P-24/001-S04': '', 'P-24/002-S04': '', 'P-24/003-S04': '',
        'P-24/004-S04': '', 'P-24/005-S04': '', 'P-24/006-S04': '', 'P-24/007-S04': '', 'P-24/008-S04': '',
        'P-24/009-S04': '', 'P-24/010-S04': '', 'P-24/011-S04': '', 'P-24/012-S04': '', 'P-24/013-S04': '',
        'P-24/014-S04': '', 'P-24/015-S04': '', 'P-24/016-S04': '', 'P-24/017-S04': '', 'P-24/018-S04': '',
        'P-24/019-S04': '', 'P-24/020-S04': '', 'P-24/021-S04': '', 'P-24/022-S04': '', 'P-24/023-S04': '',
        'P-24/024-S04': '', 'P-24/025-S04': '', 'P-24/026-S04': '', 'P-24/027-S04': '', 'P-24/028-S04': '',
        'P-24/029-S04': '', 'P-24/030-S04': '', 'P-24/031-S04': '', 'P-24/032-S04': '', 'P-24/033-S04': '',
        'P-24/034-S04': '', 'P-24/035-S04': '', 'P-24/036-S04': '', 'P-24/037-S04': '', 'P-24/038-S04': '',
        'P-24/039-S04': '', 'P-24/040-S04': '', 'P-24/041-S04': '', 'P-24/042-S04': '', 'P-24/043-S04': '',
        'P-24/044-S04': '', 'P-24/045-S04': '', 'P-24/046-S04': '', 'P-24/047-S04': '', 'P-24/048-S04': '',
        'P-24/049-S04': '', 'P-24/050-S04': '', 'P-24/051-S04': '', 'P-24/052-S04': '', 'P-24/053-S04': '',
        'P-24/054-S04': '', 'P-24/055-S04': '', 'P-24/056-S04': '', 'P-24/057-S04': '', 'P-24/058-S04': '',
        'P-24/059-S04': '', 'P-24/060-S04': '', 'P-24/061-S04': '', 'P-24/062-S04': '', 'P-24/063-S04': '',
        'P-24/064-S04': '', 'P-24/065-S04': '', 'P-24/066-S04': '', 'P-24/067-S04': '', 'P-24/068-S04': '',
        'P-24/069-S04': '', 'P-24/070-S04': '', 'P-24/071-S04': '', 'P-24/072-S04': '', 'P-24/073-S04': '',
        'P-24/074-S04': '', 'P-24/075-S04': '', 'P-24/076-S04': '', 'P-24/077-S04': '', 'P-24/078-S04': '',
    }

    df['Fecha AP VDDL'] = df['Fecha AP VDDL'].map(mapping).fillna(np.nan)

    return df