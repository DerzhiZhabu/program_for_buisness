# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\first_start.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(849, 289)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_sur = QtWidgets.QLineEdit(self.centralwidget)
        self.line_sur.setGeometry(QtCore.QRect(10, 100, 821, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.line_sur.setFont(font)
        self.line_sur.setText("")
        self.line_sur.setObjectName("line_sur")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 831, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.bt_add = QtWidgets.QPushButton(self.centralwidget)
        self.bt_add.setGeometry(QtCore.QRect(10, 150, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bt_add.setFont(font)
        self.bt_add.setObjectName("bt_add")
        self.bt_close = QtWidgets.QPushButton(self.centralwidget)
        self.bt_close.setGeometry(QtCore.QRect(740, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bt_close.setFont(font)
        self.bt_close.setObjectName("bt_close")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 831, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.l_ex = QtWidgets.QLabel(self.centralwidget)
        self.l_ex.setGeometry(QtCore.QRect(10, 190, 831, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.l_ex.setFont(font)
        self.l_ex.setText("")
        self.l_ex.setObjectName("l_ex")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 849, 21))
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
        self.label.setText(_translate("MainWindow", "Задайте пароль администратора(запомните его, позже его нельзя будет изменить)"))
        self.bt_add.setText(_translate("MainWindow", "Готово"))
        self.bt_close.setText(_translate("MainWindow", "Отмена"))
        self.label_2.setText(_translate("MainWindow", "Пароль должен состоять из цифр(без букв и знаков)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())