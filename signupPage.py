# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\signupPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

# from loginPage import *
from loginPage import *
import sqlite3

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import  QApplication,QDialog,QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets


class SignupPage(object):

    def signupBtnPressed(self):
        print("Signup button pressed")
        # take infos from the field
        username = self.userNameField.text()
        email = self.emailField.text()
        password = self.passwordField.text()

        #connect to the database
        sqliteConnection = sqlite3.connect('users.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        # Insert query
        sqlite_insert_blob_query = '''INSERT INTO USERS (USERNAME,EMAIL,PASSWORD,IMAGE) VALUES(?,?,?,?)'''

        # Converting human readable file into
        # binary data
        empPhoto = self.convertToBinaryData(self.imagePath)

        # Convert data into tuple format
        data_tuple = (username,email,password,empPhoto)

        # using cursor object executing our query
        cursor.execute(sqlite_insert_blob_query,data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted sucessfully as blob into table")
        cursor.close()


    def convertToBinaryData(self,filename):

      # Convert binary format to images or files data
      with open(filename, 'rb') as file:
          blobData = file.read()
      return blobData

    def goToLoginPage(self):
        print("go to login page")
        self.loginWindow = QtWidgets.QMainWindow()
        self.ui =LoginPage()
        self.ui.setupUi(self.loginWindow)
        self.loginWindow.show()
        # SignupPage.close()

        # self.loginWindow = QtWidgets.QMainWindow()
        # self.ui = Ui_LoginPage()
        # self.ui.setupUi(self.loginWindow)
        # self.loginWindow.show()
        # SignupPage.close()

    def browseImage(self):
        print("browing image")

        fname = QFileDialog.getOpenFileName()
        self.imagePath = fname[0]

        self.personImg = QPixmap(self.imagePath)
        self.imgLabel.setPixmap(self.personImg)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 600)
        MainWindow.setStyleSheet("background-color:#16213E;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 10, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 90, 601, 461))
        self.label_2.setStyleSheet("background-color:rgba(0,0,0,50);\n"
"border-radius:10px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.userNameField = QtWidgets.QLineEdit(self.centralwidget)
        self.userNameField.setGeometry(QtCore.QRect(200, 150, 250, 40))
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
        self.signupBtn = QtWidgets.QPushButton(self.centralwidget)
        self.signupBtn.setGeometry(QtCore.QRect(320, 400, 200, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.signupBtn.setFont(font)
        self.signupBtn.setStyleSheet("QPushButton#signupBtn{\n"
"\n"
"\n"
"color:white;\n"
"\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton#signupBtn:hover{\n"
"color:white;\n"
"border:2px solid #E94560;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton#signupBtn:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"border-radius:10px;\n"
"}")
        self.signupBtn.setObjectName("signupBtn")
        self.signupBtn.clicked.connect(self.signupBtnPressed)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 480, 151, 16))
        self.label_3.setStyleSheet("color:#f0f0f0;\n"
"background-color:none;")
        self.label_3.setObjectName("label_3")
        self.goToLogin = QtWidgets.QPushButton(self.centralwidget)
        self.goToLogin.setGeometry(QtCore.QRect(300, 500, 61, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.goToLogin.setFont(font)
        self.goToLogin.setStyleSheet("QPushButton#goToLogin{\n"
"text-align:left;\n"
"\n"
"background-color:none;\n"
"border:none;\n"
"color:#f0f0f0;\n"
"}\n"
"\n"
"QPushButton#goToLogin:hover{\n"
"color:white;\n"
"font-weight:800;\n"
"}\n"
"\n"
"QPushButton#goToLogin:pressed{\n"
"\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color:white;\n"
"font-weight:800;\n"
"}\n"
"\n"
"")
        self.goToLogin.setObjectName("goToLogin")
        self.goToLogin.clicked.connect(self.goToLoginPage)
        self.emailField = QtWidgets.QLineEdit(self.centralwidget)
        self.emailField.setGeometry(QtCore.QRect(200, 230, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.emailField.setFont(font)
        self.emailField.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid #533483;\n"
"color:white;\n"
"padding-left:0px;\n"
"padding-bottom:15px;")
        self.emailField.setObjectName("emailField")
        self.passwordField = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordField.setGeometry(QtCore.QRect(200, 310, 250, 40))
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
        self.imgLabel = QtWidgets.QLabel(self.centralwidget)
        self.imgLabel.setGeometry(QtCore.QRect(510, 150, 171, 171))
        self.imgLabel.setStyleSheet("border-radius:15px;\n"
"border:5px solid  #533483;\n"
"\n"
"")
        self.imgLabel.setText("")
        self.imgLabel.setPixmap(QtGui.QPixmap("Images/person.png"))
        self.imgLabel.setScaledContents(True)
        self.imgLabel.setObjectName("imgLabel")
        self.addImgBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addImgBtn.clicked.connect(self.browseImage)
        self.addImgBtn.setGeometry(QtCore.QRect(520, 330, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.addImgBtn.setFont(font)
        self.addImgBtn.setStyleSheet("\n"
"QPushButton#addImgBtn{\n"
"\n"
"\n"
"color:white;\n"
"background-color:#E94560;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton#addImgBtn:hover{\n"
"color:white;\n"
"border:2px solid  #533483;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton#addImgBtn:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"border-radius:10px;\n"
"}\n"
"")
        self.addImgBtn.setObjectName("addImgBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 21))
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
        self.label.setText(_translate("MainWindow", "Sign up"))
        self.userNameField.setPlaceholderText(_translate("MainWindow", "user name"))
        self.signupBtn.setText(_translate("MainWindow", "S i g n  u p"))
        self.label_3.setText(_translate("MainWindow", "Already have an account ?"))
        self.goToLogin.setText(_translate("MainWindow", "Login"))
        self.emailField.setPlaceholderText(_translate("MainWindow", "email"))
        self.passwordField.setPlaceholderText(_translate("MainWindow", "password"))
        self.addImgBtn.setText(_translate("MainWindow", "Add Profile Photo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SignupPage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

