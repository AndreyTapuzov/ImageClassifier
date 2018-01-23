from Source.UI.ClassifyImageWindow.Ui_ClassifyImageWindow import Ui_ClassifyImageWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Source.CnnSource.ResNet50Executor import ResNet50Executor
import Source.Common.Constants as Const
from Source.Common.Constants import RESNET50_MODEL_PATH
import numpy as np
class ClassifyImageWindow(Ui_ClassifyImageWindow):

    def __init__(self):
        self.__q_window_widget = QtWidgets.QWidget()
        self.setupUi(self.__q_window_widget)
        self.init()

    def show(self):
        self.__q_window_widget.show()

    def init(self):
        self.ClassifyBtn.clicked.connect(self.classify_image)
        self.BrowseFileBtn.clicked.connect(self.select_image)

        self.res_net_executor = ResNet50Executor(RESNET50_MODEL_PATH)

    def classify_image(self):
        img_path = self.ImagePathTextBox.text()
        if len(img_path) == 0 | str.isspace(img_path):
            QtWidgets.QErrorMessage(self.__q_window_widget).showMessage("Image path can not be empty")
            return

        top_predictions = self.ClassesToDisplaySpinBox.value()
        predicted_classes = self.get_predicted_classes(img_path, top_predictions)
        if(predicted_classes is None):
            return
        classes_label_txt = ""
        for i, classes in enumerate(predicted_classes[0]):
            classes_label_txt += "%d. This is %s : %f;\n" % (i+1, classes[0], classes[1])

        self.FruitClassesLabel.setText(classes_label_txt)

    def select_image(self):
        self.image_file_path, _= QtWidgets.QFileDialog\
            .getOpenFileName(self.__q_window_widget, "Select Image", "", "All Files (*);;png(*.png);;jpg(*.jpg);;jpeg(*.jpeg)")

        self.ImagePathTextBox.setText(self.image_file_path)
        try:
            pixmap = QtGui.QPixmap(self.image_file_path)
            pixmap = pixmap.scaledToHeight(self.ImageLabel.height())
            pixmap = pixmap.scaledToWidth(self.ImageLabel.width())
            self.ImageLabel.setPixmap(pixmap)
        except Exception:
            self.ImageLabel.setText(Const.NO_IMAGE_MESSAGE)

        self.FruitClassesLabel.setText(Const.NO_CLASSES_MESSAGE)

    def get_predicted_classes(self, img_path, top_predictions):
        predicted_classes = None
        try:
            predicted_classes = self.res_net_executor.get_prediction_by_image_path(img_path, top_predictions)
        except FileNotFoundError:
            QtWidgets.QErrorMessage(self.__q_window_widget).showMessage("Image file was not found")
        except OSError as e:
            QtWidgets.QErrorMessage(self.__q_window_widget).showMessage(e.strerror)
        except Exception:
            QtWidgets.QErrorMessage(self.__q_window_widget).showMessage("Unexpected error during prediction")
        return  predicted_classes

