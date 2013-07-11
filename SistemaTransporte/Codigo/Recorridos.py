from PyQt4 import QtCore, QtGui
import sys
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Recorridos(QtGui.QMainWindow):
    def setupUi(self, Recorridos):
        Recorridos.setObjectName(_fromUtf8("Recorridos"))
        Recorridos.resize(640, 520)
        self.lHoraSalida = QtGui.QLabel(Recorridos)
        self.lHoraSalida.setGeometry(QtCore.QRect(160, 350, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lHoraSalida.setFont(font)
        self.lHoraSalida.setObjectName(_fromUtf8("lHoraSalida"))
        self.lIDConductor = QtGui.QLabel(Recorridos)
        self.lIDConductor.setGeometry(QtCore.QRect(90, 120, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lIDConductor.setFont(font)
        self.lIDConductor.setObjectName(_fromUtf8("lIDConductor"))
        self.lPasajeros = QtGui.QLabel(Recorridos)
        self.lPasajeros.setGeometry(QtCore.QRect(250, 200, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lPasajeros.setFont(font)
        self.lPasajeros.setObjectName(_fromUtf8("lPasajeros"))
        self.cbEstLlegada = QtGui.QComboBox(Recorridos)
        self.cbEstLlegada.setGeometry(QtCore.QRect(310, 290, 251, 27))
        self.cbEstLlegada.setObjectName(_fromUtf8("cbEstLlegada"))
        self.cbEstLlegada.addItem(_fromUtf8(""))
        self.cbEstLlegada.addItem(_fromUtf8(""))
        self.cbEstLlegada.addItem(_fromUtf8(""))
        self.cbEstLlegada.addItem(_fromUtf8(""))
        self.cbEstLlegada.addItem(_fromUtf8(""))
        self.cbEstLlegada.addItem(_fromUtf8(""))
        self.lFecha = QtGui.QLabel(Recorridos)
        self.lFecha.setGeometry(QtCore.QRect(50, 70, 66, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lFecha.setFont(font)
        self.lFecha.setObjectName(_fromUtf8("lFecha"))
        self.dateEdit = QtGui.QDateEdit(Recorridos)
        self.dateEdit.setGeometry(QtCore.QRect(130, 70, 121, 27))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.lEstSalida = QtGui.QLabel(Recorridos)
        self.lEstSalida.setGeometry(QtCore.QRect(130, 240, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lEstSalida.setFont(font)
        self.lEstSalida.setObjectName(_fromUtf8("lEstSalida"))
        self.timeEditHoraLLegada = QtGui.QTimeEdit(Recorridos)
        self.timeEditHoraLLegada.setGeometry(QtCore.QRect(370, 380, 161, 27))
        self.timeEditHoraLLegada.setObjectName(_fromUtf8("timeEditHoraLLegada"))
        self.lEstLlegada = QtGui.QLabel(Recorridos)
        self.lEstLlegada.setGeometry(QtCore.QRect(110, 290, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lEstLlegada.setFont(font)
        self.lEstLlegada.setObjectName(_fromUtf8("lEstLlegada"))
        self.titleRecorridos = QtGui.QLabel(Recorridos)
        self.titleRecorridos.setGeometry(QtCore.QRect(235, 40, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titleRecorridos.setFont(font)
        self.titleRecorridos.setObjectName(_fromUtf8("titleRecorridos"))
        self.cbEstSalida = QtGui.QComboBox(Recorridos)
        self.cbEstSalida.setGeometry(QtCore.QRect(310, 240, 251, 27))
        self.cbEstSalida.setObjectName(_fromUtf8("cbEstSalida"))
        self.cbEstSalida.addItem(_fromUtf8(""))
        self.cbEstSalida.addItem(_fromUtf8(""))
        self.cbEstSalida.addItem(_fromUtf8(""))
        self.cbEstSalida.addItem(_fromUtf8(""))
        self.cbEstSalida.addItem(_fromUtf8(""))
        self.cbEstSalida.addItem(_fromUtf8(""))
        self.lineEPasajeros = QtGui.QLineEdit(Recorridos)
        self.lineEPasajeros.setGeometry(QtCore.QRect(370, 200, 81, 27))
        self.lineEPasajeros.setObjectName(_fromUtf8("lineEPasajeros"))
        self.timeEditHoraSalida = QtGui.QTimeEdit(Recorridos)
        self.timeEditHoraSalida.setGeometry(QtCore.QRect(160, 380, 151, 27))
        self.timeEditHoraSalida.setObjectName(_fromUtf8("timeEditHoraSalida"))
        self.lineEIDConductor = QtGui.QLineEdit(Recorridos)
        self.lineEIDConductor.setGeometry(QtCore.QRect(250, 120, 301, 27))
        self.lineEIDConductor.setObjectName(_fromUtf8("lineEIDConductor"))
        self.lHoraLLegada = QtGui.QLabel(Recorridos)
        self.lHoraLLegada.setGeometry(QtCore.QRect(370, 350, 181, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lHoraLLegada.setFont(font)
        self.lHoraLLegada.setObjectName(_fromUtf8("lHoraLLegada"))
        self.lIDUnidad = QtGui.QLabel(Recorridos)
        self.lIDUnidad.setGeometry(QtCore.QRect(130, 160, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lIDUnidad.setFont(font)
        self.lIDUnidad.setObjectName(_fromUtf8("lIDUnidad"))
        self.lineEIDUnidad = QtGui.QLineEdit(Recorridos)
        self.lineEIDUnidad.setGeometry(QtCore.QRect(250, 160, 301, 27))
        self.lineEIDUnidad.setObjectName(_fromUtf8("lineEIDUnidad"))
        self.bRegresarRecorridos = QtGui.QPushButton(Recorridos)
        self.bRegresarRecorridos.setGeometry(QtCore.QRect(150, 450, 161, 31))
        self.bRegresarRecorridos.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Descargas/IMAGENES/Regresar.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bRegresarRecorridos.setIcon(icon)
        self.bRegresarRecorridos.setIconSize(QtCore.QSize(500, 1000))
        self.bRegresarRecorridos.setObjectName(_fromUtf8("bRegresarRecorridos"))
        self.bingresarRecorridos = QtGui.QPushButton(Recorridos)
        self.bingresarRecorridos.setGeometry(QtCore.QRect(370, 450, 161, 31))
        self.bingresarRecorridos.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../Descargas/IMAGENES/Ingresar.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bingresarRecorridos.setIcon(icon1)
        self.bingresarRecorridos.setIconSize(QtCore.QSize(600, 360))
        self.bingresarRecorridos.setObjectName(_fromUtf8("bingresarRecorridos"))

        self.retranslateUi(Recorridos)
        QtCore.QMetaObject.connectSlotsByName(Recorridos)

    def retranslateUi(self, Recorridos):
        Recorridos.setWindowTitle(_translate("Recorridos", "Form", None))
        self.lHoraSalida.setText(_translate("Recorridos", "HORA DE SALIDA", None))
        self.lIDConductor.setText(_translate("Recorridos", "ID CONDUCTOR", None))
        self.lPasajeros.setText(_translate("Recorridos", "PASAJEROS", None))
        self.cbEstLlegada.setItemText(0, _translate("Recorridos", "PISCINA OLIMPICA", None))
        self.cbEstLlegada.setItemText(1, _translate("Recorridos", "ESPOL", None))
        self.cbEstLlegada.setItemText(2, _translate("Recorridos", "ACACIAS", None))
        self.cbEstLlegada.setItemText(3, _translate("Recorridos", "TERMINAL", None))
        self.cbEstLlegada.setItemText(4, _translate("Recorridos", "ORQUIDEAS", None))
        self.cbEstLlegada.setItemText(5, _translate("Recorridos", "DURAN", None))
        self.lFecha.setText(_translate("Recorridos", "FECHA", None))
        self.lEstSalida.setText(_translate("Recorridos", "ESTACION SALIDA", None))
        self.lEstLlegada.setText(_translate("Recorridos", "ESTACION LLEGADA", None))
        self.titleRecorridos.setText(_translate("Recorridos", "RECORRIDOS", None))
        self.cbEstSalida.setItemText(0, _translate("Recorridos", "PISCINA OLIMPICA", None))
        self.cbEstSalida.setItemText(1, _translate("Recorridos", "ESPOL", None))
        self.cbEstSalida.setItemText(2, _translate("Recorridos", "ACACIAS", None))
        self.cbEstSalida.setItemText(3, _translate("Recorridos", "TERMINAL", None))
        self.cbEstSalida.setItemText(4, _translate("Recorridos", "ORQUIDEAS", None))
        self.cbEstSalida.setItemText(5, _translate("Recorridos", "DURAN", None))
        self.lHoraLLegada.setText(_translate("Recorridos", "HORA DE LLEGADA", None))
        self.lIDUnidad.setText(_translate("Recorridos", "ID UNIDAD", None))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Recorridos = QtGui.QWidget()
    ui = Ui_Recorridos()
    ui.setupUi(Recorridos)
    Recorridos.show()
    sys.exit(app.exec_())