from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QSpacerItem, QSizePolicy, QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QMainWindow, QApplication
from .elements import *
from .types.app_types import SpacerFlag
import requests


# Protocols
class InitProtocol:
    def __init__(self, title: str = "Gui Creator", width: int = 800, height: int = 600, backgroundColor: str = "#000000", logo: str = "https://darknode.dev/logo.png", resizable: bool = True, hideTitleBar: bool = False):
        self.title = title
        self.width = width
        self.height = height
        self.backgroundColor = backgroundColor
        self.logo = logo
        self.hideTitleBar = hideTitleBar
        self.resizable = resizable

    empty = {}

# Subclass QMainWindow to customize your application's main window
class View(QMainWindow):

    def __init__(self, initProtocol: InitProtocol = InitProtocol.empty, title = "Gui Creator", width = 800, height = 600, backgroundColor = "#000000", logo = "https://darknode.dev/logo.png", resizable = True, hideTitleBar = False):
        """
        You can use the InitProtocol class to initialize the view or you can use the parameters.

        How to use InitProtocol:
        ```InitProtocol(title: str, width: int, height: int, backgroundColor: str, logo: str, hideTitleBar: bool, resizable: bool)```

        How to use parameters:
        ```View(title: str, width: int, height: int, backgroundColor: str, logo: str, hideTitleBar: bool, resizable: bool)```
        """
        super().__init__()

        if initProtocol != InitProtocol.empty:

            self.setWindowTitle(initProtocol.title)

            self.setStyleSheet("background-color: " + initProtocol.backgroundColor + ";")

            if initProtocol.hideTitleBar:
                self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

            if not initProtocol.resizable:
                self.setFixedSize(QSize(initProtocol.width, initProtocol.height))
            else:
                self.resize(initProtocol.width, initProtocol.height)

            if "http" in initProtocol.logo or "https" in initProtocol.logo:
                url = initProtocol.logo
                data = requests.get(url).content
                pixmap = QPixmap()
                pixmap.loadFromData(data)
                self.setWindowIcon(QIcon(pixmap))
            else:
                self.setWindowIcon(QIcon(initProtocol.logo))

        else:

            self.setWindowTitle(title)

            self.setStyleSheet("background-color: " + backgroundColor + ";")

            if hideTitleBar:
                self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

            if not resizable:
                self.setFixedSize(QSize(width, height))
            else:
                self.resize(width, height)

            if "http" in logo or "https" in logo:
                url = logo
                data = requests.get(url).content
                pixmap = QPixmap()
                pixmap.loadFromData(data)
                self.setWindowIcon(QIcon(pixmap))
            else:
                self.setWindowIcon(QIcon(logo))
        
        self.central_widget = QWidget() 
        self.layout = QVBoxLayout(self.central_widget) 
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.sizeConstraint = QSizePolicy.Policy.Maximum

        self.setCentralWidget(self.central_widget) 

        self.body()

    def addElement(self, *args):
        for element in args:
            if type(element) in LAYOUTS:
                self.layout.addLayout(element)
            else:
                self.layout.addWidget(element)
    
    def body(self):
        return self.layout

class ViewController():
    def __init__(self, rootView: View) -> None:
        self.rootView = rootView

    def pushView(self, app_type = None):
        self.rootView.show()
    
    def popView(self, app_type = None):
        self.rootView.hide()