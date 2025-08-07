import tkinter as tk
from tkinter import messagebox

class LoginView:
    def __init__(self, controller):
        self.controller = controller

        self.root = tk.Tk()
        self.root.title("Login")
        self.root.geometry("300x180")

        tk.Label(self.root, text="Username").pack(pady=(10, 0))
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password").pack(pady=(10, 0))
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.try_login).pack(pady=20)

    def try_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.controller.login(username, password):
            messagebox.showinfo("Success", f"Welcome, {username}!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def run(self):
        self.root.mainloop()