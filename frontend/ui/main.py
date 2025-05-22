import tkinter as tk
from tkinter import messagebox, font as tkfont
import requests
from login import run_login

# Colores base

if __name__ == "__main__":
    run_login()
# Panel de administración
def open_admin_panel():
    from admin_panel import AdminPanel
    root = tk.Tk()
    app = AdminPanel(root, return_to_login)
    root.mainloop()

# Volver al login
def return_to_login():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
