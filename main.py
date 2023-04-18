import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import  QApplication,QDialog,QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from folium import *

import sqlite3
my_database = sqlite3.connect('users.db')
my_database.execute('''
    ALTER TABLE PLACES ADD COLUMN DESCRIPTION TEXT NOT NULL;
''')
# my_database.commit()

# def browseImage():
#     print("browing image")
#
#     QFileDialog.getOpenFileName()
#     # imagePath = fname[0]
#     # self.bolbImage = self.convertToBinaryData(self.imagePath)
#     # self.personImg = QPixmap(self.imagePath)
#     print("selected img")
#     # self.imgLabel.setPixmap(self.personImg)
#
#
# def insertPlaces(userId,country,city,lat,lng,imgBinary):
#     my_database = sqlite3.connect('users.db')
#     my_database.execute(
#         '''INSERT INTO PLACES VALUES(?,?,?,?,?)'''
#     , (userId,country,city,lat,lng,imgBinary))
#     my_database.commit()
#     print("data inserted :)")
#
#
# def convertToBinaryData(filename):
#
#       # Convert binary format to images or files data
#       with open(filename, 'rb') as file:
#           blobData = file.read()
#       return blobData
#
#     # my_database = sqlite3.connect('places.db')
#
#
#
# if __name__ == "__main__":
#     browseImage()
print("done")
