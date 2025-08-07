import tkinter as tk
from controller.addUserControl import addUser
from model.user import User

class AdminView:
    def __init__(self, controller):
        self.controller = controller
        self.userModel= User()
        self.controlAdd = addUser(self.userModel)
        self.window = tk.Tk()
        self.window.title("Admin Panel")
        self.window.geometry("500x500")
        tk.Label(self.window, text="Admin Dashboard").pack(pady=10)

        # Add users to the database
        tk.Label(self.window, text="Add New User").pack(pady=10)

        self.username_entry = tk.Entry(self.window)
        self.username_entry.pack()
        self.password_entry = tk.Entry(self.window)
        self.password_entry.pack()
        self.is_admin_var = tk.IntVar()
        tk.Checkbutton(self.window, text="Is Admin", variable=self.is_admin_var).pack()

        tk.Button(self.window, text="Add User", command=self.add_user).pack(pady=5)
        self.status_label = tk.Label(self.window, text="")
        self.status_label.pack()

         # Section to display all users
        tk.Label(self.window, text="All Users", font=("Arial", 12)).pack(pady=10)
        self.user_listbox = tk.Listbox(self.window, width=50)
        self.user_listbox.pack(padx=20, pady=5)

        self.load_users()

        # Closes the Window
        tk.Button(self.window, text="Close", command=self.window.destroy).pack(pady=10)
        
        self.window.mainloop()

    def load_users(self):
        self.user_listbox.delete(0, tk.END)
        users = self.userModel.get_all_users()
        for user in users:
            self.user_listbox.insert(tk.END, f"{user['username']} - {'Admin' if user['is_admin'] else 'User'}")
    def add_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        is_admin = bool(self.is_admin_var.get())
        success = self.controlAdd.add_user(username, password, is_admin)
        self.load_users()
        self.status_label.config(text="User added" if success else "User exists")