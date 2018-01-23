# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\!Karazina\5_Course\Diploma\Programm\ImageClassifier\Source\UI\FindImagesWindow\FindImagesWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FindImagesWindow(object):
    def setupUi(self, FindImagesWindow):
        FindImagesWindow.setObjectName("FindImagesWindow")
        FindImagesWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        FindImagesWindow.resize(859, 509)
        self.FindImagesBtn = QtWidgets.QPushButton(FindImagesWindow)
        self.FindImagesBtn.setGeometry(QtCore.QRect(580, 10, 81, 41))
        self.FindImagesBtn.setObjectName("FindImagesBtn")
        self.DirectoryPathTextBox = QtWidgets.QLineEdit(FindImagesWindow)
        self.DirectoryPathTextBox.setGeometry(QtCore.QRect(100, 20, 411, 21))
        self.DirectoryPathTextBox.setDragEnabled(False)
        self.DirectoryPathTextBox.setObjectName("DirectoryPathTextBox")
        self.ClassesToFindListView = QtWidgets.QListView(FindImagesWindow)
        self.ClassesToFindListView.setGeometry(QtCore.QRect(20, 100, 161, 391))
        self.ClassesToFindListView.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.ClassesToFindListView.setObjectName("ClassesToFindListView")
        self.label = QtWidgets.QLabel(FindImagesWindow)
        self.label.setGeometry(QtCore.QRect(20, 70, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(FindImagesWindow)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label_2.setObjectName("label_2")
        self.BrowseDirectoryBtn = QtWidgets.QPushButton(FindImagesWindow)
        self.BrowseDirectoryBtn.setGeometry(QtCore.QRect(520, 20, 31, 21))
        self.BrowseDirectoryBtn.setObjectName("BrowseDirectoryBtn")
        self.label_3 = QtWidgets.QLabel(FindImagesWindow)
        self.label_3.setGeometry(QtCore.QRect(200, 70, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(FindImagesWindow)
        self.label_4.setGeometry(QtCore.QRect(610, 70, 131, 16))
        self.label_4.setObjectName("label_4")
        self.ImagePreviewLabel = QtWidgets.QLabel(FindImagesWindow)
        self.ImagePreviewLabel.setGeometry(QtCore.QRect(610, 100, 241, 191))
        self.ImagePreviewLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ImagePreviewLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ImagePreviewLabel.setObjectName("ImagePreviewLabel")
        self.FoundImagesNumberLabel = QtWidgets.QLabel(FindImagesWindow)
        self.FoundImagesNumberLabel.setGeometry(QtCore.QRect(280, 70, 81, 16))
        self.FoundImagesNumberLabel.setObjectName("FoundImagesNumberLabel")
        self.FoundImagesListView = QtWidgets.QListView(FindImagesWindow)
        self.FoundImagesListView.setGeometry(QtCore.QRect(200, 100, 391, 391))
        self.FoundImagesListView.setResizeMode(QtWidgets.QListView.Fixed)
        self.FoundImagesListView.setModelColumn(0)
        self.FoundImagesListView.setObjectName("FoundImagesListView")
        self.SearchingForImagesLabel = QtWidgets.QLabel(FindImagesWindow)
        self.SearchingForImagesLabel.setEnabled(True)
        self.SearchingForImagesLabel.setGeometry(QtCore.QRect(680, 20, 131, 16))
        self.SearchingForImagesLabel.setObjectName("SearchingForImagesLabel")

        self.retranslateUi(FindImagesWindow)
        QtCore.QMetaObject.connectSlotsByName(FindImagesWindow)

    def retranslateUi(self, FindImagesWindow):
        _translate = QtCore.QCoreApplication.translate
        FindImagesWindow.setWindowTitle(_translate("FindImagesWindow", "Find Images"))
        self.FindImagesBtn.setText(_translate("FindImagesWindow", "Find Images"))
        self.label.setText(_translate("FindImagesWindow", "Fruit classes to find:"))
        self.label_2.setText(_translate("FindImagesWindow", "Directory path:"))
        self.BrowseDirectoryBtn.setText(_translate("FindImagesWindow", "..."))
        self.label_3.setText(_translate("FindImagesWindow", "Found images:"))
        self.label_4.setText(_translate("FindImagesWindow", "Image preview:"))
        self.ImagePreviewLabel.setText(_translate("FindImagesWindow", "No Image"))
        self.FoundImagesNumberLabel.setText(_translate("FindImagesWindow", "0"))
        self.SearchingForImagesLabel.setText(_translate("FindImagesWindow", "Searching for images..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FindImagesWindow = QtWidgets.QWidget()
    ui = Ui_FindImagesWindow()
    ui.setupUi(FindImagesWindow)
    FindImagesWindow.show()
    sys.exit(app.exec_())

