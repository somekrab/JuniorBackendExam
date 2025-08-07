from controller.loginControl import LoginController
from view.loginView import LoginView

def main():
    controller = LoginController()
    LoginView(controller)

if __name__ == "__main__":
    main()