
import os
from PyQt6 import QtCore, QtGui, QtWidgets
import pymysql
from config import db_name, password, user, host
import webbrowser
class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(450, 730)
                MainWindow.setMaximumSize(QtCore.QSize(450, 730))
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("Iconka4.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                MainWindow.setWindowIcon(icon)
                MainWindow.setStyleSheet("background: rgba(152, 206, 252, 0.8);")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(0, 50, 441, 261))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.label.setFont(font)
                self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
        "color:rgba(0, 0, 0, 70%);\n"
        "")
                self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(80, 420, 271, 61))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
        "color:rgba(0, 0, 0, 70%);\n"
        "")
                self.label_2.setObjectName("label_2")
                self.back_btn = QtWidgets.QPushButton(self.centralwidget)
                self.back_btn.setGeometry(QtCore.QRect(140, 590, 171, 61))
                self.back_btn.setMaximumSize(QtCore.QSize(730, 450))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.back_btn.setFont(font)
                self.back_btn.setStyleSheet("QPushButton {\n"
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
                self.back_btn.setObjectName("back_btn")
                self.back_btn.clicked.connect(self.back)
                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(60, 490, 321, 51))
                self.label_3.setStyleSheet("background: rgba(0, 0, 0, 0.05);\n"
        "border-radius: 13px;")
                self.label_3.setText("")
                self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(60, 250, 321, 51))
                self.label_4.setStyleSheet("background: rgba(0, 0, 0, 0.05);\n"
        "border-radius: 13px;")
                self.label_4.setText("")
                self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.label_4.setObjectName("label_4")
                self.label_9 = QtWidgets.QLabel(self.centralwidget)
                self.label_9.setGeometry(QtCore.QRect(40, 30, 70, 70))
                self.label_9.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                self.label_9.setText("")
                self.label_9.setPixmap(QtGui.QPixmap("Iconka4.png"))
                self.label_9.setObjectName("label_9")
                self.sber_btn = QtWidgets.QPushButton(self.centralwidget)
                self.sber_btn.setGeometry(QtCore.QRect(180, 320, 100, 100))
                self.sber_btn.setMaximumSize(QtCore.QSize(730, 450))
                font = QtGui.QFont()
                self.sber_btn.clicked.connect(lambda: webbrowser.open('https://vk.com/away.php?to=https%3A%2F%2Fwww.sberbank.ru%2Fru%2Fperson%2Fcontributions%2Fdeposits%2Fnakopi&el=snippet'))
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
                self.sber_btn.setText("")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("sber.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.sber_btn.setIcon(icon1)
                self.sber_btn.setIconSize(QtCore.QSize(100, 100))
                self.sber_btn.setObjectName("sber_btn")
                self.info()
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Family money"))
                self.label.setText(_translate("MainWindow", "Рекомендуется \n"
        "перейти на сайт сбербанка и \n"
        "положить установленную сумму на \n"
        "счет накопления"))
                self.label_2.setText(_translate("MainWindow", "До вашей цели вам осталось"))
                self.back_btn.setText(_translate("MainWindow", "назад"))
        def back(self):
                MainWindow.close()
                os.system("python bluediagram.py")
        def info(self):
                with open('123.txt','r') as file:
                        self.x = file.read()
                engine = pymysql.connect(host=host,user=user,password=password,db=db_name)
                try: 
                        with engine.cursor() as cursor:
                                cursor.execute(f"select persent, target,ost from about where id = {self.x};")
                                self.db = cursor.fetchone()

                                engine.close() 
                except Exception as e:
                        print(e)
                self.label_4.setText(f"сумма накопления с % = {self.db[2]+self.db[2]*0.01*self.db[0]} руб")  
                self.otvet = self.db[1]- (self.db[2] + self.db[2]*0.01*self.db[0])
                self.label_3.setText(f"{self.otvet} руб")      
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
