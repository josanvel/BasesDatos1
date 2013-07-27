'''
Created on 27/07/2013

@author: josanvel
'''
from PyQt4 import QtCore, QtGui
from RecorridoUnidad import Ui_RecorridoUnidad
import exceptions

class MyformRecorridoUnidad(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiRU = Ui_RecorridoUnidad()
        self.uiRU.setupUi(self)

        self.connect(self.uiRU.bRegresarRUnidad, QtCore.SIGNAL("clicked()"), self.regresarUnidad)
        self.connect(self.uiRU.bConsultarRUnidad, QtCore.SIGNAL("clicked()"), self.consultarUnidad)
        
    def regresarVentanaU(self, ventana):
        self.principal = ventana
    
    def regresarUnidad(self):
        self.hide()
        self.principal.show()
    
    def consultarUnidad(self):
        self.idUnidad = self.uiRU.lineIDUnidad.displayText()
        if(self.idUnidad !=''):
            if self.toInt(self.idUnidad) == None:
                QtGui.QMessageBox.information(self, 'Ingreso erroneo','Solo se admite enteros en el campo de ID Unidad')
            '''else: ingreso a la base '''
        else:
            QtGui.QMessageBox.information(self, 'Campos vacios', 'Todos los campos deben contener informacion')
    
        
    def toInt(self,num):
        try:
            return int(num)
        except exceptions.ValueError:
            return None
        
            