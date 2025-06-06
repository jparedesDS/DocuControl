import tkinter as tk
import threading
from tkinter import ttk
from tkinter import messagebox, Toplevel, filedialog
from PIL import Image, ImageTk
import subprocess
import os
import shutil
import pandas as pd


today_date = pd.to_datetime('today', format='%d-%m-%Y', dayfirst=True)  # Capturamos la fecha actual del día
today_date_str = today_date.strftime('%d-%m-%Y') # Formateamos la fecha_actual a strf para la lectura y guardado de archivos

# Ruta base para scripts locales
script_dir = os.path.dirname(os.path.abspath(__file__))

def show_progress_and_run(target_func):
    progress_win = Toplevel(root)
    progress_win.title("Ejecutando...")
    progress_win.iconbitmap(os.path.join(script_dir, "tools/img/docucontrol_icon-256x256.ico"))
    progress_win.configure(bg="#f0f0f0")
    progress_win.resizable(False, False)

    # Tamaño ventana
    win_width, win_height = 400, 150

    # Obtener tamaño de la pantalla
    screen_width = progress_win.winfo_screenwidth()
    screen_height = progress_win.winfo_screenheight()

    # Calcular coordenadas para centrar
    x = (screen_width // 2) - (win_width // 2)
    y = (screen_height // 2) - (win_height // 2)

    progress_win.geometry(f"{win_width}x{win_height}+{x}+{y}")

    progress_win.transient(root)
    progress_win.grab_set()

    # Widgets
    tk.Label(progress_win, text="Por favor, espera...", bg="#f0f0f0", font=("Arial", 11)).pack(pady=(10, 0))

    pb = ttk.Progressbar(progress_win, mode="indeterminate", length=300)
    pb.pack(pady=10)
    pb.start(10)

    message_var = tk.StringVar()
    label_message = tk.Label(progress_win, textvariable=message_var, bg="#f0f0f0", font=("Arial", 9, "italic"))
    label_message.pack(pady=5)

    phrases = [
        "¡Generando columnas...!",
        "¡Estilo, formato y color aplicado!",
        "¡Columnas y celdas ajustadas para una mejor visualización!",
        "¡Creando los filtros de las columnas!",
    ]

    def animate_messages(index=0):
        if index < len(phrases):
            message_var.set(phrases[index])
            progress_win.after(5000, animate_messages, index + 1)
        else:
            message_var.set("Finalizando...")

    def task_wrapper():
        try:
            target_func()
        finally:
            progress_win.destroy()

    threading.Thread(target=task_wrapper, daemon=True).start()
    animate_messages()



def run_script(script_path, popup=None):
    try:
        subprocess.run(["python", script_path], check=True)
        #messagebox.showinfo("Éxito", f"'{os.path.basename(script_path)}' se ejecutó correctamente.")
        if popup:
            popup.destroy()
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", f"Error al ejecutar '{os.path.basename(script_path)}'.")

# Nueva función que ejecuta el script y copia el archivo generado
def run_script_and_copy_excel(script_path, generated_file, popup=None):
    try:
        subprocess.run(["python", script_path], check=True)

        destination_folder = filedialog.askdirectory(title="Selecciona una carpeta para copiar el Excel")
        if destination_folder:
            generated_file_path = os.path.join(script_dir, generated_file)
            if not os.path.exists(generated_file_path):
                messagebox.showerror("Error", f"No se encontró el archivo generado: '{generated_file}'.")
                return
            dest_path = os.path.join(destination_folder, generated_file)
            shutil.copy(generated_file_path, dest_path)
            os.startfile(dest_path)  # Esto abre el Excel directamente
        else:
            messagebox.showwarning("Cancelado", "No se seleccionó ninguna carpeta para copiar el archivo.")

        if popup:
            popup.destroy()
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", f"Error al ejecutar '{os.path.basename(script_path)}'.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# --------- Subventana para "Devoluciones" ----------
def open_excel_file(filepath, popup=None):
    try:
        full_path = os.path.join(script_dir, filepath)
        if not os.path.exists(full_path):
            messagebox.showerror("Error", f"No se encontró el archivo: {filepath}")
            return
        os.startfile(full_path)  # Abre con Excel u otro programa asociado
        if popup:
            popup.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir el archivo:\n{e}")


def open_devoluciones_popup():
    popup = Toplevel(root)
    popup.title("Devoluciones")
    popup.iconbitmap(os.path.join(script_dir, "tools/img/docucontrol_icon-256x256.ico"))
    popup.configure(bg="#f0f0f0")

    popup.geometry("520x200")  # aumentamos el ancho para dar espacio al cuarto botón
    popup.update_idletasks()
    popup_width = popup.winfo_width()
    popup_height = popup.winfo_height()
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    x = screen_width - popup_width - 10
    y = screen_height - popup_height - 70
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

    def load_logo(filename, size=(100, 100)):
        img_path = os.path.join(script_dir, filename)
        image = Image.open(img_path).resize(size, Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)

    tr_img = load_logo("C:\\Users\\alejandro.berzal\\Desktop\\DATA SCIENCE\\DocuControl\\tools\\img\\tr_logo.png")
    prodoc_img = load_logo("C:\\Users\\alejandro.berzal\\Desktop\\DATA SCIENCE\\DocuControl\\tools\\img\\prodoc_logo.png")
    gaia_img = load_logo("C:\\Users\\alejandro.berzal\\Desktop\\DATA SCIENCE\\DocuControl\\tools\\img\\gaia_logo.png")
    plantilla_img = load_logo("C:\\Users\\alejandro.berzal\\Desktop\\DATA SCIENCE\\DocuControl\\tools\\img\\plantilla_devoluciones.png")
    btn_tr = tk.Button(popup, image=tr_img, command=lambda: run_script(os.path.join(script_dir, "tr_email_mapi_automation.py")),
                       relief="raised", bd=4, cursor="hand2")
    btn_tr.image = tr_img

    btn_prodoc = tk.Button(popup, image=prodoc_img, command=lambda: run_script(os.path.join(script_dir, "prodoc_email_mapi_automation.py")),
                           relief="raised", bd=4, cursor="hand2")
    btn_prodoc.image = prodoc_img

    btn_gaia = tk.Button(popup, image=gaia_img, command=lambda: run_script(os.path.join(script_dir, "gaia_email_mapi_automation.py")),
                         relief="raised", bd=4, cursor="hand2")
    btn_gaia.image = gaia_img

    btn_plantilla = tk.Button(popup, image=plantilla_img,
                              command=lambda: open_excel_file("tools/plantilla_devoluciones.xlsm"),
                              relief="raised", bd=4, cursor="hand2")
    btn_plantilla.image = plantilla_img

    btn_tr.grid(row=0, column=0, padx=10, pady=10)
    btn_prodoc.grid(row=0, column=1, padx=10, pady=10)
    btn_gaia.grid(row=0, column=2, padx=10, pady=10)
    btn_plantilla.grid(row=0, column=3, padx=10, pady=10)

    tk.Label(popup, text="Técnicas Reunidas", bg="#f0f0f0").grid(row=1, column=0)
    tk.Label(popup, text="Wood / Prodoc", bg="#f0f0f0").grid(row=1, column=1)
    tk.Label(popup, text="GAIA / Technip", bg="#f0f0f0").grid(row=1, column=2)
    tk.Label(popup, text="Plantilla", bg="#f0f0f0").grid(row=1, column=3)


# --------- Subventana para "Monitoring Report" ----------
def open_monitoring_popup():
    popup = Toplevel(root)
    popup.title("Monitoring Report")
    popup.iconbitmap(os.path.join(script_dir, "tools/img/docucontrol_icon-256x256.ico"))
    popup.configure(bg="#f0f0f0")

    popup.geometry("440x260")  # Ampliamos un poco el alto por el nuevo botón
    popup.update_idletasks()
    popup_width = popup.winfo_width()
    popup_height = popup.winfo_height()
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    x = screen_width - popup_width - 10
    y = screen_height - popup_height - 70
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

    base_path = r"C:\Users\alejandro.berzal\Desktop\DATA SCIENCE\DocuControl"

    btn_informe = tk.Button(popup, text="Informe de Progreso",
                            command=lambda: show_progress_and_run(
                                lambda: run_script_and_copy_excel(
                                    os.path.join(base_path, "monitoring_report.py"),
                                    "Monitoring_Report_" + str(today_date_str) + ".xlsx",
                                    popup)
                            ),
                            height=3, width=25, font=("Arial", 11, "bold"),
                            relief="raised", bd=4, bg="#007acc", fg="white", cursor="hand2")
    btn_informe.pack(pady=10)

    btn_reclamaciones = tk.Button(popup, text="Reclamaciones (Vía Email)",
                                  command=lambda: subprocess.run(
                                      ["python", os.path.join(base_path, "reclamations.py")]),
                                  height=3, width=25, font=("Arial", 11, "bold"),
                                  relief="raised", bd=4, bg="#e67e22", fg="white", cursor="hand2")
    btn_reclamaciones.pack(pady=5)

    # NUEVO BOTÓN OVR
    btn_ovr = tk.Button(popup, text="OVR",
                        command=lambda: show_progress_and_run(
                            lambda: run_script_and_copy_excel(
                                os.path.join(base_path, "ovr_automation.py"),
                                "OVR_Report_" + str(today_date_str) + ".xlsx",
                                popup)
                        ),
                        height=3, width=25, font=("Arial", 11, "bold"),
                        relief="raised", bd=4, bg="#9b59b6", fg="white", cursor="hand2")
    btn_ovr.pack(pady=5)


# --------- Ventana Principal ----------
root = tk.Tk()
root.title("DocuControl")
root.configure(bg="#f0f0f0")

window_width = 440
window_height = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = screen_width - window_width - 10
y = screen_height - window_height - 70
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

btn_monitoring = tk.Button(root, text="Monitoring Report", command=open_monitoring_popup,
                           height=3, width=20, font=("Arial", 12, "bold"),
                           relief="raised", bd=5, bg="#007acc", fg="white", cursor="hand2")
btn_monitoring.pack(pady=15)

btn_devoluciones = tk.Button(root, text="Devoluciones", command=open_devoluciones_popup,
                             height=3, width=20, font=("Arial", 12, "bold"),
                             relief="raised", bd=5, bg="#4caf50", fg="white", cursor="hand2")
btn_devoluciones.pack(pady=5)


def load_main_logo(filename, size=(64, 64)):
    img_path = os.path.join(script_dir, filename)
    image = Image.open(img_path).resize(size, Image.ANTIALIAS)
    return ImageTk.PhotoImage(image)


# Establecer ícono para ventana y barra de tareas
root.iconbitmap(os.path.join(script_dir, "tools/img/docucontrol_icon-256x256.ico"))

# Cargar imagenes visuales (.png)
docu_icon = load_main_logo("tools/img/docucontrol_icon.png")
img_eipsa_icon = load_main_logo("tools/img/main_logo_img.png")

# Mostrar imagen visual en la esquina superior izquierda
logo_label = tk.Label(root, image=img_eipsa_icon, bg="#f0f0f0", borderwidth=0)
logo_label.place(x=10, y=10)

root.mainloop()
