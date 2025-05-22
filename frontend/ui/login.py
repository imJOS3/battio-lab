# login.py
import tkinter as tk
from tkinter import messagebox, font as tkfont
import requests

# Colores, clases y lógica igual al anterior 👇
# (Aquí va todo el código de la clase LoginApp, tal como te lo pasé antes)
LIGHT_THEME = {
    "bg": "#f0f4f8",
    "frame": "#ffffff",
    "text": "#333333",
    "entry_bg": "#ffffff",
    "button_bg": "#4CAF50",
    "button_fg": "#ffffff"
}

DARK_THEME = {
    "bg": "#1e1e1e",
    "frame": "#2e2e2e",
    "text": "#ffffff",
    "entry_bg": "#3c3c3c",
    "button_bg": "#5cdb95",
    "button_fg": "#000000"
}


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.theme = LIGHT_THEME  # por defecto
        self.root.title("BATTIO LAB")
        self.root.configure(bg=self.theme["bg"])
        self.root.state('zoomed')

        # Tipografías
        self.custom_font = tkfont.Font(family="Segoe UI", size=14)
        self.title_font = tkfont.Font(family="Segoe UI", size=26, weight="bold")

        # Marco contenedor
        self.frame = tk.Frame(root, bg=self.theme["frame"], bd=2, relief="flat")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        inner = tk.Frame(self.frame, bg=self.theme["frame"], padx=40, pady=40)
        inner.pack()

        # Título
        self.title_label = tk.Label(inner, text="🔒 BATTIO LAB", font=self.title_font,
                                    bg=self.theme["frame"], fg=self.theme["text"])
        self.title_label.pack(pady=(0, 30))

        # Usuario
        self.user_label = tk.Label(inner, text="👤 Usuario:", font=self.custom_font,
                                   bg=self.theme["frame"], anchor="w", fg=self.theme["text"])
        self.user_label.pack(fill="x")
        self.entry_user = tk.Entry(inner, font=self.custom_font, width=30,
                                   relief="solid", bd=1, bg=self.theme["entry_bg"])
        self.entry_user.pack(pady=(0, 15))

        # Contraseña
        self.pass_label = tk.Label(inner, text="🔑 Contraseña:", font=self.custom_font,
                                   bg=self.theme["frame"], anchor="w", fg=self.theme["text"])
        self.pass_label.pack(fill="x")
        self.entry_pass = tk.Entry(inner, show="*", font=self.custom_font, width=30,
                                   relief="solid", bd=1, bg=self.theme["entry_bg"])
        self.entry_pass.pack(pady=(0, 25))

        # Botón de inicio
        self.login_btn = tk.Button(inner, text="Iniciar sesión", font=self.custom_font,
                                   command=self.login, bg=self.theme["button_bg"],
                                   fg=self.theme["button_fg"], activebackground="#45a049", width=25)
        self.login_btn.pack(pady=(0, 15))

        # Botón para cambiar tema
        self.theme_btn = tk.Button(inner, text="Cambiar a Modo Oscuro", command=self.toggle_theme)
        self.theme_btn.pack()

    def toggle_theme(self):
        self.theme = DARK_THEME if self.theme == LIGHT_THEME else LIGHT_THEME
        self.update_theme()

    def update_theme(self):
        # Actualizar colores en tiempo real
        self.root.configure(bg=self.theme["bg"])
        self.frame.configure(bg=self.theme["frame"])
        for widget in self.frame.winfo_children()[0].winfo_children():
            if isinstance(widget, (tk.Label, tk.Button, tk.Entry)):
                widget.configure(bg=self.theme.get("entry_bg", "#fff"))
                if isinstance(widget, tk.Label):
                    widget.configure(bg=self.theme["frame"], fg=self.theme["text"])
                if isinstance(widget, tk.Button):
                    widget.configure(bg=self.theme["button_bg"], fg=self.theme["button_fg"])

        self.title_label.configure(bg=self.theme["frame"], fg=self.theme["text"])
        self.user_label.configure(bg=self.theme["frame"], fg=self.theme["text"])
        self.pass_label.configure(bg=self.theme["frame"], fg=self.theme["text"])
        self.entry_user.configure(bg=self.theme["entry_bg"])
        self.entry_pass.configure(bg=self.theme["entry_bg"])
        self.login_btn.configure(bg=self.theme["button_bg"], fg=self.theme["button_fg"])

        theme_text = "Cambiar a Modo Claro" if self.theme == DARK_THEME else "Cambiar a Modo Oscuro"
        self.theme_btn.configure(text=theme_text)

    def login(self):
        username = self.entry_user.get()
        password = self.entry_pass.get()

        # Validación visual
        self.entry_user.config(highlightthickness=2)
        self.entry_pass.config(highlightthickness=2)

        if not username:
            self.entry_user.config(highlightbackground="red", highlightcolor="red")
        else:
            self.entry_user.config(highlightbackground="gray", highlightcolor="gray")

        if not password:
            self.entry_pass.config(highlightbackground="red", highlightcolor="red")
        else:
            self.entry_pass.config(highlightbackground="gray", highlightcolor="gray")

        if not username or not password:
            messagebox.showwarning("Error", "Por favor, completa todos los campos.")
            return

        url = "http://127.0.0.1:5000/auth/login"
        data = {"username": username, "password": password}

        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                result = response.json()
                token = result.get("access_token")
                id_rol = result.get("idRol")

                messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")
                self.root.destroy()

                if id_rol == 1:
                    open_admin_panel()
                elif id_rol == 2:
                    messagebox.showinfo("Redirección", "Aquí irá el panel del técnico.")
                else:
                    messagebox.showerror("Error", "Rol no reconocido.")
            else:
                messagebox.showerror("Error", "Credenciales incorrectas.")
        except requests.exceptions.RequestException:
            messagebox.showerror("Error", "No se pudo conectar con el servidor.")

# Pero al final, en vez de ejecutar directamente, haz esto:
def run_login():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
