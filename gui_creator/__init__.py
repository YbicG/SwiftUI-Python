from .types.app_types import AppType
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

class App:

    rootViewController = None
    application = None

    def __init__(self, app_type: AppType):
        self.__QAPP__ = QApplication(sys.argv)

        self.app_type = app_type

        if app_type != AppType.TYPE_PYQT6 and app_type != AppType.TYPE_TKINTER:
            raise TypeError("Invalid app type \"" + app_type + "\" Valid app types are \"" + AppType.TYPE_PYQT6 + "\" and \"" + AppType.TYPE_TKINTER + "\"")
        pass


    def launch(self):
        if self.rootViewController == None:
            raise TypeError("RootViewController is not defined")
        else:
            if self.app_type == AppType.TYPE_PYQT6:            
                self.rootViewController.pushView(self.app_type)
                self.__QAPP__.exec()
                self.application = self.__QAPP__

            elif self.app_type == AppType.TYPE_TKINTER:
                self.rootViewController.pushView(self.app_type)