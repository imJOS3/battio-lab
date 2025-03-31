import tkinter as tk
from tkinter import messagebox
import requests

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x200")

        # Etiquetas y entradas
        tk.Label(root, text="Usuario:").pack(pady=5)
        self.entry_user = tk.Entry(root)
        self.entry_user.pack(pady=5)

        tk.Label(root, text="Contraseña:").pack(pady=5)
        self.entry_pass = tk.Entry(root, show="*")
        self.entry_pass.pack(pady=5)

        # Botón de inicio de sesión
        tk.Button(root, text="Iniciar sesión", command=self.login).pack(pady=20)

    def login(self):
        username = self.entry_user.get()
        password = self.entry_pass.get()

        if not username or not password:
            messagebox.showwarning("Error", "Por favor, completa todos los campos.")
            return

        url = "http://127.0.0.1:5000/login"  # Ajusta esta URL según tu backend
        data = {"username": username, "password": password}

        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")
            else:
                messagebox.showerror("Error", "Credenciales incorrectas.")
        except requests.exceptions.RequestException:
            messagebox.showerror("Error", "No se pudo conectar con el servidor.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
