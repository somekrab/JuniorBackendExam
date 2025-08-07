import tkinter as tk

class AdminView:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Admin Panel")
        self.window.geometry("300x180")
        tk.Label(self.window, text="Admin Dashboard").pack(pady=10)
        tk.Label(self.window, text="Add New User").pack(pady=10)

        self.username_entry = tk.Entry(self.window)
        self.username_entry.pack()
        self.password_entry = tk.Entry(self.window, show='*')
        self.password_entry.pack()
        self.is_admin_var = tk.IntVar()
        tk.Checkbutton(self.window, text="Is Admin", variable=self.is_admin_var).pack()

        tk.Button(self.window, text="Add User", command=self.add_user).pack(pady=5)
        self.status_label = tk.Label(self.window, text="")
        self.status_label.pack()

        self.window.mainloop()

    def add_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        is_admin = bool(self.is_admin_var.get())
        success = self.controller.add_user(username, password, is_admin)
        self.status_label.config(text="User added" if success else "User exists")