from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(210, 305)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(210, 305))
        MainWindow.setMaximumSize(QtCore.QSize(210, 305))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: rgb(72, 72, 72);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: rgb(45, 45, 45);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 10pt \"Nirmala UI\";\n"
"    border-radius: 2px 2px 2px 2px;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(45, 45, 45);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 2px 2px 2px 2px;\n"
"    font: 10pt \"Nirmala UI\";\n"
"    font-weight: bold;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 170, 255)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 205, 3)\n"
"}\n"
"\n"
"QLabel {\n"
"    font: 12pt \"Nirmala UI\";\n"
"    color: white;\n"
"    \n"
"\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 60, 61, 21))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 91, 31))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 111, 181))
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Zhopa"))
        self.pushButton.setText(_translate("MainWindow", "Click"))
