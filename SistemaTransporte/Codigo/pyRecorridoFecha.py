'''
Created on 27/07/2013

@author: josanvel
'''
from PyQt4 import QtCore, QtGui, QtSql
from RecorridoFecha import Ui_RecorridoFecha

class MyformRecorridoFecha(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiRF = Ui_RecorridoFecha()
        self.uiRF.setupUi(self)
        self.center()
        self.setearBotones()
        
        
        self.connect(self.uiRF.bRegresarRFecha, QtCore.SIGNAL("clicked()"), self.regresarFecha)
        self.connect(self.uiRF.bConsultarRFecha, QtCore.SIGNAL("clicked()"), self.consultarFecha)

    def setearBotones(self):
        iconReg = QtGui.QIcon()
        iconIng = QtGui.QIcon()
        
        iconReg.addPixmap(QtGui.QPixmap(("imagenes/bregresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiRF.bRegresarRFecha.setIcon(iconReg)
        self.uiRF.bRegresarRFecha.setIconSize(QtCore.QSize(240, 50))
        
        iconIng.addPixmap(QtGui.QPixmap(("imagenes/bingresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiRF.bConsultarRFecha.setIcon(iconIng)
        self.uiRF.bConsultarRFecha.setIconSize(QtCore.QSize(240, 50))            
    
    def consultarFecha(self):        
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                print 'No se pudo abrir la BASES DE DATOS'
        else: 
                print 'Bases de Datos Abierta'
        
        model = QtSql.QSqlTableModel(self)
        print str(self.uiRF.dFechaInicial.DaySection)
        
        dia1 = self.uiRF.dFechaInicial.date().day()
        mes1 = self.uiRF.dFechaInicial.date().month()
        ano1 = self.uiRF.dFechaInicial.date().year()
        fechaInicial = str(ano1)+"/"+str(mes1)+"/"+str(dia1)
        
        dia2 = self.uiRF.dFechaFinal.date().day()
        mes2 = self.uiRF.dFechaFinal.date().month()
        ano2 = self.uiRF.dFechaFinal.date().year()
        fechaFinal = str(ano2)+"/"+str(mes2)+"/"+str(dia2)
        
        model.setQuery(QtSql.QSqlQuery("call PRQueryRecorridoFecha('"+fechaInicial+"','"+fechaFinal+"')"))
        model.select();
    
        self.uiRF.tableViewRF.setModel(model)
        self.uiRF.tableViewRF.resizeColumnsToContents()
        self.uiRF.tableViewRF.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
            
    def regresarVentanaF(self, ventana):
        self.principal = ventana
    
    def regresarFecha(self):
        self.hide()
        self.principal.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())