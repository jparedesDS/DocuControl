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
ruta_excel = f"U:\\USUARIOS\\jose.paredes\\Desktop\\DocuControl\\monitoring_report_{hoy_str}.xlsx"

# Cargar DataFrame desde hoja 'ENVIADOS'
df = pd.read_excel(ruta_excel, sheet_name='ENVIADOS')

# Filtrar reclamaciones con más de 0 días
df_filtrado = df[df['Días Devolución'] >= 0]

# Eliminar columnas no deseadas
columnas_a_eliminar = ['Responsable', 'Nº Oferta', 'Fecha Pedido', 'Cliente', 'Fecha Prevista', 'Info/Review', 'Repsonsable', 'Días Envío', 'Material', 'Tipo Doc.', 'Crítico',
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

# Cambiar 'Enviado' por 'Submitted' en la columna Status
if 'Estado' in df_filtrado.columns:
    df_filtrado['Estado'] = df_filtrado['Estado'].replace({'Enviado': 'Submitted'})

# Aplicar estilo "resaltado de texto"
def aplicar_estilos_html(df):
    df = df.fillna("")

    def resaltar_texto(val):
        return f'<span style="background-color: yellow">{val}</span>'

    if 'Return Days' in df.columns:
        df['Return Days'] = df['Return Days'].apply(
            lambda x: resaltar_texto(f'<b><span style="color:red">{x}</span></b>'))

    if 'Doc. Sent Date' in df.columns:
        df['Doc. Sent Date'] = df['Doc. Sent Date'].apply(resaltar_texto)

    # --- Estilos de encabezado ---
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

    # --- Estilo base de celdas ---
    cell_style = 'background-color: #D4DCF4; color: #000000; text-align: left; font-size: 14px;'
    for col in df.columns:
        styled = styled.map(lambda _: cell_style, subset=[col])

    # --- Estilo especial para columna Estado/Status ---
    col_estado = 'Status' if 'Status' in df.columns else ('Estado' if 'Estado' in df.columns else None)
    if col_estado:
        estado_style = {
            'Rechazado': 'background-color:#F8B4B4; color:#000;',
            'Comentado': 'background-color:#FFE599; color:#000;',
            'Aprobado': 'background-color:#00D25F; color:#000;',
            'Submitted': 'background-color:#B1E1B9; color:#000;',
        }

        def estilo_estado(val):
            for k, v in estado_style.items():
                if k.lower() in str(val).lower():
                    return v
            return 'background-color:#D4DCF4; color:#000;'

        styled = styled.map(estilo_estado, subset=[col_estado])

    # **Ocultar índice**
    styled = styled.hide(axis='index')

    return styled.to_html(escape=False)


# Diccionario para renombrar
rename_dict = {
    "Nº Pedido": "Order No.",
    "Nº PO": "PO No.",
    "Nº Doc. Cliente": "Client Doc. No.",
    "Nº Doc. EIPSA": "EIPSA Doc. No.",
    "Título": "Title",
    "Estado": "Status",
    "Nº Revisión": "Revision No.",
    "Fecha Env. Doc.": "Doc. Sent Date",
    "Días Devolución": "Return Days"
}
# Renombrar columnas
df_filtrado = df_filtrado.rename(columns=rename_dict)

# Agrupar por prefijo y enviar correos
outlook = win32.Dispatch('outlook.application')

# Agrupar por prefijo y ordenar por Días Devolución de mayor a menor
for prefijo, grupo in df_filtrado.groupby("Prefijo Pedido"):
    grupo = grupo.sort_values(by='Return Days', ascending=False)

    # Eliminar columna de prefijo para que no se muestre en el correo
    grupo = grupo.drop(columns=['Prefijo Pedido'])

    html_table = aplicar_estilos_html(grupo)
    num_po = grupo['PO No.'].iloc[0] if 'PO No.' in grupo.columns and not grupo['PO No.'].isnull().all() else 'N/A'

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