import sys
from PyQt5 import QtWidgets
from Source.UI.MainWindow import MainWindow
import numpy
def my_excepthook(type, value, tback):
    # log the exception here

    # then call the default handler
    sys.__excepthook__(type, value, tback)

sys.excepthook = my_excepthook
def run_app():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow.MainWindow()
    main_window.show()
    sys.exit(app.exec_())

run_app()

