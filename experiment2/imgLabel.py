# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imgLabel.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cv2


class Ui_Form(object):
    def setupUi(self, Form):
        self.Form = Form
        self.Form.setObjectName("Form")
        self.Form.resize(600, 450)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 30, 521, 420))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setBackgroundRole(QtGui.QPalette.Dark)
        self.label.setAutoFillBackground(True)

        self.verticalLayout.addWidget(self.label)

        #显示图像按钮
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.clicked.connect(self.showImage)

        self.cancel = QtWidgets.QPushButton()
        self.cancel.clicked.connect(self.cancelShow)

        #添加布局
        self.contorlLayout = QtWidgets.QHBoxLayout()
        self.contorlLayout.addStretch()
        self.contorlLayout.addWidget(self.pushButton)
        self.contorlLayout.addWidget(self.cancel)
        self.contorlLayout.addStretch()

        self.verticalLayout.addLayout(self.contorlLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "No Image"))
        self.pushButton.setText(_translate("Form", "SHOW IMG"))
        self.cancel.setText(_translate("Form", "Cancel"))

    def showImage(self):
        img = cv2.imread('/Users/heguangqin/Pictures/source_1.jpg')
        rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.qimage = QtGui.QImage(rgbImg.data,rgbImg.shape[1],rgbImg.shape[0],QtGui.QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.qimage))

    def cancelShow(self):
        self.label.setText("NO IMG")
        # filename , _ = QtWidgets.QFileDialog.getOpenFileName(self.Form,"Open File",QtCore.QDir.currentPath())
        # print filename


app = QtWidgets.QApplication(sys.argv)
form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(form)
form.show()
sys.exit(app.exec_())