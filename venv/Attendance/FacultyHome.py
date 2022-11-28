
from PyQt5 import QtCore, QtGui, QtWidgets
from DBConnection import DBConnection
from Attendance import Ui_Attendance
import sys
import webbrowser
class Ui_FacultyHome(object):

    def __init__(self,Dialog,unm="gokul"):
        self.dialog=Dialog
        self.un=unm

    def takeattendance(self,event):
        try:
            self.atndnc = QtWidgets.QDialog()
            self.ui1 = Ui_Attendance(self.atndnc, self.un)
            self.ui1.setupUi(self.atndnc)
            self.atndnc.show()
            event.accept()

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def viewreports(self,event):
            webbrowser.open('http://localhost:2019/Attendance/', new=2)
            event.accept()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(673, 439)
        Dialog.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.addstdnt = QtWidgets.QLabel(Dialog)
        self.addstdnt.setGeometry(QtCore.QRect(20, 50, 341, 291))
        self.addstdnt.setStyleSheet("image: url(../Attendance/images/attendance.png);")
        self.addstdnt.setText("")
        self.addstdnt.setObjectName("addstdnt")
        self.addstdnt.mousePressEvent=self.takeattendance
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 260, 181, 31))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Vani\";")
        self.label.setObjectName("label")
        # self.label_4 = QtWidgets.QLabel(Dialog)
        # self.label_4.setGeometry(QtCore.QRect(410, 110, 201, 141))
        # self.label_4.setStyleSheet("image: url(../Attendance/images/report.png);")
        # self.label_4.setText("")
        # self.label_4.setObjectName("label_4")
        # self.label_4.mousePressEvent = self.viewreports
#         self.label_5 = QtWidgets.QLabel(Dialog)
#         self.label_5.setGeometry(QtCore.QRect(460, 260, 181, 31))
#         self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
# "font: 75 14pt \"Vani\";")
#         self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Faculty Home"))
        self.label.setText(_translate("Dialog", "Capture Image"))
        # self.label_5.setText(_translate("Dialog", "Reports"))


'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())'''

