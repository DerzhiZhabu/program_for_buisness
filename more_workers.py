# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'more_workers.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(564, 666)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 210, 541, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(106)
        self.tableWidget.verticalHeader().setVisible(False)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.l_syear = QtWidgets.QLineEdit(self.centralwidget)
        self.l_syear.setGeometry(QtCore.QRect(50, 130, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l_syear.setFont(font)
        self.l_syear.setObjectName("l_syear")
        self.l_smonth = QtWidgets.QLineEdit(self.centralwidget)
        self.l_smonth.setGeometry(QtCore.QRect(110, 130, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l_smonth.setFont(font)
        self.l_smonth.setObjectName("l_smonth")
        self.l_sday = QtWidgets.QLineEdit(self.centralwidget)
        self.l_sday.setGeometry(QtCore.QRect(170, 130, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l_sday.setFont(font)
        self.l_sday.setObjectName("l_sday")
        self.l_pyear = QtWidgets.QLineEdit(self.centralwidget)
        self.l_pyear.setGeometry(QtCore.QRect(50, 170, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l_pyear.setFont(font)
        self.l_pyear.setObjectName("l_pyear")
        self.l_pmonth = QtWidgets.QLineEdit(self.centralwidget)
        self.l_pmonth.setGeometry(QtCore.QRect(110, 170, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l_pmonth.setFont(font)
        self.l_pmonth.setObjectName("l_pmonth")
        self.l_pday = QtWidgets.QLineEdit(self.centralwidget)
        self.l_pday.setGeometry(QtCore.QRect(170, 170, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l_pday.setFont(font)
        self.l_pday.setObjectName("l_pday")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.b_use = QtWidgets.QPushButton(self.centralwidget)
        self.b_use.setGeometry(QtCore.QRect(224, 172, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b_use.setFont(font)
        self.b_use.setObjectName("b_use")
        self.l_ito = QtWidgets.QLabel(self.centralwidget)
        self.l_ito.setGeometry(QtCore.QRect(10, 590, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.l_ito.setFont(font)
        self.l_ito.setObjectName("l_ito")
        self.btn_change = QtWidgets.QPushButton(self.centralwidget)
        self.btn_change.setGeometry(QtCore.QRect(460, 0, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_change.setFont(font)
        self.btn_change.setObjectName("btn_change")
        self.l_password = QtWidgets.QLineEdit(self.centralwidget)
        self.l_password.setGeometry(QtCore.QRect(340, 0, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l_password.setFont(font)
        self.l_password.setText("")
        self.l_password.setObjectName("l_password")
        self.s_procent = QtWidgets.QSpinBox(self.centralwidget)
        self.s_procent.setGeometry(QtCore.QRect(430, 90, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.s_procent.setFont(font)
        self.s_procent.setMaximum(100)
        self.s_procent.setObjectName("s_procent")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(430, 140, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_save.setFont(font)
        self.btn_save.setObjectName("btn_save")
        self.btn_fired = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fired.setGeometry(QtCore.QRect(430, 170, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_fired.setFont(font)
        self.btn_fired.setObjectName("btn_fired")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 564, 21))
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
        self.label.setText(_translate("MainWindow", "ФИО:"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Заказ"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Услуга"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Цена услуги"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Зарплата"))
        self.label_3.setText(_translate("MainWindow", "Оказанные услуги:"))
        self.label_4.setText(_translate("MainWindow", "C"))
        self.l_syear.setText(_translate("MainWindow", "2023"))
        self.l_smonth.setText(_translate("MainWindow", "06"))
        self.l_sday.setText(_translate("MainWindow", "03"))
        self.l_pyear.setText(_translate("MainWindow", "2023"))
        self.l_pmonth.setText(_translate("MainWindow", "06"))
        self.l_pday.setText(_translate("MainWindow", "03"))
        self.label_5.setText(_translate("MainWindow", "ПО"))
        self.b_use.setText(_translate("MainWindow", "Применить"))
        self.l_ito.setText(_translate("MainWindow", "Зарплата за указанный периоод: "))
        self.btn_change.setText(_translate("MainWindow", "Изменить"))
        self.btn_save.setText(_translate("MainWindow", "Сохранить"))
        self.btn_fired.setText(_translate("MainWindow", "Уволить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
