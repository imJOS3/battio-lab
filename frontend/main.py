import tkinter as tk
from ui.login import LoginApp, run_login
from tkinter import messagebox, font as tkfont
from ui.admin.admin_panel import AdminPanel

# Panel de administración
def open_admin_panel():
    root = tk.Tk()
    app = AdminPanel(root, return_to_login)
    root.mainloop()

# Volver al login
def return_to_login():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_login()
