import tkinter as tk
from model.user import User

class UserView:
    def __init__(self):
        self.user_model = User() 
        self.window = tk.Tk()
        self.window.title("User View")
        self.window.geometry("500x500")

        tk.Label(self.window, text="Non-Admin Users", font=("Arial", 14)).pack(pady=10)

        self.user_listbox = tk.Listbox(self.window, width=40)
        self.user_listbox.pack(padx=20, pady=10)

        self.load_users()

        # Closes the Window
        tk.Button(self.window, text="Close", command=self.window.destroy).pack(pady=10)

        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.window.mainloop()

    def load_users(self):
        users = self.user_model.get_non_admin_users()
        for user in users:
            self.user_listbox.insert(tk.END, user)

    def on_close(self):
        self.user_model.close()
        self.window.destroy()