# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(529, 426)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(15, 11, 491, 181))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 360, 490, 38))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.genVideo = QPushButton(self.horizontalLayoutWidget)
        self.genVideo.setObjectName(u"genVideo")

        self.horizontalLayout.addWidget(self.genVideo)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(190, 210, 173, 131))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.videoDelayMin = QDoubleSpinBox(self.verticalLayoutWidget)
        self.videoDelayMin.setObjectName(u"videoDelayMin")
        self.videoDelayMin.setSingleStep(0.100000000000000)
        self.videoDelayMin.setValue(3.000000000000000)

        self.verticalLayout_2.addWidget(self.videoDelayMin)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.videoDelayMax = QDoubleSpinBox(self.verticalLayoutWidget)
        self.videoDelayMax.setObjectName(u"videoDelayMax")
        self.videoDelayMax.setSingleStep(0.100000000000000)
        self.videoDelayMax.setValue(10.000000000000000)

        self.verticalLayout_2.addWidget(self.videoDelayMax)

        self.verticalLayoutWidget_7 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(370, 210, 138, 128))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.verticalLayoutWidget_7)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_8.addWidget(self.label_5)

        self.fragmentInVideo = QSpinBox(self.verticalLayoutWidget_7)
        self.fragmentInVideo.setObjectName(u"fragmentInVideo")
        self.fragmentInVideo.setMinimum(1)
        self.fragmentInVideo.setMaximum(10)

        self.verticalLayout_8.addWidget(self.fragmentInVideo)

        self.label_10 = QLabel(self.verticalLayoutWidget_7)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_8.addWidget(self.label_10)

        self.videoCount = QSpinBox(self.verticalLayoutWidget_7)
        self.videoCount.setObjectName(u"videoCount")
        self.videoCount.setMinimum(1)
        self.videoCount.setMaximum(1000)

        self.verticalLayout_8.addWidget(self.videoCount)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 210, 170, 128))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.widthVideo = QSpinBox(self.verticalLayoutWidget_2)
        self.widthVideo.setObjectName(u"widthVideo")
        self.widthVideo.setMaximum(10000)
        self.widthVideo.setSingleStep(10)
        self.widthVideo.setValue(1080)

        self.verticalLayout.addWidget(self.widthVideo)

        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.heightVideo = QSpinBox(self.verticalLayoutWidget_2)
        self.heightVideo.setObjectName(u"heightVideo")
        self.heightVideo.setMaximum(10000)
        self.heightVideo.setSingleStep(10)
        self.heightVideo.setValue(1920)

        self.verticalLayout.addWidget(self.heightVideo)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0447\u0438\u043a \u0432\u0438\u0434\u0435\u043e", None))
        self.genVideo.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432\u0438\u0434\u0435\u043e", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 \u0444\u0440\u0430\u0433\u043c\u0435\u043d\u0442\u0430 \u043c\u0438\u043d.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 \u0444\u0440\u0430\u0433\u043c\u0435\u043d\u0442\u0430 \u043c\u0430\u043a\u0441.", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0440\u0430\u0433\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u0438\u0434\u0435\u043e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430", None))
    # retranslateUi

