# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stat_change.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 235)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 0, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.co_worker = QtWidgets.QComboBox(self.centralwidget)
        self.co_worker.setGeometry(QtCore.QRect(130, 40, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.co_worker.setFont(font)
        self.co_worker.setObjectName("co_worker")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btn_com = QtWidgets.QPushButton(self.centralwidget)
        self.btn_com.setGeometry(QtCore.QRect(440, 160, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_com.setFont(font)
        self.btn_com.setObjectName("btn_com")
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(0, 160, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_close.setFont(font)
        self.btn_close.setObjectName("btn_close")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(10, 90, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.l_password = QtWidgets.QLineEdit(self.centralwidget)
        self.l_password.setGeometry(QtCore.QRect(100, 90, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l_password.setFont(font)
        self.l_password.setObjectName("l_password")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 595, 21))
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
        self.label.setText(_translate("MainWindow", "Изменение статуса услуги"))
        self.label_3.setText(_translate("MainWindow", "Сотрудник:"))
        self.btn_com.setText(_translate("MainWindow", "Услуга готова"))
        self.btn_close.setText(_translate("MainWindow", "Отмена"))
        self.label_password.setText(_translate("MainWindow", "Пароль:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())