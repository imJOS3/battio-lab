import tkinter as tk
from tkinter import messagebox

class TechnicianPanel:
    def __init__(self, root, on_logout_callback):
        self.root = root
        self.root.title("BATTIOLAB - Panel del Técnico")
        self.root.geometry("900x600")
        self.root.configure(bg="#DFF6DD")

        self.on_logout_callback = on_logout_callback

        # ==== LADO IZQUIERDO ====
        sidebar = tk.Frame(root, bg="#0B3D0B", width=150)
        sidebar.pack(side="left", fill="y")

        title = tk.Label(sidebar, text="BATTIOLAB", bg="#0B3D0B", fg="white",
                         font=("Helvetica", 16, "bold"))
        title.pack(pady=20)

        # Opciones del menú lateral
        options = [
            "Nuevo Trabajo",
            "Trabajos en Progreso",
            "Historial de Trabajos"
        ]

        for option in options:
            btn = tk.Button(sidebar, text=option, bg="#0B3D0B", fg="white",
                            font=("Helvetica", 10), bd=0, activebackground="#145214",
                            command=lambda opt=option: self.cargar_modulo(opt))
            btn.pack(pady=10, anchor="w", padx=10)

        # ==== ZONA PRINCIPAL ====
        self.main_area = tk.Frame(root, bg="#DFF6DD")
        self.main_area.pack(side="right", fill="both", expand=True)

        title_main = tk.Label(self.main_area, text="Panel del Técnico", bg="#DFF6DD", fg="#0B3D0B",
                              font=("Helvetica", 20, "bold"))
        title_main.pack(pady=20)

        logout_btn = tk.Button(self.main_area, text="Cerrar sesión", bg="#0B3D0B", fg="white",
                               font=("Helvetica", 10), command=self.logout)
        logout_btn.place(relx=0.95, rely=0.02, anchor="ne")

        self.content_frame = tk.Frame(self.main_area, bg="#DFF6DD")
        self.content_frame.pack(fill="both", expand=True)

        self.create_main_buttons(self.content_frame, options)

    def create_main_buttons(self, parent, texts):
        for widget in parent.winfo_children():
            widget.destroy()

        btn_frame = tk.Frame(parent, bg="#DFF6DD")
        btn_frame.pack(pady=30)

        for idx, text in enumerate(texts):
            btn = tk.Button(btn_frame, text=text, width=25, height=2,
                            bg="#0B3D0B", fg="white", font=("Helvetica", 12, "bold"),
                            command=lambda t=text: self.cargar_modulo(t))
            row = idx // 2
            col = idx % 2
            btn.grid(row=row, column=col, padx=20, pady=15)

    def cargar_modulo(self, opcion):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        if opcion == "Nuevo Trabajo":
            label = tk.Label(self.content_frame, text="Formulario: Nuevo Trabajo (a implementar)", 
                             font=("Helvetica", 14), bg="#DFF6DD", fg="#0B3D0B")
            label.pack(pady=100)
        elif opcion == "Trabajos en Progreso":
            label = tk.Label(self.content_frame, text="Trabajos en Progreso (a implementar)", 
                             font=("Helvetica", 14), bg="#DFF6DD", fg="#0B3D0B")
            label.pack(pady=100)
        elif opcion == "Historial de Trabajos":
            label = tk.Label(self.content_frame, text="Historial de Trabajos del Técnico (a implementar)", 
                             font=("Helvetica", 14), bg="#DFF6DD", fg="#0B3D0B")
            label.pack(pady=100)

    def logout(self):
        confirm = messagebox.askyesno("Cerrar sesión", "¿Estás seguro que quieres salir?")
        if confirm:
            self.root.destroy()
            self.on_logout_callback()
