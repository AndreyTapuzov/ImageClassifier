from Source.UI.FindImagesWindow.Ui_FindImagesWindow import Ui_FindImagesWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Source.CnnSource.ResNet50Executor import ResNet50Executor
import Source.Common.Constants as Const
import glob, os, csv
from Source.Common.Constants import RESNET50_MODEL_PATH
import numpy as np

class FindImagesWindow(Ui_FindImagesWindow):

    def __init__(self):
        self.__q_window_widget = QtWidgets.QWidget()
        self.setupUi(self.__q_window_widget)
        self.init()

    def show(self):
        self.__q_window_widget.show()

    def init(self):
        self.res_net_executor = ResNet50Executor(RESNET50_MODEL_PATH)
        self.init_image_classes_list_view()
        self.BrowseDirectoryBtn.clicked.connect(self.select_directory)
        self.FindImagesBtn.clicked.connect(self.find_images)
        self.SearchingForImagesLabel.hide()

        self.FoundImagesListView.clicked.connect(self.on_found_list_item_changed)

    def select_directory(self):
        self.directory_path = QtWidgets.QFileDialog.getExistingDirectory(self.__q_window_widget, "Select Directory")

        self.DirectoryPathTextBox.setText(self.directory_path)

    def find_images(self):
        classes_for_search = self.get_classes_for_search()

        if(len(classes_for_search) == 0):
            QtWidgets.QErrorMessage(self.__q_window_widget).showMessage("No selected classes for search")
            return

        if len(self.directory_path) == 0 | str.isspace(self.directory_path):
            QtWidgets.QErrorMessage(self.__q_window_widget).showMessage("Directory path can not be empty")
            return

        self.SearchingForImagesLabel.show()

        all_images = []
        for file_type in Const.IMAGE_EXTENSIONS:
            QtCore.QCoreApplication.processEvents()
            all_images.extend(glob.glob(self.directory_path + "/**/" + file_type, recursive=True))

        found_images_listview_model = model = QtGui.QStandardItemModel(self.FoundImagesListView)
        found_images_number = 0
        for image_path in all_images:
            if(self.check_if_desired_class(image_path, classes_for_search)):
                self.add_image_to_result(image_path, found_images_listview_model)
                found_images_number += 1
                self.FoundImagesNumberLabel.setText(str(found_images_number))
            QtCore.QCoreApplication.processEvents()

        self.SearchingForImagesLabel.hide()


    def add_image_to_result(self, image_path, model):
        item = QtGui.QStandardItem()
        item.setText(image_path)
        item.setData(image_path)
        model.appendRow(item)
        self.FoundImagesListView.setModel(model)
        self.FoundImagesListView.show()

    def check_if_desired_class(self, image_path, classes):
        predicted_classes = self.res_net_executor.get_prediction_by_image_path(image_path, 1)
        if(predicted_classes[0][0][0] in classes and predicted_classes[0][0][1] >= 0.5):
            return True
        return False

    def get_image_classes(self):
        class_names = []

        with open(Const.IMAGE_CLASSES_FILE, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            for row in spamreader:
                for class_name in row:
                    class_names.append(class_name)

        return class_names

    def get_classes_for_search(self):
        classes_for_search = []
        indexes = self.ClassesToFindListView.selectionModel().selectedIndexes()
        for i, index in enumerate(indexes):
            classes_for_search.append(self.image_classes[index.row()])

        return classes_for_search

    def init_image_classes_list_view(self):
        model = QtGui.QStandardItemModel(self.ClassesToFindListView)

        self.image_classes = self.get_image_classes()

        for image_class in self.image_classes:
            item = QtGui.QStandardItem()
            item.setText(image_class)
            item.setData(image_class)
            model.appendRow(item)

        self.ClassesToFindListView.setModel(model)
        self.ClassesToFindListView.show()

    def on_found_list_item_changed(self, index):
        data = self.FoundImagesListView.model().itemData(index)
        img_path = str(list(data.values())[1])
        pixmap = QtGui.QPixmap(img_path)
        pixmap = pixmap.scaledToHeight(self.ImagePreviewLabel.height())
        pixmap = pixmap.scaledToWidth(self.ImagePreviewLabel.width())
        self.ImagePreviewLabel.setPixmap(pixmap)
