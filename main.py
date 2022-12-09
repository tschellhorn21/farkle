from controller import *


def main() -> None:
    """
    This function controls the gui.
    :return: None
    """
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
