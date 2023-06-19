# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtube_shorts/application/design/main-window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(672, 441)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(15, 11, 641, 131))
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 150, 511, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addAccount = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addAccount.setObjectName("addAccount")
        self.horizontalLayout.addWidget(self.addAccount)
        self.delAccount = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.delAccount.setObjectName("delAccount")
        self.horizontalLayout.addWidget(self.delAccount)
        self.genVideo = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.genVideo.setObjectName("genVideo")
        self.horizontalLayout.addWidget(self.genVideo)
        self.uploadVideo = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.uploadVideo.setObjectName("uploadVideo")
        self.horizontalLayout.addWidget(self.uploadVideo)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 190, 121, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.fragmentInVideo = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.fragmentInVideo.setMinimum(1)
        self.fragmentInVideo.setMaximum(10)
        self.fragmentInVideo.setObjectName("fragmentInVideo")
        self.verticalLayout_2.addWidget(self.fragmentInVideo)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.widthVideo = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.widthVideo.setMaximum(10000)
        self.widthVideo.setSingleStep(10)
        self.widthVideo.setProperty("value", 1080)
        self.widthVideo.setObjectName("widthVideo")
        self.verticalLayout_2.addWidget(self.widthVideo)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.heightVideo = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.heightVideo.setMaximum(10000)
        self.heightVideo.setSingleStep(10)
        self.heightVideo.setProperty("value", 1920)
        self.heightVideo.setObjectName("heightVideo")
        self.verticalLayout_2.addWidget(self.heightVideo)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.videoDelayMin = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.videoDelayMin.setSingleStep(0.1)
        self.videoDelayMin.setProperty("value", 3.0)
        self.videoDelayMin.setObjectName("videoDelayMin")
        self.verticalLayout_2.addWidget(self.videoDelayMin)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.videoDelayMax = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.videoDelayMax.setSingleStep(0.1)
        self.videoDelayMax.setProperty("value", 10.0)
        self.videoDelayMax.setObjectName("videoDelayMax")
        self.verticalLayout_2.addWidget(self.videoDelayMax)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(410, 190, 121, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.videoTitle = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.videoTitle.setObjectName("videoTitle")
        self.verticalLayout_3.addWidget(self.videoTitle)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.videoDescription = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.videoDescription.setDocumentTitle("")
        self.videoDescription.setObjectName("videoDescription")
        self.verticalLayout_3.addWidget(self.videoDescription)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 190, 251, 91))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.email = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.email.setObjectName("email")
        self.verticalLayout_5.addWidget(self.email)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_5.addWidget(self.label_12)
        self.password = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.password.setObjectName("password")
        self.verticalLayout_5.addWidget(self.password)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(540, 150, 84, 81))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.publicAccess = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.publicAccess.setChecked(True)
        self.publicAccess.setObjectName("publicAccess")
        self.verticalLayout_6.addWidget(self.publicAccess)
        self.privateAccess = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.privateAccess.setObjectName("privateAccess")
        self.verticalLayout_6.addWidget(self.privateAccess)
        self.linkAccess = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.linkAccess.setObjectName("linkAccess")
        self.verticalLayout_6.addWidget(self.linkAccess)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(540, 240, 101, 41))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.scheduleUploadVideo = QtWidgets.QTimeEdit(self.verticalLayoutWidget_6)
        self.scheduleUploadVideo.setMaximumDate(QtCore.QDate(2000, 1, 5))
        self.scheduleUploadVideo.setTime(QtCore.QTime(1, 0, 0))
        self.scheduleUploadVideo.setObjectName("scheduleUploadVideo")
        self.verticalLayout_7.addWidget(self.scheduleUploadVideo)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(540, 290, 101, 41))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10)
        self.videoCount = QtWidgets.QSpinBox(self.verticalLayoutWidget_7)
        self.videoCount.setMinimum(1)
        self.videoCount.setMaximum(1000)
        self.videoCount.setObjectName("videoCount")
        self.verticalLayout_8.addWidget(self.videoCount)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Загрузчик видео"))
        self.addAccount.setText(_translate("MainWindow", "Добавить аккаунт"))
        self.delAccount.setText(_translate("MainWindow", "Удалить аккаунт"))
        self.genVideo.setText(_translate("MainWindow", "Сгенерировать видео"))
        self.uploadVideo.setText(_translate("MainWindow", "Выложить видео"))
        self.label_5.setText(_translate("MainWindow", "Фрагментов"))
        self.label.setText(_translate("MainWindow", "Ширина"))
        self.label_2.setText(_translate("MainWindow", "Высота"))
        self.label_3.setText(_translate("MainWindow", "Длина фрагмента мин."))
        self.label_4.setText(_translate("MainWindow", "Длина фрагмента макс."))
        self.label_6.setText(_translate("MainWindow", "Название видео"))
        self.videoTitle.setPlaceholderText(_translate("MainWindow", "Просто видео #shorts"))
        self.label_7.setText(_translate("MainWindow", "Описание"))
        self.videoDescription.setPlaceholderText(_translate("MainWindow", "Какое-то описание"))
        self.label_11.setText(_translate("MainWindow", "Email"))
        self.email.setPlaceholderText(_translate("MainWindow", "test_email@gmail.com"))
        self.label_12.setText(_translate("MainWindow", "Password"))
        self.password.setPlaceholderText(_translate("MainWindow", "qwerty123"))
        self.label_8.setText(_translate("MainWindow", "Доступ"))
        self.publicAccess.setText(_translate("MainWindow", "Публичный"))
        self.privateAccess.setText(_translate("MainWindow", "Приватный"))
        self.linkAccess.setText(_translate("MainWindow", "По ссылке"))
        self.label_9.setText(_translate("MainWindow", "Период выгрузки"))
        self.label_10.setText(_translate("MainWindow", "Количество видео"))