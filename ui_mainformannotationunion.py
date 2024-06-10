# Form implementation generated from reading ui file '.\mainformannotationunion.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainFormAnnotationUnion(object):
    def setupUi(self, MainFormAnnotationUnion):
        MainFormAnnotationUnion.setObjectName("MainFormAnnotationUnion")
        MainFormAnnotationUnion.resize(360, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainFormAnnotationUnion.sizePolicy().hasHeightForWidth())
        MainFormAnnotationUnion.setSizePolicy(sizePolicy)
        MainFormAnnotationUnion.setMinimumSize(QtCore.QSize(360, 250))
        self.verticalLayout = QtWidgets.QVBoxLayout(MainFormAnnotationUnion)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(MainFormAnnotationUnion)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(MainFormAnnotationUnion)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label_selected = QtWidgets.QLabel(MainFormAnnotationUnion)
        self.label_selected.setObjectName("label_selected")
        self.horizontalLayout.addWidget(self.label_selected)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.btn_start = QtWidgets.QPushButton(MainFormAnnotationUnion)
        self.btn_start.setObjectName("btn_start")
        self.verticalLayout.addWidget(self.btn_start)
        self.label_status = QtWidgets.QLabel(MainFormAnnotationUnion)
        self.label_status.setText("")
        self.label_status.setObjectName("label_status")
        self.verticalLayout.addWidget(self.label_status)

        self.retranslateUi(MainFormAnnotationUnion)
        QtCore.QMetaObject.connectSlotsByName(MainFormAnnotationUnion)

    def retranslateUi(self, MainFormAnnotationUnion):
        _translate = QtCore.QCoreApplication.translate
        MainFormAnnotationUnion.setWindowTitle(_translate("MainFormAnnotationUnion", "Form"))
        self.textBrowser.setHtml(_translate("MainFormAnnotationUnion", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Instructions:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. Click &quot;Select annotation&quot; to select an annotation to modify.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. Click &quot;Start Annotation Union&quot; to select objects to union.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. Select an annotation, then click &quot;OK&quot; to union.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4. Repeat step 3 for all annotations to union.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5. When all objects are unioned, click &quot;Cancel.&quot;</p></body></html>"))
        self.pushButton.setText(_translate("MainFormAnnotationUnion", "Select Annotation"))
        self.label_selected.setText(_translate("MainFormAnnotationUnion", "Not Selected"))
        self.btn_start.setText(_translate("MainFormAnnotationUnion", "Start Annotation Union"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainFormAnnotationUnion = QtWidgets.QWidget()
    ui = Ui_MainFormAnnotationUnion()
    ui.setupUi(MainFormAnnotationUnion)
    MainFormAnnotationUnion.show()
    sys.exit(app.exec())