from PyQt6 import QtCore, QtGui, QtWidgets
import pymysql
from config import db_name,user,password,host
import os
class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(450, 730)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("Iconka4.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                MainWindow.setWindowIcon(icon)
                MainWindow.setStyleSheet("background: rgba(152, 206, 252, 0.8);")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label_10 = QtWidgets.QLabel(self.centralwidget)
                self.label_10.setGeometry(QtCore.QRect(40, 30, 70, 70))
                self.label_10.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                self.label_10.setText("")
                self.label_10.setPixmap(QtGui.QPixmap("Iconka4.png"))
                self.label_10.setObjectName("label_10")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(190, 130, 81, 31))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
        "color:rgba(0, 0, 0, 70%);\n"
        "")
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(10, 170, 421, 131))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
        "color:rgba(0, 0, 0, 70%);\n"
        "")
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(10, 300, 421, 131))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.label_4.setFont(font)
                self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
        "color:rgba(0, 0, 0, 70%);\n"
        "")
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(10, 440, 421, 131))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.label_5.setFont(font)
                self.label_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
        "color:rgba(0, 0, 0, 70%);\n"
        "")
                self.label_5.setObjectName("label_5")
                self.back_btn = QtWidgets.QPushButton(self.centralwidget)
                self.back_btn.setGeometry(QtCore.QRect(140, 590, 171, 61))
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
                self.info()
                self.back_btn.setObjectName("back_btn")
                self.back_btn.clicked.connect(self.back)
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Family Money"))
                self.label_2.setText(_translate("MainWindow", "Советы"))
                self.back_btn.setText(_translate("MainWindow", "Назад"))
        def back(self):
                MainWindow.close()
                os.system("python bluediagram.py")
        def info(self):
                with open('123.txt','r') as file:
                        self.db_id = int(file.read())
                engine = pymysql.connect(host=host,user=user,password=password,db=db_name)
                try: 
                        with engine.cursor() as cursor:
                                cursor.execute('select budget,internet_price,eat_price,count_det,ost from about')
                                self.db = cursor.fetchall()
                                self.db = self.db[self.db_id-1]
                                engine.close() 
                except Exception as e:
                        print(e)
                self.values = []
                x = 100.0
                for i in range(1,5):
                        y = 100*self.db[i]/self.db[0]
                        self.values.append(y)
                        x-=y
                self.values.insert(0,x)
                self.info_count()
                
        def info_count(self):
                self.values[2] = 40.0
                if self.values[2]<30.0:
                        self.label_3.setText("Вы можете увеличить расходы на еду")    
                elif self.values[2]>50.0:
                        self.label_3.setText("Вы много едите,это может поспособствовать быстрому набору веса\n и тратам на новую одежду и спортзал")
                else:
                        self.label_3.setText("Ваши траты на еду сбалансированы,\n продолжайте в том же духе!")
                if self.values[1]>10.0:
                        self.label_4.setText("Вы тратите много денег на услуги связи и интеренета,\n советуем подключить услуги у других операторов")
                else:
                        self.label_4.setText("Все в норме, экономьте на подписках")  
                if self.values[3]>35.0:
                        self.label_5.setText("Нам кажется вы балуете своих детей") 
                elif self.values[3] == 0:
                        self.label_5.setText("у вас нет детей")        
                else: 
                        self.label_5.setText("Ваши расходы на детей в норме или даже меньше,\n вы можете позволить больше своим детям")   
                if self.values[4] == 0:
                        self.label_4.setText("Вам стоит пересмотреть ваши расходы\nи уменьшить их, чтобы начать копить на мечту!")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
