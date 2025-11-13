import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import subprocess
import threading
import os
import shutil
import pandas as pd
import sys

# === CONFIGURACIÓN GENERAL ===
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

today_date = pd.Timestamp.today()
today_date_str = today_date.strftime("%d-%m-%Y")
script_dir = os.path.dirname(os.path.abspath(__file__))

# === FUNCIONES AUXILIARES ===
def bottom_right_quadrant_window(win, padding_x=0, padding_y=40):
    """Coloca la ventana en el cuadrante inferior derecho del monitor principal, sin tapar la barra de tareas."""
    win.update_idletasks()
    screen_w, screen_h = win.winfo_screenwidth(), win.winfo_screenheight()

    # tamaño de un cuarto de pantalla
    width = screen_w // 2
    height = screen_h // 2 - padding_y

    # posición inferior derecha
    x = screen_w - width - padding_x
    y = screen_h - height - padding_y

    win.geometry(f"{width}x{height}+{x}+{y}")

def run_script(script_path):
    try:
        subprocess.run([sys.executable, script_path], check=True)
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", f"Error al ejecutar '{os.path.basename(script_path)}'.")

def run_script_and_copy_excel(script_path, generated_file):
    try:
        subprocess.run([sys.executable, script_path], check=True)
        dest_folder = filedialog.askdirectory(title="Selecciona una carpeta para copiar el Excel")
        if not dest_folder:
            messagebox.showwarning("Cancelado", "No se seleccionó ninguna carpeta.")
            return

        src = os.path.join(script_dir, generated_file)
        if not os.path.exists(src):
            messagebox.showerror("Error", f"No se encontró el archivo '{generated_file}'.")
            return

        dst = os.path.join(dest_folder, generated_file)
        shutil.copy(src, dst)
        os.startfile(dst)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def load_image(filename, size=(30, 30)):
    path = os.path.join(script_dir, filename)
    img = Image.open(path).resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)

def show_progress_in_content(parent_frame, func, callback=None):
    for widget in parent_frame.winfo_children():
        widget.destroy()

    container = ctk.CTkFrame(parent_frame, fg_color="transparent")
    container.place(relx=0.5, rely=0.5, anchor="center")

    ctk.CTkLabel(container, text="Procesando...", font=("Arial", 16, "bold")).pack(pady=(0, 10))
    bar = ctk.CTkProgressBar(container, width=250)
    bar.pack(pady=5)
    bar.start()

    msg_var = ctk.StringVar(value="Inicializando...")
    ctk.CTkLabel(container, textvariable=msg_var, font=("Arial", 11, "italic")).pack(pady=(5, 10))

    msgs = ["Extrayendo información de la base de datos...", "Resumiendo datos...", "Generando columnas...",
            "Aplicando formato...", "Ajustando celdas...", "Generando archivo...", "Finalizando..."]

    def animate(i=0):
        if i < len(msgs):
            msg_var.set(msgs[i])
            container.after(1800, animate, i + 1)

    def run_thread():
        try:
            func()
        finally:
            msg_var.set("¡Completado!")
            bar.stop()
            if callback:
                parent_frame.after(800, callback)

    threading.Thread(target=run_thread, daemon=True).start()
    animate()

# === CLASE PRINCIPAL ===
class DocuControlApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("DocuControl App")

        # === ICONO DE LA APP ===
        icon_path = os.path.join(script_dir, "utils/img/docucontrol_white_icon.ico")
        if os.path.exists(icon_path):
            try:
                # Asegura el icono en la barra de tareas (Windows)
                self.iconbitmap(icon_path)

                # Este fragmento adicional lo refuerza en algunos sistemas
                import ctypes
                ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("DocuControl App")
            except Exception as e:
                print(f"No se pudo establecer el icono: {e}")

        # tamaño y posición automática
        bottom_right_quadrant_window(self)

        # Layout principal
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nswe")
        self.sidebar.grid_rowconfigure(99, weight=1)

        logo = load_image("utils/img/main_logo_img.png", (60, 60))
        ctk.CTkLabel(self.sidebar, image=logo, text="", width=100).grid(row=0, column=0, pady=(15, 8))
        self.logo_img = logo

        ctk.CTkLabel(self.sidebar, text="DocuControl", font=("Arial", 17, "bold")).grid(row=1, column=0, pady=(0, 20))

        # Botones laterales grandes
        self.btn_monitoring = ctk.CTkButton(self.sidebar, text="📊 Documentación", fg_color="#1E88E5",
                                            height=45, corner_radius=8, font=("Arial", 12, "bold"),
                                            command=self.show_monitoring_page)
        self.btn_monitoring.grid(row=2, column=0, pady=6, padx=10, sticky="ew")

        self.btn_devoluciones = ctk.CTkButton(self.sidebar, text="📦 Devoluciones", fg_color="#43A047",
                                              height=45, corner_radius=8, font=("Arial", 12, "bold"),
                                              command=self.show_devoluciones_page)
        self.btn_devoluciones.grid(row=3, column=0, pady=6, padx=10, sticky="ew")

        # Frame inferior
        self.bottom_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        self.bottom_frame.grid(row=100, column=0, sticky="swe", padx=10, pady=12)

        self.btn_volver = ctk.CTkButton(self.bottom_frame, text="⬅️ Volver", fg_color="#757575",
                                        height=45, corner_radius=8, font=("Arial", 12, "bold"),
                                        command=self.show_welcome_page)
        self.btn_volver.pack(fill="x", pady=(0,4))

        self.btn_exit = ctk.CTkButton(self.bottom_frame, text="🚪 Salir", fg_color="#E53935",
                                      height=45, corner_radius=8, font=("Arial", 12, "bold"),
                                      command=self.destroy)
        self.btn_exit.pack(fill="x")

        # Frame principal
        self.content = ctk.CTkFrame(self, corner_radius=8)
        self.content.grid(row=0, column=1, sticky="nswe", padx=15, pady=15)
        self.show_welcome_page()

    # === PÁGINAS ===
    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_welcome_page(self):
        self.clear_content()

        # Logo arriba
        self.logo_image = load_image("utils/img/docucontrol_white.png", (450, 280))
        ctk.CTkLabel(self.content, image=self.logo_image, text="").pack(pady=(0, 30))

        # Título grande
        ctk.CTkLabel(
            self.content,
            text="¡Bienvenido! 👋",
            font=("Arial", 26, "bold")
        ).pack(pady=(0, 15))

        # Subtítulo o descripción
        ctk.CTkLabel(
            self.content,
            text="Gestiona tus documentos de manera rápida y sencilla.\n"
                 "Selecciona una opción en el menú lateral para comenzar.",
            font=("Arial", 16),
            wraplength=450,
            justify="center"
        ).pack(pady=(0, 30))

        '''# Opcional: botón de acción para empezar
        ctk.CTkButton(
            self.content,
            text="Comenzar",
            width=200,
            height=40,
            fg_color="#6678AF",
            hover_color="#5566AA"
        ).pack(pady=(0, 20))'''

    def show_monitoring_page(self):
        self.clear_content()
        ctk.CTkLabel(self.content, text="📊 Control Documental", font=("Arial", 26, "bold")).pack(pady=15)

        btn_frame = ctk.CTkFrame(self.content, fg_color="transparent")
        btn_frame.place(relx=0.5, rely=0.5, anchor="center")
        btn_frame.grid_columnconfigure(0, weight=1)

        btns_info = [
            ("Informe de Progreso", "#1E88E5",
             lambda: show_progress_in_content(self.content, lambda: run_script_and_copy_excel(
                 os.path.join(script_dir, "utils/monitoring_report.py"),
                 f"monitoring_report_{today_date_str}.xlsx"),
                                              callback=lambda: self.show_monitoring_page())),
            ("Reclamaciones (vía Email)", "#F39C12",
             lambda: show_progress_in_content(self.content, lambda: run_script(
                 os.path.join(script_dir, "utils/reclamations.py")),
                                              callback=lambda: self.show_monitoring_page())),
            ("Historial de revisiones", "#FF7F50",
             lambda: show_progress_in_content(self.content, lambda: run_script(
                 os.path.join(script_dir, "utils/revision_history.py")),
                                              callback=lambda: self.show_monitoring_page())),
            ("OVR Report", "#9B59B6",
             lambda: show_progress_in_content(self.content, lambda: run_script_and_copy_excel(
                 os.path.join(script_dir, "utils/ovr_automation.py"),
                 f"OVR_Report_{today_date_str}.xlsx"),
                                              callback=lambda: self.show_monitoring_page())),
        ]

        for i, (text, color, cmd) in enumerate(btns_info):
            btn = ctk.CTkButton(
                btn_frame,
                text=text,
                command=cmd,
                fg_color=color,
                text_color="white",
                font=("Arial", 12, "bold"),
                corner_radius=8,
                height=50,
                width=230
            )
            btn.grid(row=i, column=0, pady=8, padx=8, sticky="ew")

    def show_devoluciones_page(self):
        self.clear_content()
        ctk.CTkLabel(self.content, text="📦 Devolución de documentos", font=("Arial", 26, "bold")).pack(pady=15)

        logos = {
            "Técnicas Reunidas": ("utils/img/tr_logo.png", "utils/tr_email_mapi_automation.py"),
            "Wood / Prodoc": ("utils/img/prodoc_logo.png", "utils/prodoc_email_mapi_automation.py"),
            "GAIA / Technip": ("utils/img/gaia_logo.png", "utils/gaia_email_mapi_automation.py"),
            "Plantilla": ("utils/img/plantilla_devoluciones.png", None),
        }

        frame = ctk.CTkFrame(self.content, fg_color="transparent")
        frame.pack(pady=8)

        for i, (label, (img, script)) in enumerate(logos.items()):
            logo_img = load_image(img, (75, 75))
            if script:
                cmd = lambda s=script: run_script(os.path.join(script_dir, s))
            else:
                cmd = lambda: os.startfile(os.path.join(script_dir, "utils/plantilla_devoluciones.xlsm"))
            btn = ctk.CTkButton(
                frame,
                image=logo_img,
                text=label,
                compound="top",
                command=cmd,
                fg_color="#2C3E50",
                hover_color="#34495E",
                corner_radius=8,
                width=110,
                height=130
            )
            btn.image = logo_img
            btn.grid(row=0, column=i, padx=10, pady=6)

# === EJECUCIÓN ===
if __name__ == "__main__":
    root = DocuControlApp()
    root.mainloop()
