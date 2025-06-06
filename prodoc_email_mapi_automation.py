""" Versión v1.0.0 - Automatización, envío, tratamiento de datos y entrada a BBDD para transmittals de PRODOC """
from datetime import timedelta
# Imports
import time
import shutil
import win32com.client
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO
from tools.ERPconn import *
from tools.email_identification import *
from tools.po_identification import *
from tools.prodoc_data_process import *
from tools.apply_style_email import *

# Time
date = datetime.now()
dia = date.strftime('%d-%m-%Y')
fecha_actual = pd.Timestamp.now()
# Generamos las carpetas correspondientes para guardar los archivos
nombre_carpeta = os.path.join(f'Z:\\JOSE\\02 DEVOLUCIÓN DOCUMENTACIÓN\\PRODOC\\' +dia)
if not os.path.isdir(nombre_carpeta):
    print(f'No existe la ruta: '+nombre_carpeta+', se crea la carpeta')
    os.mkdir(nombre_carpeta)

# Ruta del archivo Excel donde se agregarán los datos
combine_path = f'Z:\\JOSE\\02 DEVOLUCIÓN DOCUMENTACIÓN\\PRODOC\\all_tr_combine.xlsx'
# Se indica la url en la que guardaremos los archivos
cwd = os.getcwd()    # Capturamos la url de la carpeta
src = cwd    # Capturamos la url en una variable
dst = f'Z:\\JOSE\\02 DEVOLUCIÓN DOCUMENTACIÓN\\PRODOC\\' +str(dia)    # Generamos una url de una nueva carpeta en la que iran los .xlsx

# Añadimos dataframes vacíos para la captura de los datos
df = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
i = 0

# Conexionado con el servidor de Outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
# Bandeja de entrada de Outlook, acceso y búsqueda de los últimos mensajes recibidos .Folders("carpeta")
inbox = outlook.GetDefaultFolder(6)#.Folders["test1"]    # Quitar selección de carpeta
messages = inbox.Items.Restrict("[Unread]=true")    # Obligamos a solo buscar entre los emails que se encuentren aún sin leer
messages.Sort("ReceivedTime", True)    # Ordenamos los mensajes según su entrada por tiempo
message = messages.GetFirst()    # Selección del email

start_time = time.time()
# Bucle captura de mensaje a través de BeautifulSoup para tabla html, bodytext y creación excel entrada BBDD
while message:
    if message.SenderEmailAddress != 'Prodoc.postmaster@woodplc.com':
        message = messages.GetNext()
        continue  # Salta al siguiente email si no es del remitente deseado
    try:
        receivedtime = message.ReceivedTime.strftime('%d-%m-%Y %H:%M:%S')  # Obtenemos la fecha entrante del email.
        subject_email = message.Subject  # Obtenemos el Asunto del email entrante.
        regex_transmittal = r'TL-\d{2,4}[A-Z0-9]+-VDC-\d{4}'
        match = re.search(regex_transmittal, subject_email)
        transmittal_code = match.group(0) if match else None
        subject_email = re.sub(r'[\/:*?"<>|]', '', subject_email)
        message.SaveAs(subject_email + '.msg')
        text_html = message.HTMLBody  # Captura de texto email
        html_body = BeautifulSoup(text_html, "lxml")  # Captura del texto.
        html_tables = html_body('table')[0]  # Seleccionamos la tabla excel en el cuerpo del email.
        df_list = pd.read_html(StringIO(text_html))  # Captura del email en text_html.
        df = df_list[0]  # Seleccionamos la posición [5] en la que encontramos la información y tabla del email.
        df = df.loc[:, ['Name', 'P.O.', 'Title', 'Rev', 'S.R. Status',
                        'Date']]  # Reorganizamos las columnas para realizar la importación correcta a BBDD.
        df['Nº Pedido'] = df[
            'P.O.']  # Creamos una nueva columna en la cual identificamos el Tipo de documento a traves del ['Vendor Number'].
        prodoc_vendor_number(df)
        df['Tipo de documento'] = df[
            'Name']  # Creamos una nueva columna en la cual identificamos el Tipo de documento a traves del ['Vendor Number'].
        df['Tipo de documento'] = df['Tipo de documento'].str.extract(r'-(\D{2,3})(?=-\d{1,})',
                                                                      expand=False)  # Obtenemos el 'TIPO DE DOCUMENTO'.
        df[
            'Supp.'] = 'S00'  # Creamos una nueva columna en la cual identificaremos el suplemento a traves del ['Vendor Number'].
        ### Reemplaza los valores de la columna "Suplemento", si el valor no se encuentra en el mapeo o es NaN, se reemplaza con 'S00'.
        reemplazar_null(df)
        df.insert(6, "Crítico",
                  "Sí")  # Creación nuevas columnas ["Critico"] en la 6º posición del df ################## La idea sería a traves del tipo de documento indicar si es critico o no.
        df['P.O.'] = df['P.O.'].apply(str)
        identificar_cliente_por_PO_PRODOC(df)
        # Generamos una nueva columna llamada ['EMAIL'] con el Tipo de documento, el cual transformaremos para identificar el email de la persona al que va asociado el documento.
        df['EMAIL'] = df['Tipo de documento']  # Damos los datos de tipo de documento a la columna df[EMAIL]
        df2['EMAIL'] = df['EMAIL']  # Creamos un df2 con solo esta columna.
        df['EMAIL'].pop  # Eliminamos la columna.
        procesar_documento_y_fecha(df, receivedtime)
        cambiar_tipo_estado(df)
        critico(df)
        # Renombramos las columnas al Castellano
        df.rename(
            columns={'Name': 'Doc. EIPSA', 'Rev': 'Rev.', 'Title': 'Título', 'S.R. Status': 'Estado', 'Rev': 'TR Rev.',
                     'P.O.': 'PO'},
            inplace=True)
        df['Doc. Cliente'] = df['Doc. EIPSA']
        df['Rev.'] = df['TR Rev.']
        reconocer_tipo_proyecto(df)
        df['Nº Transmittal'] = transmittal_code
        print(df)

        # Generamos la conexión con Outlook y se genera el email
        ol = win32com.client.Dispatch("outlook.application")  # Conexión directa con la aplicación de Outlook.
        olmailitem = 0x0  # Tamaño del nuevo email.
        newmail = ol.CreateItem(olmailitem)  # Creación del email.
        newmail.Subject = 'DEV: ' + str(df['Nº Pedido'].iloc[0]) + ' [' + subject_email + ']'
        ### Aplicamos la función que nos identifica quien es el resposable del documento ###
        df2 = email_employee(df2)
        ### Aplicar la función para generar la columna 'Responsable_email' ###
        df['Responsable_email'] = df['Nº Pedido'].apply(get_responsable_email)
        # Generamos la selección automática de a quien se va a enviar el email
        mapping = {';luis-bravo@eipsa.es;': 'LB', ';ana-calvo@eipsa.es;': 'AC', ';sandra-sanz@eipsa.es;': 'SS',
                   ';carlos-crespohor@eipsa.es;': 'CC'}
        df['Responsable'] = df.apply(lambda row: mapping[row['Responsable_email']], axis=1)
        df.reset_index()  # Quitamos el index el df
        df3 = df['Responsable_email'].apply(
            pd.Series)  # Generamos df3 donde encontramos la información del responsable del proyecto.
        df_final = pd.concat([df, df3], axis=1)  # Se une la columna ['Responsable_email'] al df_final.
        # Estructuramos los datos del df_final
        df_final = df_final.reindex(
            ['Nº Pedido', 'Supp.', 'Responsable', 'Cliente', 'Material', 'PO', 'Doc. EIPSA', 'Doc. Cliente',
             'Título', 'Rev.', 'TR Rev.', 'Estado', 'Tipo de documento', 'Crítico', 'Nº Transmittal', 'Fecha'],
            axis=1)
        df_final.to_excel(f'RESUMEN - ' + subject_email + '.xlsx', index=False)  # Generamos el dataframe RESUMEN.
        aplicar_estilos_y_guardar_excel(df_final, f'RESUMEN - ' + subject_email + '.xlsx')
        df_import = df_final.copy()  # Generamos el dataframe de IMPORTACIÓN a ERP (df_import).
        df_import = df_import.reindex(
            ['Nº Pedido', 'Supp.', 'PO', 'Doc. Cliente', 'Título', 'Rev.', 'TR Rev.', 'Estado',
             'Fecha'], axis=1)  # Estructuramos los datos del df_import.
        # Exportar el DataFrame estilizado a HTML
        styled_df = aplicar_estilos_html(df_import)
        # Cargar datos previos del archivo Excel si existe
        if os.path.exists(combine_path):
            df_existing = pd.read_excel(combine_path)
            df_combined = pd.concat([df_existing, df_final], ignore_index=True)
        else:
            df_combined = df_final
        reemplazar_null(df_combined)
        # Guardar los datos combinados en el archivo Excel
        df_combined.to_excel(combine_path, index=False)
        # Exportar el DataFrame estilizado a HTML
        df_body = df_import.drop(
            columns=['Nº Pedido', 'Supp.', 'PO', 'Fecha'])  # Quitamos esas columnas para el cuerpo
        df_body = aplicar_estilos_html(df_body)
        # Creamos un DataFrame con los datos superiores (Nº Pedido, Supp., PO)
        df_info = pd.DataFrame({
            df_final['Cliente'].iloc[0]: ['Nº Pedido', 'Supp.', 'PO', 'Fecha'],
            df_final['Material'].iloc[0]: [df_import['Nº Pedido'].iloc[0], df_import['Supp.'].iloc[0],
                                           df_import['PO'].iloc[0], df_import['Fecha'].iloc[0]]})
        df_info = aplicar_estilo_info(df_info)
        # Unimos HTML al cuerpo del email
        body = df_info + df_body

        # Generamos la entrada de datos al email
        newmail.To = ';santos-sanchez@eipsa.es;' + str(df3[0][0])
        newmail.CC = ';jesus-martinez@eipsa.es;ernesto-carrillo@eipsa.es;' + str(df2[0][0])
        newmail.HTMLBody = ('<html><body>'
                            '<p>Buenos días,</p>'
                            '<p>Han devuelto la siguiente documentación:</p>'
                            + '<div>' + body + '</div>'
                                               '<p>DESCARGADO Y ACTUALIZADO EN ERP.</p>'
                                               '<p>HAY QUE SUBIRLO ANTES DEL: ' + (
                                    date + pd.DateOffset(days=15)).strftime("%d-%m-%Y") + '</p>'
                                                                                          '</body></html>')
        attach = 'C:\\Users\\alejandro.berzal\\Desktop\\DATA SCIENCE\\DocuControl\\RESUMEN - ' + subject_email + '.xlsx'  # Url para la captura del documento.
        newmail.Attachments.Add(attach)  # Adjuntar el archivo al email.
        newmail.Display()  # Visualización del email.
        # newmail.Send()    # Envio automático del email.
        # Movemos los archivos a las carpetas correspondientes
        shutil.move(os.path.join(src, f'RESUMEN - ' + subject_email + '.xlsx'),
                    os.path.join(dst, f'RESUMEN - ' + subject_email + '.xlsx'))
        print(df_final)
        i += 1
    except (IndexError, KeyError):
        print("No se localiza ningún Transmittal en este email...")

    message = messages.GetNext()

    # importar_archivos_excel_en_carpeta(nombre_carpeta2)
    print("Duración del proceso: {} seconds".format(time.time() - start_time))