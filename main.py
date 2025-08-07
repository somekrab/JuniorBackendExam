from controller.loginControl import LoginController
from view.loginView import LoginView

def main():
    controller = LoginController()
    view = LoginView(controller)
    view.run()
    controller.close()

if __name__ == "__main__":
    main()