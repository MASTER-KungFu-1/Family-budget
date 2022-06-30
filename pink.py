import sys
from PyQt6 import QtGui,QtWidgets,QtCore
from PyQt6.QtGui import QIntValidator, QDoubleValidator
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QTextEdit, QLineEdit, QTableWidget, \
    QTableWidgetItem
import pymysql
import matplotlib.pyplot as plt
import numpy as np
import random
import os
from config import db_name, password, user, host
class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(450, 730)
                MainWindow.setMaximumSize(QtCore.QSize(450, 730))
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("Iconka4.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                MainWindow.setWindowIcon(icon)
                MainWindow.setStyleSheet("background:#FCC0F3;")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.text1_lb = QtWidgets.QLabel(self.centralwidget)
                self.text1_lb.setGeometry(QtCore.QRect(20, 250, 401, 141))
                font = QtGui.QFont()
                font.setPointSize(13)
                self.text1_lb.setFont(font)
                self.text1_lb.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
        "color:rgba(0, 0, 0, 70%);\n"
        "")
                self.text1_lb.setTextFormat(QtCore.Qt.TextFormat.AutoText)
                self.text1_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.text1_lb.setObjectName("text1_lb")
                self.line1 = QtWidgets.QLineEdit(self.centralwidget)
                self.line1.setGeometry(QtCore.QRect(101, 364, 251, 41))
                self.line1.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
                self.line1.setStyleSheet("line-height: 28px;\n"
        "border: 2px solid transparent;\n"
        "border-bottom-color: #777;\n"
        "padding: .2rem 0;\n"
        "outline: none;\n"
        "background-color: transparent;\n"
        "color: #0d0c22;")
                self.line1.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
                self.line1.setObjectName("line1")
                self.text2_lb = QtWidgets.QLabel(self.centralwidget)
                self.text2_lb.setGeometry(QtCore.QRect(80, 410, 291, 101))
                font = QtGui.QFont()
                font.setPointSize(13)
                self.text2_lb.setFont(font)
                self.text2_lb.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
        "color:rgba(0, 0, 0, 70%);\n"
        "")
                self.text2_lb.setTextFormat(QtCore.Qt.TextFormat.AutoText)
                self.text2_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.text2_lb.setObjectName("text2_lb")
                self.next_btn = QtWidgets.QPushButton(self.centralwidget)
                self.next_btn.setGeometry(QtCore.QRect(100, 570, 251, 61))
                font = QtGui.QFont()
                font.setPointSize(16)
                self.next_btn.setFont(font)
                self.next_btn.setStyleSheet("QPushButton {\n"
        "    border-radius: 10px;\n"
        "    border: 1px solid #000000;\n"
        "    background: rgba(255, 69, 214, 0.65);\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border-radius: 10px;\n"
        "    border: 1px solid #000000;\n"
        "    background: rgba(255, 69, 214, 0.9);;\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-radius: 10px;\n"
        "    border: 1px solid #000000;\n"
        "    background: rgba(255, 69, 214, 0.65);\n"
        "}")
                self.next_btn.setObjectName("next_btn")
                self.line2 = QtWidgets.QLineEdit(self.centralwidget)
                self.line2.setGeometry(QtCore.QRect(100, 494, 251, 41))
                self.line2.setStyleSheet("border: 2px solid transparent;\n"
        "border-bottom-color: #777;\n"
        "padding: .2rem 0;\n"
        "outline: none;\n"
        "background-color: transparent;\n"
        "color: #0d0c22;")
                self.line2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
                self.line2.setObjectName("line2")
                self.line_shadow2 = QtWidgets.QLabel(self.centralwidget)
                self.line_shadow2.setGeometry(QtCore.QRect(100, 500, 251, 31))
                self.line_shadow2.setStyleSheet("background: rgba(0, 0, 0, 0.10);\n"
        "")
                self.line_shadow2.setText("")
                self.line_shadow2.setObjectName("line_shadow2")
                self.line_shadow1 = QtWidgets.QLabel(self.centralwidget)
                self.line_shadow1.setGeometry(QtCore.QRect(100, 370, 251, 31))
                self.line_shadow1.setStyleSheet("background: rgba(0, 0, 0, 0.10);\n"
        "")
                self.line_shadow1.setText("")
                self.line_shadow1.setObjectName("line_shadow1")
                self.picture = QtWidgets.QLabel(self.centralwidget)
                self.picture.setGeometry(QtCore.QRect(105, 70, 241, 191))
                self.picture.setStyleSheet("")
                self.picture.setText("")
                self.picture.setPixmap(QtGui.QPixmap("Iconka3.png"))
                self.picture.setObjectName("picture")
                self.comboBox = QtWidgets.QComboBox(self.centralwidget)
                self.comboBox.setGeometry(QtCore.QRect(100, 371, 251, 31))
                self.comboBox.setObjectName("comboBox")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.line_shadow2.raise_()
                self.text1_lb.raise_()
                self.text2_lb.raise_()
                self.next_btn.raise_()
                self.line_shadow1.raise_()
                self.picture.raise_()
                self.line1.raise_()
                self.line2.raise_()
                self.comboBox.raise_()
                self.pink_budget()
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Family Money"))
                self.text1_lb.setText(_translate("MainWindow", "Установите бюджет \n"
        "на месяц"))
                self.text2_lb.setText(_translate("MainWindow", "Установите % накопления"))
                self.next_btn.setText(_translate("MainWindow", "Далее"))
                self.comboBox.setItemText(0, _translate("MainWindow", "Машину"))
                self.comboBox.setItemText(1, _translate("MainWindow", "Квартиру"))
                self.comboBox.setItemText(2, _translate("MainWindow", "Путешествие"))
                self.comboBox.setItemText(3, _translate("MainWindow", "Дорогую покупку"))
        def pink_budget(self):
                self.comboBox.hide()
                self.line1.setValidator(QIntValidator(1, 99999999, self.line1))
                self.line2.setValidator(QIntValidator(1, 99, self.line2))
                with open('123.txt','r') as file:
                        self.db_id = int(file.read())
                self.next_btn.disconnect()
                self.next_btn.clicked.connect(self.pink_budget_check)
        def pink_budget_check(self):
                if self.line1.text()!='' and self.line2.text()!='' and self.line1.text().find(' ')==-1 and self.line2.text().find(' ')==-1 and self.line1.text().find('\xa0')==-1 and self.line2.text().find('\xa0')==-1 and int(self.line1.text())!=0 and int(self.line2.text())!=0:
                        self.pink_target()
                else:
                        dlg =QtWidgets.QMessageBox()
                        dlg.setWindowTitle("Ошибка")        
                        dlg.setText('Вы заполнили не все поля\n или вы поставили пробел!')
                        dlg.exec()     
        def pink_target(self):
                engine = pymysql.connect(host=host,user=user,password=password,db=db_name)
                try: 
                        with engine.cursor() as cursor:
                                cursor.execute(f"update about set budget = {int(self.line1.text())}, persent = {int(self.line2.text())} where id = {self.db_id};")
                                engine.commit()
                                engine.close() 
                except Exception as e:
                        print(e)
                self.budget = int(self.line1.text())
                self.line2.setText("")
                self.line1.hide()
                self.comboBox.show()
                self.text1_lb.setText("На что хотите накопить?")
                self.text2_lb.setText("Сумма вашей цели:")
                self.line2.setValidator(QIntValidator(1, 999999999, self.line2)) 
                
                self.next_btn.disconnect()
                self.next_btn.clicked.connect(self.pink_target_check)
        def pink_target_check(self):
                if self.line2.text()!='' and self.line2.text().find(' ')==-1 and self.line2.text().find('\xa0')==-1 :
                        self.pink_food()
                else:
                        dlg =QtWidgets.QMessageBox()
                        dlg.setWindowTitle("Ошибка")        
                        dlg.setText('Заполните поле ввода!')
                        dlg.exec() 
        def pink_food(self):
                engine = pymysql.connect(host=host,user=user,password=password,db=db_name)
                try: 
                        with engine.cursor() as cursor:
                                cursor.execute(f"update about set target = {int(self.line2.text())}, target_name = '{self.comboBox.currentText()}' where id = {self.db_id};")
                                engine.commit()
                                engine.close() 
                except Exception as e:
                        print(e)

                self.line1.setText("")
                self.line2.setText("")
                self.line2.hide()
                self.text2_lb.hide()
                self.line_shadow2.hide()
                self.comboBox.hide()
                self.text1_lb.setText("Установите месячный лимит на \n необязательные продукты \n(сладости, алкоголь, газировка)")
                self.line1.show()

                self.next_btn.disconnect()
                self.next_btn.clicked.connect(self.pink_food_check)
        def pink_food_check(self):
                f = False
                try:
                        if self.budget - int(self.line1.text())>=0:
                                self.budget -= int(self.line1.text())
                                f = True 
                except: pass                
                if self.line1.text()!='' and f and self.line1.text().find(' ')==-1 and self.line1.text().find('\xa0')==-1:
                        self.pink_link()
                elif self.line1.text() == '':
                        dlg =QtWidgets.QMessageBox()
                        dlg.setWindowTitle("Ошибка")        
                        dlg.setText('Заполните поле ввода!')
                        dlg.exec()
                else:         
                        dlg =QtWidgets.QMessageBox()
                        dlg.setWindowTitle("Ошибка")        
                        dlg.setText(f'Ваш бюджет меньше чем данная трата!\nбюджет = {self.budget}')
                        dlg.exec()         
        def pink_link(self):
                engine = pymysql.connect(host=host,user=user,password=password,db=db_name)
                try: 
                        with engine.cursor() as cursor:
                                cursor.execute(f"update about set eat_price = {int(self.line1.text())} where id = {self.db_id};")
                                engine.commit()
                                engine.close() 
                except Exception as e:
                        print(e) 

                self.line1.setText("")
                self.text1_lb.setText("Установите месячный лимит на связь \n (интернет, телефонная связь)")
                
                self.next_btn.disconnect()
                self.next_btn.clicked.connect(self.pink_link_check)
        def pink_link_check(self):
                f = False
                try:
                        if self.budget - int(self.line1.text())>=0:
                                self.budget -= int(self.line1.text())
                                f = True
                except: pass                  
                if self.line1.text()!='' and f and self.line1.text().find(' ')==-1 and self.line1.text().find('\xa0')==-1:
                        self.pink_children()
                elif self.line1.text()=='':
                        dlg =QtWidgets.QMessageBox()
                        dlg.setWindowTitle("Ошибка")        
                        dlg.setText('Заполните поле ввода!')
                        dlg.exec()
                else:         
                        dlg =QtWidgets.QMessageBox()
                        dlg.setWindowTitle("Ошибка")        
                        dlg.setText(f'Ваш бюджет меньше чем данная трата!\nбюджет = {self.budget}')
                        dlg.exec()
        def pink_children(self):

                engine = pymysql.connect(host=host,user=user,password=password,db=db_name)
                try: 
                        with engine.cursor() as cursor:
                                cursor.execute(f"update about set internet_price = {int(self.line1.text())} where id = {self.db_id};")
                                engine.commit()
                                engine.close() 
                except Exception as e:
                        print(e)

                self.line1.setText("")
                self.text1_lb.setText("Установите месячный лимит на \n игрушки детям")
                self.next_btn.disconnect()
                self.next_btn.clicked.connect(self.pink_children_check)
        def pink_children_check(self):
                f = False
                try:
                        if self.budget - int(self.line1.text())>=0:
                                self.budget -= int(self.line1.text())
                                f = True 
                except: pass                
                if self.line1.text()!='' and f and self.line1.text().find(' ')==-1 and self.line1.text().find('\xa0')==-1:
                        self.pink_child_lim()
                elif self.line1.text() == '':
                        dlg =QtWidgets.QMessageBox()
                        dlg.setWindowTitle("Ошибка")        
                        dlg.setText('Заполните поле ввода!')
                        dlg.exec()
                else:         
                        dlg =QtWidgets.QMessageBox()
                        dlg.setWindowTitle("Ошибка")        
                        dlg.setText(f'Ваш бюджет меньше чем данная трата!\nбюджет = {self.budget}')
                        dlg.exec()
                 
        def pink_child_lim(self):
                engine = pymysql.connect(host=host,user=user,password=password,db=db_name)
                try: 
                        with engine.cursor() as cursor:
                                cursor.execute(f"update about set count_det = {int(self.line1.text())} where id = {self.db_id};")
                                engine.commit()
                                engine.close() 
                except Exception as e:
                        print(e)
                self.diaram()
                MainWindow.close()  
                os.system("python bluediagram.py")
                
        def diaram(self):
                with open('123.txt','r') as file:
                        self.db_id = int(file.read())
                engine = pymysql.connect(host=host,user=user,password=password,db=db_name)
                try: 
                        with engine.cursor() as cursor:
                                cursor.execute('select budget,internet_price,eat_price,count_det from about')
                                self.db = cursor.fetchall()
                                self.db = self.db[self.db_id-1]
                                engine.close() 
                except Exception as e:
                        print(e)
                label = ['Остаток']
                info = []
                for i in range(1,len(self.db)):
                        if self.db[i]!=0:
                                if i == 1:
                                        label.append('Связь')
                                        info.append(1)
                                elif i == 2:
                                        label.append('Еда')
                                        info.append(2)
                                else:
                                        label.append('Дети')
                                        info.append(3)                           
                colors = []    
                for i in range(len(label)):
                        color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
                        colors.append(color[0])       
                expl = [0.1]
                for i in range(len(colors)-1):
                        expl.append(0)

                values = []
                x = 100.0
                for i in range(len(info)):
                        y = 100*self.db[info[i]]/self.db[0]
                        values.append(y)
                        x-=y
                if x<0.0:
                        x = 0.0        
                values.insert(0,x)
                engine = pymysql.connect(host=host,user=user,password=password,db=db_name)
                try: 
                        with engine.cursor() as cursor:
                                cursor.execute(f"update about set ost={0.01*x*self.db[0]} where id = {self.db_id};")
                                engine.commit()
                                engine.close() 
                except Exception as e:
                        print(e)         
                plt.title('Ваши расходы')
                plt.pie(values,labels=label,colors=colors,explode=expl,shadow=True,autopct='%1.1f%%',startangle=180)
                plt.axis('equal')
                plt.savefig('diaram.png',format='png',transparent=True)                

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
