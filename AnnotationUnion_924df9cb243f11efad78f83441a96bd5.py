"""


:author: Alexander Castronovo
:contact: 
:email: alexander.castronovo@mpfi.org
:organization: 
:address: 
:copyright: 
:date: Jun 06 2024 16:01
:dragonflyVersion: 2024.1.0.1601
:UUID: 924df9cb243f11efad78f83441a96bd5
"""

__version__ = '1.0.0'

from ORSServiceClass.OrsPlugin.orsPlugin import OrsPlugin
from ORSServiceClass.decorators.infrastructure import menuItem
from ORSServiceClass.actionAndMenu.menu import Menu
from ORSServiceClass.OrsPlugin.uidescriptor import UIDescriptor


class AnnotationUnion_924df9cb243f11efad78f83441a96bd5(OrsPlugin):

    # Plugin definition
    multiple = True
    savable = False
    keepAlive = False
    canBeGenericallyOpened = False

    # UIs
    UIDescriptors = [UIDescriptor(name='MainFormAnnotationUnion',
                                  title='Annotation Union',
                                  dock='Left',
                                  tab='Main',
                                  modal=False,
                                  collapsible=True,
                                  floatable=True)]

    def __init__(self, varname=None):
        super().__init__(varname)

    @classmethod
    def getMainFormName(cls):
        return 'MainFormAnnotationUnion'

    @classmethod
    def getMainFormClass(cls):
        from .mainformannotationunion import MainFormAnnotationUnion
        return MainFormAnnotationUnion

    @classmethod
    def openGUI(cls):
        instance = AnnotationUnion_924df9cb243f11efad78f83441a96bd5()

        if instance is not None:
            instance.openWidget("MainFormAnnotationUnion")

    @classmethod
    @menuItem("Annotation Union")
    def AnnotationUnion(cls):
        menu_item = Menu(title="Start Annotation Union",
                         id_="AnnotationUnion_924df9cb243f11efad78f83441a96bd5_1",
                         section="",
                         action="AnnotationUnion_924df9cb243f11efad78f83441a96bd5.openGUI()")

        return menu_item

