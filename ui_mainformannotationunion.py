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
        MainFormAnnotationUnion.resize(150, 100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainFormAnnotationUnion.sizePolicy().hasHeightForWidth())
        MainFormAnnotationUnion.setSizePolicy(sizePolicy)
        MainFormAnnotationUnion.setMinimumSize(QtCore.QSize(150, 100))
        self.verticalLayout = QtWidgets.QVBoxLayout(MainFormAnnotationUnion)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_start = QtWidgets.QPushButton(MainFormAnnotationUnion)
        self.btn_start.setObjectName("btn_start")
        self.verticalLayout.addWidget(self.btn_start)

        self.retranslateUi(MainFormAnnotationUnion)
        QtCore.QMetaObject.connectSlotsByName(MainFormAnnotationUnion)

    def retranslateUi(self, MainFormAnnotationUnion):
        _translate = QtCore.QCoreApplication.translate
        MainFormAnnotationUnion.setWindowTitle(_translate("MainFormAnnotationUnion", "Form"))
        self.btn_start.setText(_translate("MainFormAnnotationUnion", "Start Annotation Union"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainFormAnnotationUnion = QtWidgets.QWidget()
    ui = Ui_MainFormAnnotationUnion()
    ui.setupUi(MainFormAnnotationUnion)
    MainFormAnnotationUnion.show()
    sys.exit(app.exec())
