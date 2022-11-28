from PyQt5 import QtCore, QtGui, QtWidgets
from Camera1 import CaptureImage
from DBConnection import DBConnection
from predict import face_recognition,predict,show_prediction_labels_on_image,train
import sys
import os
import datetime
class Ui_Attendance(object):
    unmlist=[]
    def __init__(self,Dialog,unm):
        self.dialog=Dialog
        self.un=unm
    def getCameraImage(self,event):
        try:
            CaptureImage()
            self.showMessageBox("Information", "Picture Captured..!")
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()

    def submit(self):
        try:
            namelist=[]
            namelist.clear()

            print("Training KNN classifier...")
            classifier = train("../Attendance/photos", model_save_path="trained_knn_model.clf", n_neighbors=1)
            print("Training complete!")

            # STEP 2: Using the trained classifier, make predictions for unknown images
            for image_file in os.listdir("../Attendance/test"):
                full_file_path = os.path.join("../Attendance/test", image_file)

                print("Looking for faces in {}".format(image_file))

                # Find all people in the image using a trained classifier model
                # Note: You can pass in either a classifier file name or a classifier model instance
                predictions = predict(full_file_path, model_path="trained_knn_model.clf")

                # Print results on the console
                for name, (top, right, bottom, left) in predictions:
                    namelist.append(name)
                    print("- Found {} at ({}, {})".format(name, left, top))

                # Display results overlaid on an image
                show_prediction_labels_on_image(os.path.join("../Attendance/test", image_file), predictions)

            print(namelist)
            #self.setNames(namelist)
            database = DBConnection.getConnection()
            cursor=database.cursor()
            for nm in namelist:
                sql="insert into temp values('"+str(nm)+"')"
                cursor.execute(sql)
                database.commit()
            self.showMessageBox("Information", "Submited picture..!")

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def closed(self):
        try:
            unmlist=[]
            unmlist.clear()
            database = DBConnection.getConnection()
            cursor = database.cursor()

            cursor.execute("select stdntnm from temp")
            rows = cursor.fetchall()
            for r in rows:
                unmlist.append(r[0])


            cursor.execute("select name,rollno from students")
            row = cursor.fetchall()
            for r in row:
                nm = r[0]
                if nm in unmlist:

                    sql="insert into attendance values(%s,%s,%s,%s)"
                    values=(r[1],nm,str(datetime.datetime.now().date()),"P")
                    cursor.execute(sql,values)
                    database.commit()
                    #print("p"+str(r[0]))
                else:
                    sql = "insert into attendance values(%s,%s,%s,%s)"
                    values = (r[1],nm,str(datetime.datetime.now().date()), "A")
                    cursor.execute(sql, values)
                    database.commit()
                    #print("A"+str(r[0]))
            cursor.execute("delete from temp")
            database.commit()
            self.showMessageBox("Information", "Attendance closed..!")
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)


    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setNames(self,nmlist):
        self.unmlist=nmlist

    def getNames(self):
        self.unmlist

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(609, 503)
        Dialog.setStyleSheet("background-color: rgb(200, 129, 152);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(240, 50, 201, 31))
        self.label.setStyleSheet("font: 75 16pt \"Vani\";")
        self.label.setObjectName("label")
        self.camera = QtWidgets.QLabel(Dialog)
        self.camera.setGeometry(QtCore.QRect(210, 120, 161, 121))
        self.camera.setStyleSheet("image: url(../Attendance/images/camera.png);")
        self.camera.setText("")
        self.camera.setObjectName("camera")
        self.camera.mousePressEvent=self.getCameraImage
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(230, 250, 181, 41))
        self.label_5.setStyleSheet("font: 75 12pt \"Vani\";")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 350, 121, 41))
        self.pushButton.setStyleSheet("font: 75 12pt \"Vani\";\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.submit)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 350, 121, 41))
        self.pushButton_2.setStyleSheet("font: 75 14pt \"Vani\";\n"
"background-color: rgb(138, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.closed)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Capture Image"))
        self.label.setText(_translate("Dialog", "Capture Image"))
        self.label_5.setText(_translate("Dialog", "Click on Camera"))
        self.pushButton.setText(_translate("Dialog", "Submit"))
        self.pushButton_2.setText(_translate("Dialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Attendance()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

