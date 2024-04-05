# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\add_offer.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 362)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 0, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line_of_name = QtWidgets.QLineEdit(self.centralwidget)
        self.line_of_name.setGeometry(QtCore.QRect(150, 80, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.line_of_name.setFont(font)
        self.line_of_name.setText("")
        self.line_of_name.setObjectName("line_of_name")
        self.line_of_client = QtWidgets.QLineEdit(self.centralwidget)
        self.line_of_client.setGeometry(QtCore.QRect(150, 130, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.line_of_client.setFont(font)
        self.line_of_client.setText("")
        self.line_of_client.setObjectName("line_of_client")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.l_date = QtWidgets.QLabel(self.centralwidget)
        self.l_date.setGeometry(QtCore.QRect(500, 80, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.l_date.setFont(font)
        self.l_date.setObjectName("l_date")
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(20, 230, 81, 41))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.btn_confirm.setGeometry(QtCore.QRect(580, 230, 211, 41))
        self.btn_confirm.setObjectName("btn_confirm")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(500, 130, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.l_number = QtWidgets.QLineEdit(self.centralwidget)
        self.l_number.setGeometry(QtCore.QRect(590, 130, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.l_number.setFont(font)
        self.l_number.setText("")
        self.l_number.setObjectName("l_number")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(170, 191, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.l_exception = QtWidgets.QLabel(self.centralwidget)
        self.l_exception.setGeometry(QtCore.QRect(20, 280, 761, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.l_exception.setFont(font)
        self.l_exception.setText("")
        self.l_exception.setObjectName("l_exception")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 21))
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
        self.label.setText(_translate("MainWindow", "Создание нового заказа"))
        self.label_2.setText(_translate("MainWindow", "Название:"))
        self.label_4.setText(_translate("MainWindow", "ФИО Клиента:"))
        self.l_date.setText(_translate("MainWindow", "Дата:"))
        self.btn_cancel.setText(_translate("MainWindow", "Отмена"))
        self.btn_confirm.setText(_translate("MainWindow", "Создать заказ и добавить услуги"))
        self.label_7.setText(_translate("MainWindow", "Телефон:"))
        self.label_5.setText(_translate("MainWindow", "Тип автомобиля:"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Легковой"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Грузовой"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())