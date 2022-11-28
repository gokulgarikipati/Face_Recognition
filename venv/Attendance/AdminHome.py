

from PyQt5 import QtCore, QtGui, QtWidgets
from AddStudent import Ui_AddStudent
import webbrowser
from ViewStudents import  Ui_ViewStudents
class Ui_AdminHome(object):
    def __init__(self,Dialog):
        self.dialog=Dialog

    def addstdnts(self, event):
        try:
            self.adstdnt = QtWidgets.QDialog()
            self.ui1 = Ui_AddStudent()
            self.ui1.setupUi(self.adstdnt)
            self.adstdnt.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()
    def viewstdents(self,event):
        try:
            self.viewstdnt = QtWidgets.QDialog()
            self.ui1 = Ui_ViewStudents()
            self.ui1.setupUi(self.viewstdnt)
            self.ui1.studentdetails()
            self.viewstdnt.show()

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()
    def reports(self,event):
        webbrowser.open('http://localhost:2016/Attendance/', new=2)
        event.accept()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(673, 560)
        Dialog.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.addstdnt = QtWidgets.QLabel(Dialog)
        self.addstdnt.setGeometry(QtCore.QRect(10, 20, 201, 161))
        self.addstdnt.setStyleSheet("image: url(../Attendance/images/add.png);")
        self.addstdnt.setText("")
        self.addstdnt.setObjectName("addstdnt")
        self.addstdnt.mousePressEvent = self.addstdnts
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(410, 30, 181, 141))
        self.label_2.setStyleSheet("image: url(../Attendance/images/add1.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.mousePressEvent=self.viewstdents
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 180, 181, 31))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Vani\";")
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(450, 180, 181, 31))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Vani\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(270, 280, 171, 161))
        self.label_4.setStyleSheet("image: url(../Attendance/images/report.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_4.mousePressEvent=self.reports
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(300, 450, 181, 31))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Vani\";")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Admin Home"))
        self.label.setText(_translate("Dialog", "Add People"))
        self.label_3.setText(_translate("Dialog", "View People"))
        self.label_5.setText(_translate("Dialog", "Reports"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

