import os
import time
import pandas as pd
import win32com.client as win32
import re
from datetime import datetime

# Obtener la fecha actual
hoy = pd.to_datetime("today")
hoy_str = hoy.strftime("%d-%m-%Y")

# Ruta del archivo original
ruta_excel = f"C:\\Users\\alejandro.berzal\\Desktop\\DATA SCIENCE\\DocuControl\\Monitoring_Report_{hoy_str}.xlsx"

# Cargar DataFrame desde hoja 'ENVIADOS'
df = pd.read_excel(ruta_excel, sheet_name='ENVIADOS')

# Filtrar reclamaciones con más de 100 días
df_filtrado = df[df['Días Devolución'] >= 100]

# Eliminar columnas no deseadas
columnas_a_eliminar = ['Resp.', 'Cliente', 'Material', 'Tipo Doc.', 'Crítico',
                       'Fecha INICIAL', 'Fecha FIN', 'Reclamaciones',
                       'Seguimiento', 'Historial Rev.']
df_filtrado = df_filtrado.drop(columns=[col for col in columnas_a_eliminar if col in df_filtrado.columns])
df_filtrado = df_filtrado.reset_index(drop=True)

# Formatear columnas específicas
if 'Nº Revisión' in df_filtrado.columns:
    df_filtrado['Nº Revisión'] = df_filtrado['Nº Revisión'].apply(lambda x: int(x) if pd.notnull(x) else '')

if 'Fecha Env. Doc.' in df_filtrado.columns:
    df_filtrado['Fecha Env. Doc.'] = pd.to_datetime(df_filtrado['Fecha Env. Doc.'], errors='coerce').dt.strftime('%d-%m-%Y')

# Aplicar estilo "resaltado de texto"
def aplicar_estilos_html(df):
    # Reemplazar NaN por espacios en blanco
    df = df.fillna("")

    # Simula resaltado amarillo SOLO en texto
    def resaltar_texto(val):
        return f'<span style="background-color: yellow">{val}</span>'

    # Resaltar 'Días Devolución'
    if 'Días Devolución' in df.columns:
        df['Días Devolución'] = df['Días Devolución'].apply(
            lambda x: resaltar_texto(f'<b><span style="color:red">{x}</span></b>'))

    # Resaltar 'Fecha Env. Doc.'
    if 'Fecha Env. Doc.' in df.columns:
        df['Fecha Env. Doc.'] = df['Fecha Env. Doc.'].apply(resaltar_texto)

    # Estilo general para cabecera
    header_style = [{
        'selector': 'th',
        'props': [
            ('background-color', '#6678AF'),
            ('color', '#FFFFFF'),
            ('text-align', 'center'),
            ('font-size', '14px'),
            ('font-weight', 'bold')
        ]
    }]

    styled = df.style.set_table_styles(header_style)

    # Estilo base para todas las celdas
    cell_style = 'background-color: #D4DCF4; color: #000000; text-align: left; font-size: 14px;'
    for col in df.columns:
        if col != 'Estado':
            styled = styled.map(lambda _: cell_style, subset=[col])

    # Estilo especial para columna 'Estado'
    if 'Estado' in df.columns:
        estado_style = 'background-color: #B1E1B9; color: #000000; text-align: center;'
        styled = styled.map(lambda _: estado_style, subset=['Estado'])

    return styled.to_html(index=False, escape=False)  # escape=False permite HTML en el contenido


# Agrupar por pedido y enviar correos
outlook = win32.Dispatch('outlook.application')
for pedido, grupo in df_filtrado.groupby('Nº Pedido'):
    html_table = aplicar_estilos_html(grupo)
    num_po = grupo['Nº PO'].iloc[0] if 'Nº PO' in grupo.columns and not grupo['Nº PO'].isnull().all() else 'N/A'

    mail = outlook.CreateItem(0)
    mail.Subject = f"RECLAIMS: {pedido} / PO: {num_po} // DOC. UNDER REVIEW"
    mail.Display()

    signature = mail.HTMLBody
    custom_body = f"""
    <p>Dear All,</p>
    <p>- The following documents have been sent pending review and have not yet been returned by the customer:</p>
    {html_table}
    <p>If you can tell us the resolution of these documents and when they are expected to be returned by the customer, I would appreciate it..</p>
    """
    mail.HTMLBody = custom_body + signature
    mail.Save()
    time.sleep(2)

    # Sanear nombre del archivo
    pedido_limpio = re.sub(r'[\\/*?:"<>|]', "-", str(pedido))
    nombre_base = f"Reclamacion_Pedido_{pedido_limpio}"
    nombre_archivo = f"{nombre_base}.msg"

    # Ruta donde guardar los correos (ajusta según tu usuario)
    carpeta_guardado = os.path.expanduser(f"Z:\\JOSE\\03 RECLAMACIONES\\" + pedido_limpio)
    os.makedirs(carpeta_guardado, exist_ok=True)

    # Evitar sobrescritura de archivos
    contador = 1
    ruta_completa = os.path.join(carpeta_guardado, nombre_archivo)
    while os.path.exists(ruta_completa):
        nombre_archivo = f"{nombre_base}_{contador}.msg"
        ruta_completa = os.path.join(carpeta_guardado, nombre_archivo)
        contador += 1

    try:
        mail.SaveAs(ruta_completa)
        print(f"Guardado correctamente en: {ruta_completa}")
    except Exception as e:
        print(f"❌ Error al guardar el correo: {e}")


