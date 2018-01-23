# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\!Karazina\5_Course\Diploma\Programm\ImageClassifier\Source\UI\ClassifyImageWindow\ClassifyImageWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ClassifyImageWindow(object):
    def setupUi(self, ClassifyImageWindow):
        ClassifyImageWindow.setObjectName("ClassifyImageWindow")
        ClassifyImageWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        ClassifyImageWindow.resize(571, 310)
        self.ImagePathTextBox = QtWidgets.QLineEdit(ClassifyImageWindow)
        self.ImagePathTextBox.setGeometry(QtCore.QRect(80, 20, 351, 21))
        self.ImagePathTextBox.setObjectName("ImagePathTextBox")
        self.label = QtWidgets.QLabel(ClassifyImageWindow)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label.setObjectName("label")
        self.ClassifyBtn = QtWidgets.QPushButton(ClassifyImageWindow)
        self.ClassifyBtn.setGeometry(QtCore.QRect(480, 20, 75, 23))
        self.ClassifyBtn.setObjectName("ClassifyBtn")
        self.label_2 = QtWidgets.QLabel(ClassifyImageWindow)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 71, 16))
        self.label_2.setObjectName("label_2")
        self.FruitClassesLabel = QtWidgets.QLabel(ClassifyImageWindow)
        self.FruitClassesLabel.setGeometry(QtCore.QRect(10, 120, 181, 171))
        self.FruitClassesLabel.setAutoFillBackground(True)
        self.FruitClassesLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FruitClassesLabel.setTextFormat(QtCore.Qt.PlainText)
        self.FruitClassesLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.FruitClassesLabel.setObjectName("FruitClassesLabel")
        self.BrowseFileBtn = QtWidgets.QPushButton(ClassifyImageWindow)
        self.BrowseFileBtn.setGeometry(QtCore.QRect(440, 20, 31, 21))
        self.BrowseFileBtn.setObjectName("BrowseFileBtn")
        self.label_3 = QtWidgets.QLabel(ClassifyImageWindow)
        self.label_3.setGeometry(QtCore.QRect(240, 90, 101, 16))
        self.label_3.setObjectName("label_3")
        self.ImageLabel = QtWidgets.QLabel(ClassifyImageWindow)
        self.ImageLabel.setGeometry(QtCore.QRect(240, 120, 231, 171))
        self.ImageLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ImageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ImageLabel.setObjectName("ImageLabel")
        self.ClassesToDisplaySpinBox = QtWidgets.QSpinBox(ClassifyImageWindow)
        self.ClassesToDisplaySpinBox.setGeometry(QtCore.QRect(200, 50, 42, 22))
        self.ClassesToDisplaySpinBox.setMinimum(1)
        self.ClassesToDisplaySpinBox.setMaximum(10)
        self.ClassesToDisplaySpinBox.setProperty("value", 2)
        self.ClassesToDisplaySpinBox.setObjectName("ClassesToDisplaySpinBox")
        self.label_4 = QtWidgets.QLabel(ClassifyImageWindow)
        self.label_4.setGeometry(QtCore.QRect(80, 50, 111, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(ClassifyImageWindow)
        QtCore.QMetaObject.connectSlotsByName(ClassifyImageWindow)

    def retranslateUi(self, ClassifyImageWindow):
        _translate = QtCore.QCoreApplication.translate
        ClassifyImageWindow.setWindowTitle(_translate("ClassifyImageWindow", "Classify Image"))
        self.label.setText(_translate("ClassifyImageWindow", "Image path:"))
        self.ClassifyBtn.setText(_translate("ClassifyImageWindow", "Classify"))
        self.label_2.setText(_translate("ClassifyImageWindow", "Fruit Classes:"))
        self.FruitClassesLabel.setText(_translate("ClassifyImageWindow", "No classes"))
        self.BrowseFileBtn.setText(_translate("ClassifyImageWindow", "..."))
        self.label_3.setText(_translate("ClassifyImageWindow", "Image to classify:"))
        self.ImageLabel.setText(_translate("ClassifyImageWindow", "No Image"))
        self.label_4.setText(_translate("ClassifyImageWindow", "Top classes to display:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClassifyImageWindow = QtWidgets.QWidget()
    ui = Ui_ClassifyImageWindow()
    ui.setupUi(ClassifyImageWindow)
    ClassifyImageWindow.show()
    sys.exit(app.exec_())

