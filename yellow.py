from PyQt6 import QtCore, QtGui, QtWidgets
import os
import pymysql
import matplotlib.pyplot as plt
import numpy as np
import random
from config import host,password,user, db_name
class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(450, 730)
                MainWindow.setMaximumSize(QtCore.QSize(450, 730))
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("Iconka4.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                MainWindow.setWindowIcon(icon)
                MainWindow.setStyleSheet("background: rgba(245, 218, 118, 0.8);")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.start_btn = QtWidgets.QPushButton(self.centralwidget)
                self.start_btn.setGeometry(QtCore.QRect(100, 570, 251, 61))
                font = QtGui.QFont()
                font.setPointSize(16)
                self.start_btn.setFont(font)
                self.start_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background: rgba(244, 249, 17, 0.45);\n"
"    border: 1px solid #000000;\n"

"}\n"
"\n"
"QPushButton:hover {\n"
"    border-radius: 10px;\n"
"    background: rgba(244, 249, 17, 0.8);\n"
"    border: 1px solid #000000;\n"

"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-radius: 10px;\n"
"    background: rgba(244, 249, 17, 0);\n"
"    border: 1px solid #000000;\n"

"}")
                self.start_btn.setObjectName("start_btn")
                self.start_btn.clicked.connect(self.start)
                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(100, 290, 251, 141))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.label_6.setFont(font)
                self.label_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
        "color:rgba(0, 0, 0, 70%);\n"
"")
                self.label_6.setTextFormat(QtCore.Qt.TextFormat.AutoText)
                self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.label_6.setObjectName("label_6")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(160, 490, 151, 41))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.label.setFont(font)
                self.label.setObjectName("label")
                self.label_7 = QtWidgets.QLabel(self.centralwidget)
                self.label_7.setGeometry(QtCore.QRect(105, 70, 241, 191))
                self.label_7.setStyleSheet("")
                self.label_7.setText("")
                self.label_7.setPixmap(QtGui.QPixmap("Iconka3.png"))
                self.label_7.setObjectName("label_7")
                MainWindow.setCentralWidget(self.centralwidget)


                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Family Money"))
                self.start_btn.setText(_translate("MainWindow", "Начать"))
                self.label_6.setText(_translate("MainWindow", "Оптимизируйте \n"
        "свой бюджет с \n"
        "нами"))
                self.label.setText(_translate("MainWindow", "Жми “начать”"))
      
        def start(self):
                try:
                        with open("123.txt",'r') as file:
                                a = file.read()
                        self.diaram()
                        MainWindow.close()
                        os.system("python bluediagram.py")            

                except Exception as e:
                        engine = pymysql.connect(host=host,user=user,password=password,db=db_name)
                        try: 
                                with engine.cursor() as cursor:
                                        cursor.execute("select id from about;")    
                                        self.b = cursor.fetchall()
                                        self.b = max(self.b)
                                        self.b = self.b[0]+1
                                        cursor.execute(f"insert into about (id) values ({self.b});")
                                        engine.commit()
                                        engine.close()      
                                with open('123.txt','w') as file:
                                        file.write(str(self.b))      
                        except Exception as e:
                                print(e)
                        MainWindow.close()
                        os.system("python pink.py")
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
                for i in range(1,len(self.db)):
                        if self.db[i]!=0:
                                if i == 1:
                                        label.append('Связь')
                                elif i == 2:
                                        label.append('Еда')
                                else:
                                        label.append('Дети')        
                colors = []    
                for i in range(len(label)):
                        color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
                        colors.append(color[0])       
                # colors = ['red','blue','purple','green']
                expl = [0.3]
                for i in range(len(colors)-1):
                        expl.append(0)

                values = []
                x = 100.0
                for i in range(1,len(colors)):
                        y = 100*self.db[i]/self.db[0]
                        values.append(y)
                        x-=y
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

