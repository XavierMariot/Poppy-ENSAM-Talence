# -*- coding: utf-8 -*-

from PyQt4.QtGui import QFrame, QPushButton, QFileDialog, QPixmap, QLabel
from PyQt4.QtCore import SIGNAL

class FrameImage(QFrame):
    def __init__(self, parent, posx, posy, width, height, save=None):
        QFrame.__init__(self, parent)
        self.__width      = width
        self.__height     = height
        self.__image      = None
        self.__btnSave    = None
        self.__comment    = None
        self.__zoneImage  = QLabel(self)
        self.__comment    = QLabel(self)
        self.__xZoneImage = 0
        self.__yZoneImage = 0
        self.__save       = save

        # configure initial state
        self.setFrameShape(QFrame.Box)
        self.move(posx, posy)        
        self.resize(width,height)
        self.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.__configure()

    def __configure(self):
        # configuring comment initial position, size and content
        self.__comment.move(10, self.__height-30)
        self.__comment.resize(self.__width-10,30)
        self.__comment.setText("")
        # configuring initial button properties
        self.__btnSave = QPushButton('Save',self)
        self.__btnSave.resize(0,0)
        self.__btnSave.setToolTip('Save image in a file...')
        self.connect(self.__btnSave, SIGNAL('clicked()'), self.SaveImage)

    def ImageQ(self):
        return self.__image != None

    def GetImage(self):
        return self.__image

    def DisplayComment(self, comment):
        self.__comment.clear()
        self.__comment.setText(comment)
        self.__comment.repaint()
        
    def DisplayImage(self, image):
        self.__image = image.copy()
        pixm = QPixmap.fromImage(self.__image)
        self.__zoneImage.setPixmap(pixm)
        self.__zoneImage.resize(self.__image.width(),\
                                self.__image.height())
        self.__zoneImage.move(self.__xZoneImage,self.__yZoneImage)
        # label widget for Pixmap
        if self.__save != None :
            self.__btnSave.resize(40,20)
            self.__btnSave.move(self.__width-45, self.__height-21)
 
    def ClearImage(self):
        self.__image = None
        self.__zoneImage.clear()
        if self.__comment != None:
            self.__comment.clear()
 
    def SaveImage(self):
        if self.__image != None: 
            fichier = QFileDialog.getSaveFileName(self,\
                      'Save a bitmap image (*.png *.bmp *.jpg *.jpeg)',\
                      "Images/untitled.png", 'Images (*.png *.bmp *.jpg *.jpeg)')
            self.__image.save(fichier)           
