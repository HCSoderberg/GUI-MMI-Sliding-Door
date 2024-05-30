from models.mainModel import Model
from views.mainView import View
from controllers.mainController import Controller

def main():
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.start()

if __name__ == "__main__":
    main()