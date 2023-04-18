# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mapPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import io
import folium
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def __init__(self):
        location=(13.133932434766733, 16.103938729508073 )
        myMap = folium.map(
            title="World Map",
            location=location,
            zoom_start=2
        )

        #save map to data object
        data = io.BytesIO()
        myMap.save(data,close_file=False)




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:#16213E;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 781, 491))
        self.label.setStyleSheet("QLabel{\n"
"\n"
"background-color:white;\n"
"border-radius:10px;\n"
"border:2px solid white;\n"
"\n"
"}\n"
"")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/mapexample.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setGeometry(QtCore.QRect(20, 0, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.backBtn.setFont(font)
        self.backBtn.setStyleSheet("\n"
"QPushButton{\n"
"\n"
"background-color:#FFEBA1;\n"
"color:white;\n"
"border-radius:15px;\n"
"background-color:none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid white;\n"
"}\n"
"")
        self.backBtn.setObjectName("backBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.backBtn.setText(_translate("MainWindow", "<-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

