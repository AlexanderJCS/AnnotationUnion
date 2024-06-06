import ORSModel
from ORSModel import orsObj, ROI
from ORSServiceClass.ORSWidget.chooseObjectAndNewName.chooseObjectAndNewName import ChooseObjectAndNewName
from PyQt6.QtCore import pyqtSlot, Qt
from PyQt6 import QtGui

from OrsLibraries.workingcontext import WorkingContext
from ORSServiceClass.windowclasses.orsabstractwindow import OrsAbstractWindow
from PyQt6.QtWidgets import QDialog

from OrsLibraries.workingcontext import WorkingContext
from ORSServiceClass.windowclasses.orsabstractwindow import OrsAbstractWindow
from .ui_mainformannotationunion import Ui_MainFormAnnotationUnion

from typing import Optional


class MainFormAnnotationUnion(OrsAbstractWindow):

    def __init__(self, implementation, parent=None):
        super().__init__(implementation, parent)
        self.ui = Ui_MainFormAnnotationUnion()
        self.ui.setupUi(self)
        WorkingContext.registerOrsWidget('AnnotationUnion_924df9cb243f11efad78f83441a96bd5', implementation, 'MainFormAnnotationUnion', self)

    @staticmethod
    def annotation_dialog() -> Optional[ORSModel.Annotation]:
        chooser = ChooseObjectAndNewName(
            managedClass=[ORSModel.Annotation],
            parent=WorkingContext.getCurrentContextWindow(),
        )

        chooser.setWindowTitle("Select an annotation or X to stop")
        chooser.setWindowFlags(
            Qt.WindowType.Window | Qt.WindowType.WindowTitleHint | Qt.WindowType.WindowCloseButtonHint
        )

        if chooser.exec() == QDialog.DialogCode.Rejected:
            return None

        guid = chooser.getObjectGUID()
        roi = orsObj(guid)

        return roi

    @pyqtSlot()
    def on_btn_start_clicked(self):
        annotations = []

        while True:
            roi = self.annotation_dialog()
            if roi is None:
                break
            annotations.append(roi)

        if len(annotations) == 0:
            return

        start_annotation = annotations[0]

        for annotation in annotations[1:]:
            count = annotation.getControlPointCount(0)

            for i in range(count):
                start_annotation.addControlPoint(
                    annotation.getControlPointPositionAtIndex(i, 0, None),
                    0,
                    None
                )
