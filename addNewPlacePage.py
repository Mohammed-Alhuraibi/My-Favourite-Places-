# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\addNewPlacePage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QMessageBox

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QApplication,QDialog,QFileDialog
from PyQt5.QtGui import QPixmap

import sqlite3

class Ui_AddNewPlacePage(object):

    def addFavBtnPressed(self):
        print("Add btn pressed")

        # take infos from the field
        country = self.countryField.text()
        city = self.cityField.text()
        lat = self.latField.text()
        lng = self.lngField.text()
        description = self.descriptionField.toPlainText()
        print("Info taken from the field")
        if(country == "" or city == "" or lat == "" or lng == "" or description == "" ):
            print("make sure to fill the information above")
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Make sure to fill the empty fields !")
            msg.exec_()


        else:
            try:
                #connect to the database
                sqliteConnection = sqlite3.connect('users.db')
                cursor = sqliteConnection.cursor()
                print("Connected to SQLite")

                # Insert query
                sqlite_insert_blob_query = '''INSERT INTO PLACES (USER_ID,COUNTRY,CITY,LAT,LNG,IMG,DESCRIPTION) VALUES(?,?,?,?,?,?,?)'''

                # Converting human readable file into
                # binary data
                empPhoto = self.convertToBinaryData(self.imagePath)

                # Convert data into tuple format
                data_tuple = (1,country,city,float(lat),float(lng),empPhoto,description)


                # using cursor object executing our query
                cursor.execute(sqlite_insert_blob_query,data_tuple)
                sqliteConnection.commit()
                print("Image inserted sucessfully as blob into table")
                cursor.close()
            except sqlite3.Error as error:
                print("Error while retriving the data ", error)
            finally:
                sqliteConnection.close()
                print("connection closed")

            msg = QMessageBox()
            msg.setWindowTitle("Successfully Added")
            msg.setIcon(QMessageBox.Ok)
            msg.setText("Successfully Added to your favourite places")
            msg.exec_()

        self.countryField.setText("")
        self.cityField.setText("")
        self.latField.setText("")
        self.lngField.setText("")
        self.descriptionField.setPlainText("")


    def convertToBinaryData(self,filename):
          # Convert binary format to images or files data
          with open(filename, 'rb') as file:
              blobData = file.read()
          return blobData



    def browseImage(self):
        print("browing image")

        fname = QFileDialog.getOpenFileName()
        self.imagePath = fname[0]

        self.personImg = QPixmap(self.imagePath)
        self.imgSouvenir.setPixmap(self.personImg)





    def setupUi(self, AddNewPlacePage):
        AddNewPlacePage.setObjectName("AddNewPlacePage")
        AddNewPlacePage.resize(800, 603)
        AddNewPlacePage.setStyleSheet("background-color:#16213E;\n"
"")
        self.centralwidget = QtWidgets.QWidget(AddNewPlacePage)
        self.centralwidget.setObjectName("centralwidget")
        self.cityField = QtWidgets.QLineEdit(self.centralwidget)
        self.cityField.setGeometry(QtCore.QRect(180, 140, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cityField.setFont(font)
        self.cityField.setStyleSheet("QLineEdit{\n"
"\n"
"background-color:white;\n"
"border-radius:10px;\n"
"padding-left:10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border:2px solid #E94560;\n"
"}\n"
"QLineEdit:focus{\n"
"border:2px solid #E94560;\n"
"}")
        self.cityField.setText("")
        self.cityField.setObjectName("cityField")
        self.imgSouvenir = QtWidgets.QLabel(self.centralwidget)
        self.imgSouvenir.setGeometry(QtCore.QRect(510, 60, 171, 171))
        self.imgSouvenir.setStyleSheet("border-radius:15px;border:10px solid white;")
        self.imgSouvenir.setText("")
        self.imgSouvenir.setPixmap(QtGui.QPixmap("Images/havıngFun.jpg"))
        self.imgSouvenir.setScaledContents(True)
        self.imgSouvenir.setObjectName("imgSouvenir")
        self.addSouvenirImgBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addSouvenirImgBtn.setGeometry(QtCore.QRect(520, 240, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.addSouvenirImgBtn.setFont(font)
        self.addSouvenirImgBtn.setStyleSheet("background-color:#95DAC1;\n"
"color:white;\n"
"border-radius:10px;\n"
"")
        self.addSouvenirImgBtn.setObjectName("addSouvenirImgBtn")
        self.addSouvenirImgBtn.clicked.connect(self.browseImage)
        self.countryField = QtWidgets.QLineEdit(self.centralwidget)
        self.countryField.setGeometry(QtCore.QRect(180, 60, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.countryField.setFont(font)
        self.countryField.setStyleSheet("QLineEdit{\n"
"\n"
"background-color:white;\n"
"border-radius:10px;\n"
"padding-left:10px;\n"
"}\n"
"QLineEdit:hover{\n"
"border:2px solid #E94560;\n"
"}\n"
"QLineEdit:focus{\n"
"border:2px solid #E94560;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.countryField.setText("")
        self.countryField.setObjectName("countryField")
        self.descriptionField = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.descriptionField.setGeometry(QtCore.QRect(180, 280, 311, 151))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.descriptionField.setFont(font)
        self.descriptionField.setStyleSheet("QPlainTextEdit{\n"
"\n"
"background-color:white;\n"
"border-radius:10px;\n"
"padding-left:10px;\n"
"padding-top:10px;\n"
"}\n"
"\n"
"QPlainTextEdit:hover{\n"
"border:2px solid #E94560;\n"
"}\n"
"QPlainTextEdit:focus{\n"
"border:2px solid #E94560;\n"
"}")
        self.descriptionField.setObjectName("descriptionField")
        self.addToFavBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addToFavBtn.setGeometry(QtCore.QRect(190, 480, 461, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.addToFavBtn.setFont(font)
        self.addToFavBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.addToFavBtn.setStyleSheet("\n"
"QPushButton{\n"
"\n"
"background-color:#E94560;\n"
"color:white;\n"
"border-radius:25px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.addToFavBtn.setObjectName("addToFavBtn")
        self.addToFavBtn.clicked.connect(self.addFavBtnPressed)
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setGeometry(QtCore.QRect(10, 10, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.backBtn.setFont(font)
        self.backBtn.setStyleSheet("\n"
"QPushButton{\n"
"\n"
"background-color:none;\n"
"color:white;\n"
"border-radius:15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:3px solid white;\n"
"}\n"
"")
        self.backBtn.setObjectName("backBtn")
        self.latField = QtWidgets.QLineEdit(self.centralwidget)
        self.latField.setGeometry(QtCore.QRect(180, 210, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.latField.setFont(font)
        self.latField.setStyleSheet("QLineEdit{\n"
"\n"
"background-color:white;\n"
"border-radius:10px;\n"
"padding-left:10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border:2px solid #E94560;\n"
"}\n"
"QLineEdit:focus{\n"
"border:2px solid #E94560;\n"
"}")
        self.latField.setText("")
        self.latField.setObjectName("latField")
        self.lngField = QtWidgets.QLineEdit(self.centralwidget)
        self.lngField.setGeometry(QtCore.QRect(340, 210, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lngField.setFont(font)
        self.lngField.setStyleSheet("QLineEdit{\n"
"\n"
"background-color:white;\n"
"border-radius:10px;\n"
"padding-left:10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border:2px solid #E94560;\n"
"}\n"
"QLineEdit:focus{\n"
"border:2px solid #E94560;\n"
"}")
        self.lngField.setText("")
        self.lngField.setObjectName("lngField")
        AddNewPlacePage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddNewPlacePage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        AddNewPlacePage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddNewPlacePage)
        self.statusbar.setObjectName("statusbar")
        AddNewPlacePage.setStatusBar(self.statusbar)

        self.retranslateUi(AddNewPlacePage)
        QtCore.QMetaObject.connectSlotsByName(AddNewPlacePage)

    def retranslateUi(self, AddNewPlacePage):
        _translate = QtCore.QCoreApplication.translate
        AddNewPlacePage.setWindowTitle(_translate("AddNewPlacePage", "MainWindow"))
        self.cityField.setPlaceholderText(_translate("AddNewPlacePage", "city"))
        self.addSouvenirImgBtn.setText(_translate("AddNewPlacePage", "Add a souvenir photo"))
        self.countryField.setPlaceholderText(_translate("AddNewPlacePage", "country"))
        self.descriptionField.setPlaceholderText(_translate("AddNewPlacePage", "what have you done there :)"))
        self.addToFavBtn.setText(_translate("AddNewPlacePage", "Add it to my Fav"))
        self.backBtn.setText(_translate("AddNewPlacePage", "<-"))
        self.latField.setPlaceholderText(_translate("AddNewPlacePage", "Latitude"))
        self.lngField.setPlaceholderText(_translate("AddNewPlacePage", "Longitude"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddNewPlacePage = QtWidgets.QMainWindow()
    ui = Ui_AddNewPlacePage()
    ui.setupUi(AddNewPlacePage)
    AddNewPlacePage.show()
    sys.exit(app.exec_())

