import tkinter as tk
from tkinter import messagebox
from gestion_usuarios import GestionUsuarios  # Importamos el módulo de gestión de usuarios
from gestion_productos import GestionProductos  # Importamos el módulo de gestión de productos

class AdminPanel:
    def __init__(self, root, on_logout_callback):
        self.root = root
        self.root.title("BATTIOLAB - Panel de Administración")
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
            "Gestión de Usuarios",
            "Gestión de Productos",  # Nueva opción agregada
            "Control de Stock",
            "Historial General",
            "Estado de Sincronización"
        ]

        for option in options:
            btn = tk.Button(sidebar, text=option, bg="#0B3D0B", fg="white",
                            font=("Helvetica", 10), bd=0, activebackground="#145214",
                            command=lambda opt=option: self.cargar_modulo(opt))
            btn.pack(pady=10, anchor="w", padx=10)

        # ==== ZONA PRINCIPAL ====
        self.main_area = tk.Frame(root, bg="#DFF6DD")
        self.main_area.pack(side="right", fill="both", expand=True)

        # Título superior
        title_main = tk.Label(self.main_area, text="Panel Principal", bg="#DFF6DD", fg="#0B3D0B",
                              font=("Helvetica", 20, "bold"))
        title_main.pack(pady=20)

        # Botón Cerrar sesión
        logout_btn = tk.Button(self.main_area, text="Cerrar sesión", bg="#0B3D0B", fg="white",
                               font=("Helvetica", 10), command=self.logout)
        logout_btn.place(relx=0.95, rely=0.02, anchor="ne")

        # Contenedor para cambiar frames dinámicamente
        self.content_frame = tk.Frame(self.main_area, bg="#DFF6DD")
        self.content_frame.pack(fill="both", expand=True)

        # Mostrar botones funcionales (solo al inicio)
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
        # Limpiamos el contenido actual
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Cargar el módulo correspondiente
        if opcion == "Gestión de Usuarios":
            frame = GestionUsuarios(self.content_frame)
            frame.pack(fill="both", expand=True)
        elif opcion == "Gestión de Productos":
            frame = GestionProductos(self.content_frame)  # Cargamos el módulo de gestión de productos
            frame.pack(fill="both", expand=True)
        else:
            label = tk.Label(self.content_frame, text=f"Módulo en desarrollo: {opcion}",
                             font=("Helvetica", 14), bg="#DFF6DD", fg="#0B3D0B")
            label.pack(pady=100)

    def logout(self):
        confirm = messagebox.askyesno("Cerrar sesión", "¿Estás seguro que quieres salir?")
        if confirm:
            self.root.destroy()
            self.on_logout_callback()
