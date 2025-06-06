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

# Filtrar reclamaciones con más de 0 días
df_filtrado = df[df['Días Devolución'] >= 10]

# Eliminar columnas no deseadas
columnas_a_eliminar = ['Resp.', 'Cliente', 'Material', 'Tipo Doc.', 'Crítico',
                       'Fecha INICIAL', 'Fecha FIN', 'Reclamaciones',
                       'Seguimiento', 'Historial Rev.']
df_filtrado = df_filtrado.drop(columns=[col for col in columnas_a_eliminar if col in df_filtrado.columns])
df_filtrado = df_filtrado.reset_index(drop=True)

# Crear columna "Prefijo Pedido" para agrupar por el inicio del pedido
df_filtrado["Prefijo Pedido"] = df_filtrado["Nº Pedido"].astype(str).str.extract(r'^(P-\d+/\d+)', expand=False)

# Formatear columnas específicas
if 'Nº Revisión' in df_filtrado.columns:
    df_filtrado['Nº Revisión'] = df_filtrado['Nº Revisión'].apply(lambda x: int(x) if pd.notnull(x) else '')

if 'Fecha Env. Doc.' in df_filtrado.columns:
    df_filtrado['Fecha Env. Doc.'] = pd.to_datetime(df_filtrado['Fecha Env. Doc.'], errors='coerce').dt.strftime('%d-%m-%Y')

# Aplicar estilo "resaltado de texto"
def aplicar_estilos_html(df):
    df = df.fillna("")

    def resaltar_texto(val):
        return f'<span style="background-color: yellow">{val}</span>'

    if 'Días Devolución' in df.columns:
        df['Días Devolución'] = df['Días Devolución'].apply(
            lambda x: resaltar_texto(f'<b><span style="color:red">{x}</span></b>'))

    if 'Fecha Env. Doc.' in df.columns:
        df['Fecha Env. Doc.'] = df['Fecha Env. Doc.'].apply(resaltar_texto)

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

    cell_style = 'background-color: #D4DCF4; color: #000000; text-align: left; font-size: 14px;'
    for col in df.columns:
        if col != 'Estado':
            styled = styled.map(lambda _: cell_style, subset=[col])

    if 'Estado' in df.columns:
        estado_style = 'background-color: #B1E1B9; color: #000000; text-align: center;'
        styled = styled.map(lambda _: estado_style, subset=['Estado'])

    return styled.to_html(index=False, escape=False)

# Agrupar por prefijo y enviar correos
outlook = win32.Dispatch('outlook.application')

# Agrupar por prefijo y ordenar por Días Devolución de mayor a menor
for prefijo, grupo in df_filtrado.groupby("Prefijo Pedido"):
    grupo = grupo.sort_values(by='Días Devolución', ascending=False)

    # Eliminar columna de prefijo para que no se muestre en el correo
    grupo = grupo.drop(columns=['Prefijo Pedido'])

    html_table = aplicar_estilos_html(grupo)
    num_po = grupo['Nº PO'].iloc[0] if 'Nº PO' in grupo.columns and not grupo['Nº PO'].isnull().all() else 'N/A'

    mail = outlook.CreateItem(0)
    mail.Subject = f"RECLAIMS: {prefijo} / PO: {num_po} // DOC. UNDER REVIEW"
    mail.Display()

    signature = mail.HTMLBody
    custom_body = f"""
    <p>Dear All,</p>
    <p>- The following documents have been sent pending review and have not yet been returned by the customer:</p>
    {html_table}
    <p>If you can tell us the resolution of these documents and when they are expected to be returned by the customer, I would appreciate it.</p>
    """
    mail.HTMLBody = custom_body + signature
    mail.Save()
    time.sleep(2)

    # Sanear nombre del archivo
    prefijo_limpio = re.sub(r'[\\/*?:"<>|]', "-", str(prefijo))
    nombre_base = f"Reclamacion_Pedido_{prefijo_limpio}"
    nombre_archivo = f"{nombre_base}.msg"

    carpeta_guardado = os.path.expanduser(f"Z:\\JOSE\\03 RECLAMACIONES\\" + prefijo_limpio)
    os.makedirs(carpeta_guardado, exist_ok=True)

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