from re import M
from PyQt6 import QtCore, QtGui, QtWidgets
import pymysql
from config import db_name, password, user, host
import os
class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(500, 730)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("Iconka4.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                MainWindow.setWindowIcon(icon)
                MainWindow.setStyleSheet("background: rgba(152, 206, 252, 0.8);")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.sber_btn = QtWidgets.QPushButton(self.centralwidget)
                self.sber_btn.setGeometry(QtCore.QRect(30, 590, 191, 61))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.sber_btn.setFont(font)
                self.sber_btn.setStyleSheet("QPushButton {\n"
        "    border-radius: 10px;\n"
        "    background: rgba(126,216,255, 1);\n"
        "    border: 1px solid #000000;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border-radius: 10px;\n"
        "    background: rgba(86,216,255, 1);\n"
        "    border: 1px solid #000000;\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-radius: 10px;\n"
        "    background: rgba(126,216,255, 1);\n"
        "    border: 1px solid #000000;;\n"
        "}")
                self.sber_btn.setObjectName("sber_btn")
                self.sber_btn.clicked.connect(self.sber)
                self.recom_btn = QtWidgets.QPushButton(self.centralwidget)
                self.recom_btn.setGeometry(QtCore.QRect(250, 590, 171, 61))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.recom_btn.setFont(font)
                self.recom_btn.setStyleSheet("QPushButton {\n"
        "    border-radius: 10px;\n"
        "    background: rgba(126,216,255, 1);\n"
        "    border: 1px solid #000000;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border-radius: 10px;\n"
        "    background: rgba(86,216,255, 1);\n"
        "    border: 1px solid #000000;\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-radius: 10px;\n"
        "    background: rgba(126,216,255, 1);\n"
        "    border: 1px solid #000000;;\n"
        "}")
                self.recom_btn.setObjectName("recom_btn")
                self.recom_btn.clicked.connect(self.recom)
                self.label_8 = QtWidgets.QLabel(self.centralwidget)
                self.label_8.setGeometry(QtCore.QRect(40, 30, 130, 130))
                self.label_8.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                self.label_8.setText("")
                self.label_8.setPixmap(QtGui.QPixmap("Iconka4.png"))
                self.label_8.setObjectName("label_8")
                
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(-80, 140, 800, 440))
                self.label_2.setObjectName("label_2")
                self.label_2.setPixmap(QtGui.QPixmap("diaram.png"))
                MainWindow.setCentralWidget(self.centralwidget)
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)


        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Family Money"))
                self.sber_btn.setText(_translate("MainWindow", "сделать накопление"))
                self.recom_btn.setText(_translate("MainWindow", "советы"))
        def sber(self):
                MainWindow.close()
                os.system("python bluesber.py")
        def recom(self):
                MainWindow.close()
                os.system("python recom.py")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
