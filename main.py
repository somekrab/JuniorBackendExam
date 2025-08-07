from controller.loginControl import LoginController
from view.loginView import LoginView

# Opens the Login Screen through loginControl.py
def main():
    controller = LoginController()
    LoginView(controller)

if __name__ == "__main__":
    main()