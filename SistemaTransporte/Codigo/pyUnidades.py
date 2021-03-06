'''
Created on 27/07/2013

@author: josanvel
'''
from PyQt4 import QtCore, QtGui, QtSql
from Unidades import Ui_Unidades
import exceptions

class MyformUnidades(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiU = Ui_Unidades()
        self.uiU.setupUi(self)
        self.center()
        self.setearBotones()
        
        self.connect(self.uiU.bRegresarUnidades, QtCore.SIGNAL("clicked()"), self.regresarUnidades)
        self.connect(self.uiU.bingresarUnidades, QtCore.SIGNAL("clicked()"), self.ingresarUnidades)
        
    def setearBotones(self):
        iconReg = QtGui.QIcon()
        iconIng = QtGui.QIcon()
        
        iconReg.addPixmap(QtGui.QPixmap(("imagenes/bregresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiU.bRegresarUnidades.setIcon(iconReg)
        self.uiU.bRegresarUnidades.setIconSize(QtCore.QSize(240, 50))
        
        iconIng.addPixmap(QtGui.QPixmap(("imagenes/bingresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiU.bingresarUnidades.setIcon(iconIng)
        self.uiU.bingresarUnidades.setIconSize(QtCore.QSize(240, 50))
        
    def regresarVentanaU(self, ventanaAtras):
        self.ventanaPrincipal = ventanaAtras
        
    def regresarUnidades(self):
        self.hide()
        self.ventanaPrincipal.show()
    
    def ingresarUnidades(self):
        matricula = self.uiU.lineEMatricula.displayText()
        capacidad = self.uiU.lineECapacidad.displayText()
        anoF  = self.uiU.lineEAnoFab.displayText()
        
        if matricula != '' and capacidad != '' and anoF != '':    
            if self.valMatricula(matricula) == False:
                QtGui.QMessageBox.information(None, 'Ingreso erroneo','Numero de matricula incorrecto')
                self.uiU.lineEMatricula.setText("")
                
            elif self.toInt(capacidad) == None:  
                QtGui.QMessageBox.information(None, 'Ingreso erroneo','El campo capacidad solo admite enteros')
                self.uiU.lineECapacidad.setText("")
                
            elif self.toInt(anoF) == None:
                QtGui.QMessageBox.information(None, 'Ingreso erroneo','El campo anio fabricacion solo admite enteros')
                self.uiU.lineEAnoFab.setText("")
            elif self.toInt(capacidad)>50:
                QtGui.QMessageBox.information(None, 'Ingreso erroneo', 'Valor de capacidad incorrecto')
            else:
                self.IngresarOperacion()
                self.hide()
                self.ventanaPrincipal.show()
                
        else:
            QtGui.QMessageBox.information(None, 'Campos vacios', 'Todos los campos deben contener informacion')

    def IngresarOperacion(self):
        matricula = self.uiU.lineEMatricula.displayText()
        capacidad = self.toInt(self.uiU.lineECapacidad.displayText())
        anoFab = self.uiU.lineEAnoFab.displayText()
        fechaAd = QtCore.QDate.currentDate()
  
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                QtGui.QMessageBox.information(None,'ERROR', 'No se pudo abrir la BASES DE DATOS')
        
        query = QtSql.QSqlQuery()
        query.prepare("call PRInsertUnidad(?,?,?,?)")

        query.addBindValue(matricula)
        query.addBindValue(capacidad)
        query.addBindValue(anoFab)
        query.addBindValue(fechaAd)
                
        if not query.exec_():
            QtGui.QMessageBox.warning( None, "Error al crear una Unidad",\
                                          "No se pudo INSERTAR una Unidad" ) 
        else:
            QtGui.QMessageBox.information(None, "INFORMACION","Ah ingresado una  nueva Unidad")  
    
    def toInt(self,num):
        try:
            return int(num)
        except exceptions.ValueError:
            return None
    
    def valMatricula(self,mat):
        if len(mat)==7 or len(mat)==8:
            if mat[3]=='-':
                a = mat.split('-')
                letras = a[0]
                digitos = a[1]
                if self.toInt(digitos) and self.toInt(letras)==None:
                    return True
            else:
                return False
        else:
            return False

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
            
        