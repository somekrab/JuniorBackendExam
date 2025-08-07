import tkinter as tk
from tkinter import messagebox
from view.adminView import AdminView
from view.userView import UserView

class LoginView:
    def __init__(self, controller):
        self.controller = controller

        self.window = tk.Tk()
        self.window.title("Login")
        self.window.geometry("300x180")

        # Takes user input for username
        tk.Label(self.window, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self.window)
        self.username_entry.pack()

        # Takes user input for password, displayed as "***"
        tk.Label(self.window, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self.window, show="*")
        self.password_entry.pack()

        # Login Button
        tk.Button(self.window, text="Login", command=self.handle_login).pack(pady=10)

        self.window.mainloop()

    # Method to Login 
    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user = self.controller.login(username, password)

        # If successful, Login Window closes and opens admin/user window
        if user:
            self.window.destroy()
            if user['is_admin']:
                AdminView(self.controller)
            else:
                UserView()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")