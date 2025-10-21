import re
from datetime import datetime
import time
from utils.apply_style_ovr import *

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

# Función mejorada para extraer pares (fecha, acción, número rev)
# Función mejorada: todo lo que NO sea Enviado va a Dev.
def procesar_historial_avanzado(historial):
    resultados = []
    patron = r'(\d{2}[/-]\d{2}[/-]\d{4})\s*([A-Za-zÁÉÍÓÚáéíóúüÜñÑ.\s]+?)\s*Rev\.?\s*(\d+)'
    matches = re.findall(patron, str(historial))
    for match in matches:
        fecha_str, accion, rev_num = match
        accion = accion.strip()
        if 'Enviado' in accion:
            tipo = 'Env.'
        else:
            tipo = 'Dev.'
        try:
            fecha = datetime.strptime(fecha_str.replace('/', '-'), '%d-%m-%Y')
            resultados.append((tipo, int(rev_num), fecha))
        except ValueError:
            continue
    return resultados


# Procesar columna de historial con la versión avanzada
historial_procesado = df['Historial Rev.'].apply(procesar_historial_avanzado)

# Crear columnas necesarias
max_rev = 8  # ajusta según lo máximo que tengas
nombres_columnas = []
for i in range(max_rev + 1):
    nombres_columnas.extend([f'Env. {i}', f'Dev. {i}'])

df_fechas = pd.DataFrame('', index=df.index, columns=nombres_columnas)

# Llenar columnas correctamente
for idx, eventos in historial_procesado.items():
    for tipo, rev_num, fecha in eventos:
        col_name = f'{tipo} {rev_num}'
        if col_name in df_fechas.columns:
            df_fechas.at[idx, col_name] = fecha.strftime('%d-%m-%Y')

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
df_ovr = df_ovr.drop(columns=['Seguimiento', 'Resp.', 'Reclamaciones', 'Seguimiento', 'Cliente', 'Material', 'Crítico'])

# Guardar resultado final
aplicar_estilos_y_guardar_excel(df_ovr, f'OVR_Simple_{today_date_str}.xlsx')