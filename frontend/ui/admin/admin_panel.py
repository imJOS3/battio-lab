import tkinter as tk
from tkinter import messagebox
from ui.admin.gestion_usuarios import GestionUsuarios
from ui.admin.gestion_productos import GestionProductos
from ui.admin.gestion_clientes import GestionClientes
from ui.admin.gestion_empleados import GestionEmpleados
from ui.admin.gestion_servicios import GestionServicios
from ui.admin.gestion_precioManoDeObra import GestionPrecioManoDeObra


class AdminPanel:
    def __init__(self, root, on_logout_callback):
        self.root = root
        self.root.title("BATTIOLAB - Panel de Administración")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg="#121212")

        self.on_logout_callback = on_logout_callback

        # ==== SIDEBAR ====
        sidebar = tk.Frame(root, bg="#1f1f1f", width=260)
        sidebar.pack(side="left", fill="y")

        title = tk.Label(sidebar, text="BATTIOLAB", bg="#1f1f1f", fg="#00ff99",
                         font=("Helvetica", 22, "bold"))
        title.pack(pady=40)

        self.options = [
            "Gestión de Usuarios",
            "Gestión de Productos",
            # "Control de Stock",
            "Clientes",
            "Empleados",
            # "Facturas",
            "Precios Mano de Obra",
            # "Roles",
            "Servicios",
        ]

        for option in self.options:
            btn = tk.Button(sidebar, text=option, font=("Helvetica", 14, "bold"),
                            bg="#1f1f1f", fg="white", activebackground="#00ff99",
                            activeforeground="#000000", bd=0, height=2,
                            command=lambda opt=option: self.cargar_modulo(opt))
            btn.pack(fill="x", padx=30, pady=10)

            # Efecto hover
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#00ff99", fg="#000000"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#1f1f1f", fg="white"))

        # ==== ÁREA PRINCIPAL ====
        self.main_area = tk.Frame(root, bg="#121212")
        self.main_area.pack(side="right", fill="both", expand=True)

        # === Encabezado ===
        top_frame = tk.Frame(self.main_area, bg="#121212")
        top_frame.pack(fill="x", padx=40, pady=30)

        title_main = tk.Label(top_frame, text="Panel Principal", bg="#121212", fg="#00ff99",
                              font=("Helvetica", 30, "bold"))
        title_main.pack(side="left")

        logout_btn = tk.Button(top_frame, text="Cerrar sesión", bg="#ff4d4d", fg="white",
                               font=("Helvetica", 12, "bold"), padx=15, pady=5,
                               activebackground="#ff1a1a", activeforeground="white",
                               command=self.logout, bd=0)
        logout_btn.pack(side="right")
        logout_btn.bind("<Enter>", lambda e: logout_btn.config(bg="#ff1a1a"))
        logout_btn.bind("<Leave>", lambda e: logout_btn.config(bg="#ff4d4d"))

        # === Contenido dinámico ===
        self.content_frame = tk.Frame(self.main_area, bg="#121212")
        self.content_frame.pack(fill="both", expand=True, padx=40, pady=20)

        self.create_main_buttons(self.content_frame, self.options)

    def create_main_buttons(self, parent, texts):
        for widget in parent.winfo_children():
            widget.destroy()

        btn_frame = tk.Frame(parent, bg="#121212")
        btn_frame.place(relx=0.5, rely=0.4, anchor="center")

        for idx, text in enumerate(texts):
            btn = tk.Button(btn_frame, text=text, width=30, height=3,
                            bg="#00ff99", fg="#000000", font=("Helvetica", 16, "bold"),
                            activebackground="#00cc77", activeforeground="#000000",
                            bd=0, command=lambda t=text: self.cargar_modulo(t))
            btn.grid(row=idx, column=0, pady=15)

            # Hover
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#00cc77"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#00ff99"))

    def cargar_modulo(self, opcion):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        if opcion == "Gestión de Usuarios":
            frame = GestionUsuarios(self.content_frame)
        elif opcion == "Gestión de Productos":
            frame = GestionProductos(self.content_frame)
        elif opcion == "Clientes":
            frame = GestionClientes(self.content_frame)
        elif opcion == "Empleados":
            frame = GestionEmpleados(self.content_frame)
        elif opcion == "Servicios":
            frame = GestionServicios(self.content_frame)
        elif opcion == "Precios Mano de Obra":
            frame = GestionPrecioManoDeObra(self.content_frame)
        else:
            frame = tk.Label(self.content_frame, text=f"🚧 Módulo en desarrollo: {opcion} 🚧",
                             font=("Helvetica", 20, "italic"), bg="#121212", fg="#00ff99")

        frame.pack(fill="both", expand=True)

    def logout(self):
        confirm = messagebox.askyesno("Cerrar sesión", "¿Estás seguro que quieres salir?")
        if confirm:
            self.root.destroy()
            self.on_logout_callback()
