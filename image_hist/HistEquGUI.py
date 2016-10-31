# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exercise1.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np



class Ui_MainWindow(object):

    def __init__(self):
        self.origin = None

    def setupUi(self, MainWindow):

        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 30, 720, 530))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        # self.widget.setObjectName("widget")
        self.origin = QtWidgets.QLabel("ORIGIN IMAGE")
        # self.label.setGeometry(QtCore.QRect(90, 130, 60, 16))
        self.origin.setObjectName("origin")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.origin.sizePolicy().hasHeightForWidth())
        self.origin.setSizePolicy(sizePolicy)
        self.origin.setAlignment(QtCore.Qt.AlignCenter)
        self.origin.setBackgroundRole(QtGui.QPalette.Dark)
        self.origin.setAutoFillBackground(True)

        self.verticalLayout.addWidget(self.origin)

        self.output = QtWidgets.QLabel("THE OUTPUT")
        self.output.setObjectName("output")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output.sizePolicy().hasHeightForWidth())
        self.output.setSizePolicy(sizePolicy)
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setBackgroundRole(QtGui.QPalette.Dark)
        self.output.setAutoFillBackground(True)


        self.verticalLayout.addWidget(self.output)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.picShow = QtWidgets.QPushButton("SHOW IMAGE")
        self.picShow.setObjectName("picShow")
        self.picShow.clicked.connect(self.selectImg)
        self.horizontalLayout.addWidget(self.picShow)

        #  对数变换
        self.log_change = QtWidgets.QPushButton("LOG CHANGE")
        self.log_change.setObjectName("change")
        self.log_change.clicked.connect(self.logChange)
        self.horizontalLayout.addWidget(self.log_change)

        # 非线性变换
        self.nonLiner_change = QtWidgets.QPushButton("NnoeLiner CHANGE")
        self.nonLiner_change.setObjectName("change")
        self.nonLiner_change.clicked.connect(self.nonLinerChange)
        self.horizontalLayout.addWidget(self.nonLiner_change)

        #  分段线性变换
        self.seg_change = QtWidgets.QPushButton("SEAM CHANGE")
        self.seg_change.setObjectName("change")
        self.seg_change.clicked.connect(self.SegchangeImg)
        self.horizontalLayout.addWidget(self.seg_change)

        self.hist_equ_btn = QtWidgets.QPushButton("HIST EQU")
        self.hist_equ_btn.setObjectName("hist_equ")
        self.hist_equ_btn.clicked.connect(self.HistEqu)
        self.horizontalLayout.addWidget(self.hist_equ_btn)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def selectImg(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self.MainWindow,"select image","/Users/heguangqin/Pictures")
        print filename
        self.originImg = cv2.imread(filename)
        self.rgbImg = cv2.cvtColor(self.originImg,cv2.COLOR_BGR2RGB)
        self.qimage = QtGui.QImage(self.rgbImg.data, self.rgbImg.shape[1], self.rgbImg.shape[0], QtGui.QImage.Format_RGB888)
        self.origin.setPixmap(QtGui.QPixmap.fromImage(self.qimage))
        self.output.setPixmap(QtGui.QPixmap.fromImage(self.qimage))


    # 分段线性变换
    def SegchangeImg(self):
        table = []
        a, b = 48, 127
        for i in range(a):
            table.append(0)
        i = 0
        for i in range(a,b):
            table.append((255*(i-a)/(b-a)))
        i = 0
        for i in range(b,256):
            table.append(255)
        # nrows,ncols,channels = self.originImg.shape
        mat = self.originImg.copy()
        array = mat.ravel()

        for k in range(len(array)):
            array[k] = table[array[k]]

        self.rgbImg = cv2.cvtColor(mat, cv2.COLOR_BGR2RGB)
        self.qimage = QtGui.QImage(self.rgbImg.data, self.rgbImg.shape[1], self.rgbImg.shape[0],
                                   QtGui.QImage.Format_RGB888)
        # self.origin.setPixmap(QtGui.QPixmap.fromImage(self.qimage))
        self.output.setPixmap(QtGui.QPixmap.fromImage(self.qimage))


    #  非线性变换
    def nonLinerChange(self):
        table = []
        for i in range(256):
            table.append(round((255**2-(i-255)**2)**0.5))
        mat = self.originImg.copy()
        array = mat.ravel()

        for k in range(len(array)):
            array[k] = table[array[k]]

        self.rgbImg = cv2.cvtColor(mat, cv2.COLOR_BGR2RGB)
        self.qimage = QtGui.QImage(self.rgbImg.data, self.rgbImg.shape[1], self.rgbImg.shape[0],
                                   QtGui.QImage.Format_RGB888)
        self.output.setPixmap(QtGui.QPixmap.fromImage(self.qimage))


    #  对数变换
    def logChange(self):
        table = []
        c = 46
        for i in range(256):
            table.append(round(c*np.log(1+i)))
        mat = self.originImg.copy()
        array = mat.ravel()

        for k in range(len(array)):
            array[k] = table[array[k]]

        self.rgbImg = cv2.cvtColor(mat, cv2.COLOR_BGR2RGB)
        self.qimage = QtGui.QImage(self.rgbImg.data, self.rgbImg.shape[1], self.rgbImg.shape[0],
                                   QtGui.QImage.Format_RGB888)
        self.output.setPixmap(QtGui.QPixmap.fromImage(self.qimage))

    def HistEqu(self):
        mat = self.originImg.copy()
        img_b, img_g, img_r = cv2.split(mat)

        equ_b = cv2.equalizeHist(img_b)
        equ_g = cv2.equalizeHist(img_g)
        equ_r = cv2.equalizeHist(img_r)

        equ = cv2.merge([equ_b, equ_g, equ_r])
        self.rgbImg = cv2.cvtColor(equ, cv2.COLOR_BGR2RGB)
        self.qimage = QtGui.QImage(self.rgbImg.data, self.rgbImg.shape[1], self.rgbImg.shape[0],
                                   QtGui.QImage.Format_RGB888)
        self.output.setPixmap(QtGui.QPixmap.fromImage(self.qimage))

import sys
app = QtWidgets.QApplication(sys.argv)
form = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(form)
form.show()
sys.exit(app.exec_())