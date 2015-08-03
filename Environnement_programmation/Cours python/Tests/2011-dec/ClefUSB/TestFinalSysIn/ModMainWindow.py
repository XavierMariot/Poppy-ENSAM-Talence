# -*- coding: latin-1 -*-from PyQt4.QtGui import QMainWindow, QPushButton, QImage, QLabelfrom PyQt4.QtGui import QFileDialog, QDialog, QAction, QDoubleSpinBoxfrom PyQt4.QtGui import QGridLayout, QSliderfrom PyQt4.QtCore import SIGNAL, SLOTfrom math import fsumfrom ModFrameImage import FrameImagefrom ModImageArray import ImageArrayclass MainWindow(QMainWindow):    "This is the main window that implements the graphical user interface"    def __init__(self):    # constructor        QMainWindow.__init__(self)        frame1W, frame1H = 220,220        frame2W, frame2H = 220,280        frame3W, frame3H = 350,280        spaceH, spaceV = 20,40        self.resize(frame1W+frame2W+frame3W+4*spaceH,\                    max(frame1H,frame2H,frame3H)+2*spaceV)        self.__cadre1 = FrameImage(self,spaceH,spaceV,\                                  frame1W,frame1H)        self.__cadre2 = FrameImage(self,2*spaceH+frame1W,spaceV,\                                  frame2W,frame2H,True)        self.__cadre3 = FrameImage(self,3*spaceH+frame1W+frame2W,spaceV,\                                  frame3W,frame3H,True)        # empty object ImageArray        self.__ARGBarray = ImageArray()                 # Quit,Open, Process menu        Quit = QAction('Quitter...', self)           self.connect(Quit, SIGNAL('triggered()'), SLOT('close()'))          Open = QAction('Ouvrir...', self)          self.connect(Open, SIGNAL('triggered()'), self.OpenImageFile)        Process = QAction('Transformer...', self)          self.connect(Process, SIGNAL('triggered()'), self.OpenImageFile)                # Menu bar, with sub-menus        menubar = self.menuBar()          menuF = menubar.addMenu('Fichier')          menuF.addAction(Open)          menuF.addAction(Quit)    ###################################################################  DEBUT DE LA ZONE A COMPLETER ############    #######################################################        menuT = menubar.addMenu('Transformer')        menuT.addAction('Reinit',     self.__ReinitImage2)        menuT.addAction('Negatif',    self.__Negative)        menuT.addAction('Monochrome', self.__UniColor)        # ici les menus GradientH, GradientV et Contour...                menuA = menubar.addMenu('Analyser')        # ici le menu 'Histogramme'...     def __Negative(self):        self.__TraiterImage(self.__ARGBarray.Negative)    # TODO :  d�finition de la m�thode __HGradient    # TODO :  d�finition de la m�thode __VGradient    # TODO :  d�finition de la m�thode __Edge    # TODO :  d�finition de la m�thode __Histogram    #################################################################  FIN DE LA ZONE A COMPLETER ############    #####################################################    def __UniColor(self):        rgbChoice = RGBValueDialog(self)        rgbChoice.exec_()        r, g, b = rgbChoice.getRGB()        self.__TraiterImage(self.__ARGBarray.UniColor, r, g, b)            def OpenImageFile(self):        fichier = QFileDialog.getOpenFileName(self,'opens a file')        self.__image = QImage(fichier)        self.__cadre1.DisplayImage(self.__image)        self.__cadre2.ClearImage()        self.__cadre3.ClearImage()        self.__ARGBarray.LoadImage(self.__image)    def __ReinitImage2(self):        if self.__cadre1.ImageQ():            self.__cadre2.ClearImage()            self.__cadre3.ClearImage()            self.__cadre2.DisplayImage(self.__image)            self.__cadre2.DisplayComment('')            self.__ARGBarray.LoadImage(self.__image)    def __TraiterImage(self,traitement,*args):        if self.__cadre1.ImageQ():            self.__cadre2.DisplayComment("Traitement en cours")            traitement(*args)            newimage = self.__ARGBarray.ConvertToQImage()            self.__cadre2.DisplayComment("Traitement fini")            self.__cadre2.DisplayImage(newimage)            self.__cadre3.ClearImage()       class RGBValueDialog(QDialog):    def __init__(self,parent, r=1./3, g=1./3, b=1./3, alpha=False):        QDialog.__init__(self,parent)           self.__rgba = [r, g, b, alpha]        self.__a = None               self.__r = QDoubleSpinBox()        self.__r.setSingleStep(0.05)        self.__r.setRange(0,1)        self.__r.setValue(self.__rgba[0])        self.__rlabel = QLabel("Red")        self.__g = QDoubleSpinBox()        self.__g.setSingleStep(0.05)        self.__g.setRange(0,1)        self.__g.setValue(self.__rgba[1])        self.__glabel = QLabel("Green")        self.__b = QDoubleSpinBox()        self.__b.setSingleStep(0.05)        self.__b.setRange(0,1)        self.__b.setValue(self.__rgba[2])        self.__blabel = QLabel("Blue ")        if alpha != False :            self.__a = QDoubleSpinBox()            self.__a.setSingleStep(0.05)            self.__a.setRange(0,1)            self.__a.setValue(self.__rgba[3])            self.__alabel = QLabel("Alpha ")                       self.__btnOK = QPushButton('OK',self)         # layout        layout = QGridLayout()        layout.addWidget(self.__r, 0, 1)        layout.addWidget(self.__rlabel, 0, 0)        layout.addWidget(self.__g, 1, 1)        layout.addWidget(self.__glabel, 1, 0)        layout.addWidget(self.__b, 2, 1)        layout.addWidget(self.__blabel,2, 0)        if alpha != False:            layout.addWidget(self.__a,3, 0)            layout.addWidget(self.__alabel,3,1)            layout.addWidget(self.__btnOK,4,1)        else:            layout.addWidget(self.__btnOK,3,1)                    self.setLayout(layout)        self.__r.setFocus()        self.setWindowTitle("RGB values")         # Connections        self.connect(self.__btnOK, SIGNAL('clicked()'), self.__update)    def getRGB(self) : return self.__rgba[:3]    def getARGB(self) : return (self.__rgba[3],self.__rgba[0],self.__rgba[1],self.__rgba[2])    def __update(self):        # get values        a = 1        if self.__a != None:            a = self.__a.value()        self.__rgba = (self.__r.value(),self.__g.value(),self.__b.value(),a)        self.done(0)