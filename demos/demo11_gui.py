from PyQt6.QtWidgets import *
from windows.main_window import MainWindow


def demo_gui():
    app = QApplication([])

    window = MainWindow()

    app.exec()