import tkinter as tk

class UserView:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("User Window")
        self.window.geometry("300x180")
        tk.Label(self.window, text="Welcome, regular user!").pack(pady=20)
        self.window.mainloop()