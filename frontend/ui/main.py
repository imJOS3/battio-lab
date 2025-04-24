import tkinter as tk
from tkinter import messagebox, font as tkfont
import requests

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BATTIO LAB")
        self.root.configure(bg="#7af40d")

        # Pantalla completa dentro del marco de Windows
        self.root.state('zoomed')  # Equivalente a maximizado

        # Fuente personalizada
        self.custom_font = tkfont.Font(family="Helvetica", size=16)
        self.title_font = tkfont.Font(family="Helvetica", size=28, weight="bold")

        # Contenedor central
        frame = tk.Frame(root, bg="#7af40d")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Título estilizado
        tk.Label(frame, text="BATTIO LAB", font=self.title_font, bg="#7af40d", fg="black").pack(pady=(0, 30))

        # Etiqueta y entrada de usuario
        tk.Label(frame, text="Usuario:", font=self.custom_font, bg="#7af40d", fg="black").pack(pady=5)
        self.entry_user = tk.Entry(frame, font=self.custom_font, width=25)
        self.entry_user.pack(pady=5)

        # Etiqueta y entrada de contraseña
        tk.Label(frame, text="Contraseña:", font=self.custom_font, bg="#7af40d", fg="black").pack(pady=5)
        self.entry_pass = tk.Entry(frame, show="*", font=self.custom_font, width=25)
        self.entry_pass.pack(pady=5)

        # Botón de inicio de sesión
        tk.Button(frame, text="Iniciar sesión", font=self.custom_font, command=self.login, bg="black", fg="white", width=20).pack(pady=30)

    def login(self):
        username = self.entry_user.get()
        password = self.entry_pass.get()

        if not username or not password:
            messagebox.showwarning("Error", "Por favor, completa todos los campos.")
            return

        url = "http://127.0.0.1:5000/auth/login"
        data = {"username": username, "password": password}

        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                token = response.json().get("access_token")
                #messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")
                messagebox.showinfo("Éxito", f"Inicio de sesión exitoso.\nToken: {token}")
    # Aquí podrías guardar el token en memoria o pasar a otra ventana
            else:
                messagebox.showerror("Error", "Credenciales incorrectas.")
        except requests.exceptions.RequestException:
            messagebox.showerror("Error", "No se pudo conectar con el servidor.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
