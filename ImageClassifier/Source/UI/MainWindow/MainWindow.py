from Source.UI.MainWindow.Ui_MainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Source.UI.ClassifyImageWindow.ClassifyImageWindow import  ClassifyImageWindow
from Source.UI.FindImagesWindow.FindImagesWindow import FindImagesWindow

class MainWindow(Ui_MainWindow):

    def __init__(self):
        self.__q_main_window = QtWidgets.QMainWindow()
        self.setupUi(self.__q_main_window)
        self.init()

    def show(self):
        self.__q_main_window.show()

    def init(self):
        self.ClassifyImageBtn.clicked.connect(self.show_classify_image_window)
        self.FindImagesBtn.clicked.connect(self.show_find_images_window)
        self.classify_image_window = ClassifyImageWindow()
        self.find_image_window = FindImagesWindow()

    def show_classify_image_window(self):
        self.classify_image_window.show()

    def show_find_images_window(self):
        self.find_image_window.show()

