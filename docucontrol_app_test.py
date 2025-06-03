import tkinter as tk
import threading
from tkinter import ttk
from tkinter import messagebox, Toplevel, filedialog
from PIL import Image, ImageTk
import subprocess
import os
import shutil
import pandas as pd

# Fecha actual
today_date = pd.to_datetime('today', format='%d-%m-%Y', dayfirst=True)
today_date_str = today_date.strftime('%d-%m-%Y')

# Ruta base
script_dir = os.path.dirname(os.path.abspath(__file__))

# ----------------- FUNCIONES -----------------
def show_progress_and_run(target_func):
    progress_win = Toplevel(root)
    progress_win.title("Ejecutando...")
    progress_win.configure(bg="#f0f0f0")
    progress_win.resizable(False, False)
    win_width, win_height = 400, 150
    progress_win.geometry(f"{win_width}x{win_height}")

    root.update_idletasks()
    root_x = root.winfo_x()
    root_y = root.winfo_y()
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    x = root_x + (root_width // 2) - (win_width // 2)
    y = root_y + (root_height // 2) - (win_height // 2)
    progress_win.geometry(f"+{x}+{y}")

    progress_win.transient(root)
    progress_win.grab_set()

    tk.Label(progress_win, text="Por favor, espera...", bg="#f0f0f0", font=("Arial", 11)).pack(pady=(10, 0))
    pb = ttk.Progressbar(progress_win, mode="indeterminate", length=300)
    pb.pack(pady=10)
    pb.start(10)
    message_var = tk.StringVar()
    label_message = tk.Label(progress_win, textvariable=message_var, bg="#f0f0f0", font=("Arial", 10, "italic"))
    label_message.pack(pady=5)
    phrases = [
        "¡Generando columnas...!",
        "¡Estilo, formato y color aplicado!",
        "¡Columnas y celdas ajustadas para una mejor visualización!",
        "¡Creando los filtros de las columnas!"
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
        messagebox.showinfo("Éxito", f"'{os.path.basename(script_path)}' se ejecutó correctamente.")
        if popup:
            popup.destroy()
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", f"Error al ejecutar '{os.path.basename(script_path)}'.")

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
            os.startfile(dest_path)
        else:
            messagebox.showwarning("Cancelado", "No se seleccionó ninguna carpeta para copiar el archivo.")
        if popup:
            popup.destroy()
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", f"Error al ejecutar '{os.path.basename(script_path)}'.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def open_excel_file(filepath, popup=None):
    try:
        full_path = os.path.join(script_dir, filepath)
        if not os.path.exists(full_path):
            messagebox.showerror("Error", f"No se encontró el archivo: {filepath}")
            return
        os.startfile(full_path)
        if popup:
            popup.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir el archivo:\n{e}")

def open_devoluciones_popup():
    popup = Toplevel(root)
    popup.title("Devoluciones")
    popup.configure(bg="#f0f0f0")
    popup.geometry("520x200")
    popup.update_idletasks()
    x = root.winfo_screenwidth() - popup.winfo_width() - 10
    y = root.winfo_screenheight() - popup.winfo_height() - 70
    popup.geometry(f"+{x}+{y}")

    def load_logo(filename, size=(100, 100)):
        img_path = os.path.join(script_dir, filename)
        image = Image.open(img_path).resize(size, Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)

    tr_img = load_logo("tools/img/tr_logo.png")
    prodoc_img = load_logo("tools/img/prodoc_logo.png")
    gaia_img = load_logo("tools/img/gaia_logo.png")
    plantilla_img = load_logo("tools/img/plantilla_devoluciones.png")

    btns = [
        (tr_img, lambda: run_script(os.path.join(script_dir, "tr_email_mapi_automation.py"))),
        (prodoc_img, lambda: run_script(os.path.join(script_dir, "prodoc_email_mapi_automation.py"))),
        (gaia_img, lambda: run_script(os.path.join(script_dir, "gaia_email_mapi_automation.py"))),
        (plantilla_img, lambda: open_excel_file("tools/plantilla_devoluciones.xlsm"))
    ]

    for i, (img, cmd) in enumerate(btns):
        btn = tk.Button(popup, image=img, command=cmd, relief="raised", bd=4, cursor="hand2")
        btn.image = img
        btn.grid(row=0, column=i, padx=10, pady=10)

    labels = ["Técnicas Reunidas", "Wood / Prodoc", "GAIA / Technip", "Plantilla"]
    for i, text in enumerate(labels):
        tk.Label(popup, text=text, bg="#f0f0f0").grid(row=1, column=i)

def open_monitoring_popup():
    popup = Toplevel(root)
    popup.title("Monitoring Report")
    popup.configure(bg="#f0f0f0")
    popup.geometry("440x260")
    popup.update_idletasks()
    x = root.winfo_screenwidth() - popup.winfo_width() - 10
    y = root.winfo_screenheight() - popup.winfo_height() - 70
    popup.geometry(f"+{x}+{y}")

    base_path = script_dir

    ttk.Button(popup, text="Informe de Progreso",
               command=lambda: show_progress_and_run(lambda: run_script_and_copy_excel(
                   os.path.join(base_path, "monitoring_report.py"),
                   f"Monitoring_Report_{today_date_str}.xlsx",
                   popup)),
               style="Monitoring.TButton").pack(pady=10)

    ttk.Button(popup, text="Reclamaciones (Vía Email)",
               command=lambda: subprocess.run(["python", os.path.join(base_path, "reclamations.py")]),
               style="Reclamaciones.TButton").pack(pady=5)

    ttk.Button(popup, text="OVR",
               command=lambda: show_progress_and_run(lambda: run_script_and_copy_excel(
                   os.path.join(base_path, "ovr_automation.py"),
                   f"OVR_Report_{today_date_str}.xlsx",
                   popup)),
               style="OVR.TButton").pack(pady=5)

# ----------------- MAIN APP -----------------
root = tk.Tk()
root.title("DocuControl")
root.configure(bg="#f0f0f0")
window_width = 440
window_height = 200
x = root.winfo_screenwidth() - window_width - 10
y = root.winfo_screenheight() - window_height - 70
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# --------- ESTILOS VISUALES ---------
style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="white", font=("Arial", 11, "bold"))
style.map("TButton", background=[("active", "#45a049")])
style.configure("Monitoring.TButton", background="#007acc", font=("Arial", 11, "bold"))
style.map("Monitoring.TButton", background=[("active", "#005f99")])
style.configure("OVR.TButton", background="#9b59b6")
style.map("OVR.TButton", background=[("active", "#7d3c98")])
style.configure("Reclamaciones.TButton", background="#e67e22")
style.map("Reclamaciones.TButton", background=[("active", "#cf711f")])
style.configure("TLabel", background="#f0f0f0")

# --------- LOGO E ÍCONO ---------
def load_main_logo(filename, size=(60, 60)):
    img_path = os.path.join(script_dir, filename)
    image = Image.open(img_path).resize(size, Image.ANTIALIAS)
    return ImageTk.PhotoImage(image)

main_logo_img = load_main_logo("tools/img/main_logo_img.png")
root.iconphoto(False, main_logo_img)

# --------- FRAME PRINCIPAL Y BOTONES ---------
main_frame = ttk.Frame(root, padding=10)
main_frame.pack(expand=True)

btn_monitoring = ttk.Button(main_frame, text="Monitoring Report", command=open_monitoring_popup, style="Monitoring.TButton")
btn_monitoring.grid(row=0, column=0, padx=10, pady=15)

btn_devoluciones = ttk.Button(main_frame, text="Devoluciones", command=open_devoluciones_popup, style="TButton")
btn_devoluciones.grid(row=1, column=0, padx=10, pady=5)

root.mainloop()
