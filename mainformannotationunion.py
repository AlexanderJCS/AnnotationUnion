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

        self.selected_annotation: Optional[ORSModel.Annotation, None] = None

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
    def on_btn_select_base_clicked(self):
        annotation = self.annotation_dialog()
        if annotation is None:
            self.ui.label_selected.setText("Not Selected")
            return

        self.selected_annotation = annotation
        self.ui.label_selected.setText(f"Selected: {annotation.getTitle()}")

    @pyqtSlot()
    def on_btn_start_clicked(self):
        if self.selected_annotation is None:
            self.ui.label_status.setText("No annotation selected")
            return

        self.selected_annotation: ORSModel.Annotation

        annotations = []

        while True:
            annotation = self.annotation_dialog()
            if annotation is None:
                break

            annotations.append(annotation)

        for annotation in annotations:
            count = annotation.getControlPointCount(0)

            for i in range(count):
                self.selected_annotation.addControlPoint(
                    annotation.getControlPointPositionAtIndex(i, 0, None),
                    0,
                    None
                )

                appended_ctrl_point_idx = self.selected_annotation.getControlPointCount(0) - 1
                self.selected_annotation.setControlPointCaptionAtIndex(
                    appended_ctrl_point_idx,
                    0,
                    annotation.getControlPointCaptionAtIndex(i, 0),
                )

        self.ui.label_status.setText(f"Unioned {len(annotations)} annotations")