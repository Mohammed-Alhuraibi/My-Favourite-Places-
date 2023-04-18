# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\loginPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from signupPage import *
from personPage import *
from PyQt5 import QtCore, QtGui
from  PyQt5 import QtWidgets as QtWidgets
from PyQt5.QtWidgets import QMessageBox

import sqlite3

class LoginPage(object):


    def loginBtnPressed(self):
        print("login btn pressed")
        username = self.userNameField.text()
        password = self.passwordField.text()

        if(username == "" or password == ""):
            print("make sure to fill username and password")
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Make sure to fill the empty fields !")
            msg.exec_()
        else:
            try:
                self.my_database = sqlite3.connect('users.db')
                self.cur = self.my_database.cursor()

                self.users = self.cur.execute('''SELECT ID,USERNAME,EMAIL,PASSWORD,IMAGE FROM USERS WHERE USERNAME = ? AND PASSWORD = ? ''',(username,password))
                self.userInfo = self.users.fetchall()[0]

                userInfo.user['name'] = self.userInfo[1]
                userInfo.user['id'] = self.userInfo[0]
                print(userInfo.user['name'], userInfo.user['id'])
                if(self.userInfo[1] == username):
                    print("user found")
                    self.personWindow = QtWidgets.QMainWindow()
                    self.ui = Ui_MainWindow()
                    self.ui.setupUi(self.personWindow)
                    self.personWindow.show()
                    self.loadDataToNewPage()
                    MainWindow.close()


                else:
                    print("username not found")
                    boxmes = QMessageBox()
                    boxmes.setWindowTitle("Warning")
                    boxmes.setIcon(QMessageBox.Critical)
                    boxmes.setText("user not found tray again")
                    boxmes.exec_()

            except :
                print("user not found")
                boxmes = QMessageBox()
                boxmes.setWindowTitle("Warning")
                boxmes.setIcon(QMessageBox.Critical)
                boxmes.setText("user not found tray again")
                boxmes.exec_()




    def goToSignupPage(self):
        print("go to singup page")
        self.signupWindow = QtWidgets.QMainWindow()
        self.ui = SignupPage()
        self.ui.setupUi(self.signupWindow)
        self.signupWindow.show()
        MainWindow.close()


    def loadDataToNewPage(self):
        # self.ui.username.setText(self.userInfo[1])
        imageBinary = self.userInfo[4]
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(imageBinary)
        self.ui.img.setPixmap(pixmap)






    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 600)
        MainWindow.setStyleSheet("background-color:#16213E;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 20, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 391, 461))
        self.label_2.setStyleSheet("background-color:rgba(0,0,0,50);\n"
"border-radius:10px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.userNameField = QtWidgets.QLineEdit(self.centralwidget)
        self.userNameField.setGeometry(QtCore.QRect(120, 190, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.userNameField.setFont(font)
        self.userNameField.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid #533483;\n"
"color:white;\n"
"padding-left:0px;\n"
"padding-bottom:15px;")
        self.userNameField.setObjectName("userNameField")
        self.passwordField = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordField.setGeometry(QtCore.QRect(120, 280, 250, 40))
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.passwordField.setFont(font)
        self.passwordField.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid #533483;\n"
"color:white;\n"
"padding-left:0px;\n"
"padding-bottom:15px;")
        self.passwordField.setObjectName("passwordField")
        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginBtn.setGeometry(QtCore.QRect(140, 390, 200, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.loginBtn.setFont(font)
        self.loginBtn.setStyleSheet("QPushButton#loginBtn{\n"
"\n"
"\n"
"color:white;\n"
"\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton#loginBtn:hover{\n"
"color:white;\n"
"border:2px solid #E94560;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton#loginBtn:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"border-radius:10px;\n"
"}")
        self.loginBtn.setObjectName("loginBtn")
        self.loginBtn.clicked.connect(self.loginBtnPressed)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 470, 151, 16))
        self.label_3.setStyleSheet("color:#f0f0f0;\n"
"background-color:none;")
        self.label_3.setObjectName("label_3")
        self.createOneBtn = QtWidgets.QPushButton(self.centralwidget)
        self.createOneBtn.setGeometry(QtCore.QRect(140, 490, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.createOneBtn.setFont(font)
        self.createOneBtn.setStyleSheet("QPushButton#createOneBtn{\n"
"text-align:left;\n"
"\n"
"background-color:none;\n"
"border:none;\n"
"color:#f0f0f0;\n"
"}\n"
"\n"
"QPushButton#createOneBtn:hover{\n"
"color:white;\n"
"font-weight:800;\n"
"}\n"
"\n"
"QPushButton#createOneBtn:pressed{\n"
"\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color:white;\n"
"font-weight:800;\n"
"}\n"
"\n"
"")
        self.createOneBtn.setObjectName("createOneBtn")
        self.createOneBtn.clicked.connect(self.goToSignupPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Login"))
        self.userNameField.setPlaceholderText(_translate("MainWindow", "user name"))
        self.passwordField.setPlaceholderText(_translate("MainWindow", "password"))
        self.loginBtn.setText(_translate("MainWindow", "L o g i n"))
        self.label_3.setText(_translate("MainWindow", "Don\'t have an account ?"))
        self.createOneBtn.setText(_translate("MainWindow", "Create one"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LoginPage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

