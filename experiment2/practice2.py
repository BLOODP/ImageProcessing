# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'practice2.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cv2
import numpy as np

IMAGE_WIDTH = 256
IMAGE_HEIGHT = 256
IMAGE_CHANNELS = 3

TheImage = cv2.cv.CreateImage((IMAGE_WIDTH,IMAGE_HEIGHT),cv2.cv.IPL_DEPTH_8U,IMAGE_CHANNELS)





class Ui_Form(object):
    def setupUi(self, Form):
        self.Form = Form
        self.Form.setObjectName("Form")
        self.Form.resize(646, 473)

        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(39, 29, 571, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        #创建垂直布局
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")


        # piclabel 用于显示图片，设置label样式属性
        self.picLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.picLabel.sizePolicy().hasHeightForWidth())
        self.picLabel.setObjectName("picLabel")
        self.picLabel.setSizePolicy(sizePolicy)
        self.picLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.picLabel.setBackgroundRole(QtGui.QPalette.Dark)
        self.picLabel.setAutoFillBackground(True)
        self.verticalLayout.addWidget(self.picLabel)

        #创建水平布局
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # imgShowBtn用于加载图片
        self.imgShowBtn = QtWidgets.QPushButton("SHOW IMG")
        self.imgShowBtn.setObjectName("imgShowBtn")
        self.imgShowBtn.clicked.connect(self.picBtnClicked)  #将imgShowBtn的点击事件绑定到函数picBtnClicked
        self.horizontalLayout.addWidget(self.imgShowBtn)

        # degeBtn 用于图片边缘化处理
        self.edgeBtn = QtWidgets.QPushButton("Edge Detect")
        self.edgeBtn.setObjectName("edgeBtn")
        self.edgeBtn.clicked.connect(self.OnBnClickedEdgedetect)      #将edgeBtn的点击事件绑定到函数OnBnClickedEdgedetect
        self.horizontalLayout.addWidget(self.edgeBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.picLabel.setText(_translate("Form", "TextLabel"))
        # self.imgShowBtn.setText(_translate("Form", "PushButton"))
        # self.pushButton.setText(_translate("Form", "PushButton"))

    def picBtnClicked(self):
        #选择图片
        fileName , _ = QtWidgets.QFileDialog.getOpenFileName(self.Form,"Select Image","/Users/heguangqin/Pictures")
        if fileName:
            image = cv2.imread(fileName)  #读取图片
            rgbImg = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)    #将图片由BGR格式转换为RGB格式
            #将mat形式的图片转换为Iplimage
            ipl = cv2.cv.CreateImageHeader((image.shape[1],image.shape[0]),cv2.cv.IPL_DEPTH_8U,3)
            cv2.cv.SetData(ipl,rgbImg.tostring(),image.dtype.itemsize * 3 * image.shape[1])
            if not ipl:
                return
            if TheImage:
                cv2.cv.Zero(TheImage)

            self.ResizeImage(ipl)
            self.ShowImage()

    def ShowImage(self):
        imageArray = np.asarray(TheImage[:,:]) #将iplimage的图片数据提取出来转换为多维数组

        qIamge = QtGui.QImage(imageArray.data,TheImage.width,TheImage.height,QtGui.QImage.Format_RGB888)
        self.picLabel.setPixmap(QtGui.QPixmap.fromImage(qIamge))  #将图片显示在picLabel控件上


    def ResizeImage(self,ipl):
        w = ipl.width
        h = ipl.height
        theMax = max(w,h)
        scale = theMax/256
        nw = int(w/scale)
        nh = int(h/scale)
        tlx = 0 if nw > nh else int((256-nw)/2)
        tly = int((256-nh)/2) if nw > nh else 0
        cv2.cv.SetImageROI(TheImage,(tlx,tly,nw,nh))
        cv2.cv.Resize(ipl,TheImage)
        cv2.cv.ResetImageROI(TheImage)

    def OnBnClickedEdgedetect(self):
        gray = cv2.cv.CreateImage((IMAGE_WIDTH,IMAGE_HEIGHT),cv2.cv.IPL_DEPTH_8U,1)
        edge = cv2.cv.CreateImage((IMAGE_WIDTH, IMAGE_HEIGHT), cv2.cv.IPL_DEPTH_8U, 1)
        cv2.cv.CvtColor(TheImage,gray,cv2.COLOR_RGB2GRAY) #将原图转换为灰度图
        cv2.cv.Canny(gray,edge,30,100,3)     #对灰度图做边缘检测
        cv2.cv.CvtColor(edge,TheImage,cv2.COLOR_GRAY2RGB)
        self.ShowImage()




app = QtWidgets.QApplication(sys.argv)
form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(form)
form.show()
sys.exit(app.exec_())