import pandas as pd
import re
from datetime import datetime
import time
from tools.apply_style_ovr import *

start_time = time.time()
today_date = datetime.today()
today_date_str = today_date.strftime('%d-%m-%Y')

# Cargar el archivo Excel principal
df = pd.read_excel("C:\\Users\\alejandro.berzal\\Desktop\\DATA SCIENCE\\DocuControl\\data_import\\data_erp.xlsx")
df = df[df['Estado'] != 'Eliminado']
df['Estado'] = df['Estado'].fillna('Sin Enviar')

# Renombrar columnas
df = df.rename(columns={
    'Fecha': 'Fecha Doc.',
    'Fecha Prevista': 'Fecha FIN',
    'Fecha Pedido': 'Fecha INICIAL'
})

# Convertir fechas
df['Fecha Doc.'] = pd.to_datetime(df['Fecha Doc.'], dayfirst=True, errors='coerce')
df['Fecha INICIAL'] = pd.to_datetime(df['Fecha INICIAL'], dayfirst=True, errors='coerce')
df['Fecha FIN'] = pd.to_datetime(df['Fecha FIN'], dayfirst=True, errors='coerce')

# Calcular días de aprobación
mask_aprobado = df['Estado'] == 'Aprobado'
df.loc[mask_aprobado, 'Días Aprobación'] = (
    (df.loc[mask_aprobado, 'Fecha Doc.'] - df.loc[mask_aprobado, 'Fecha INICIAL']).dt.days
)

# Función para extraer fechas del historial
def procesar_historial(historial):
    fechas_raw = re.findall(r'\d{2}[/-]\d{2}[/-]\d{4}', str(historial))
    fechas = []
    for f in fechas_raw:
        try:
            fecha = datetime.strptime(f.replace('/', '-'), '%d-%m-%Y')
            fechas.append(fecha)
        except ValueError:
            continue
    fechas.sort()
    return fechas

# Procesar columna de historial
fechas_ordenadas = df['Historial Rev.'].apply(procesar_historial)
max_fechas = fechas_ordenadas.apply(len).max()
num_pares = max_fechas // 2 + max_fechas % 2

nombres_columnas = []
for i in range(num_pares):
    nombres_columnas.extend([f'Env. {i}', f'Dev. {i}'])

df_fechas = pd.DataFrame(columns=nombres_columnas)

for idx, fechas in fechas_ordenadas.items():
    fila = {}
    for i, fecha in enumerate(fechas):
        if i < len(nombres_columnas):
            fila[nombres_columnas[i]] = fecha.strftime('%d-%m-%Y')
    df_fechas.loc[idx] = fila

# Unir al original
df_final = pd.concat([df, df_fechas], axis=1)

# Procesamiento principal
df_ovr = df_final.reindex(columns=[
    'Nº Pedido', 'Resp.', 'Nº PO', 'Cliente', 'Material', 'Nº Doc. Cliente',
    'Nº Doc. EIPSA', 'Título', 'Tipo Doc.', 'Crítico', 'Estado', 'Nº Revisión',
    'Fecha INICIAL', 'Fecha FIN', 'Fecha Doc.', 'Días Aprobación',
    'Reclamaciones', 'Seguimiento', 'Env. 0', 'Dev. 0', 'Env. 1', 'Dev. 1', 'Env. 2', 'Dev. 2',
    'Env. 3', 'Dev. 3', 'Env. 4', 'Dev. 4', 'Env. 5', 'Dev. 5', 'Env. 6', 'Dev. 6', 'Env. 7', 'Dev. 7', 'Env. 8', 'Dev. 8', 'Historial Rev.',
])
df_ovr['Tipo Doc.'] = df_ovr['Tipo Doc.'].str.strip()
df_ovr = df_ovr.drop(columns=['Seguimiento', 'Resp.', 'Reclamaciones', 'Cliente', 'Material', 'Crítico'])

# --- UNIÓN CON DATA_TAGS ---

# Cargar data_tags
df_tags = pd.read_excel("C:\\Users\\alejandro.berzal\\Desktop\\DATA SCIENCE\\DocuControl\\data_import\\data_tags.xlsx")

# Crear columna unificada para las dos columnas de data_tags
df_tags_melted = df_tags.melt(
    id_vars=[col for col in df_tags.columns if col not in ['Nº Doc. EIPSA Cálculo', 'Nº Doc. EIPSA Plano']],
    value_vars=['Nº Doc. EIPSA Cálculo', 'Nº Doc. EIPSA Plano'],
    var_name='Tipo Nº Doc.',
    value_name='Nº Doc. EIPSA Tag'
)

# Filtrar nulos
df_tags_melted = df_tags_melted[df_tags_melted['Nº Doc. EIPSA Tag'].notna()]

# Merge 1: por 'Nº Doc. EIPSA'
merge_eipsa = df_ovr.merge(df_tags_melted, left_on='Nº Doc. EIPSA', right_on='Nº Doc. EIPSA Tag', how='left')

# Merge 2: por 'Nº Doc. Cliente'
merge_cliente = df_ovr.merge(df_tags_melted, left_on='Nº Doc. Cliente', right_on='Nº Doc. EIPSA Tag', how='left')

# Unir ambos merges y eliminar duplicados
df_union = pd.concat([merge_eipsa, merge_cliente], ignore_index=True)
df_union = df_union.drop_duplicates(subset=['Nº Doc. EIPSA', 'Nº Doc. Cliente'])


# Guardar resultado final
aplicar_estilos_y_guardar_excel(df_union, f'OVR_Report_Union_{today_date_str}.xlsx')
