import gui_creator as gc
from gui_creator.library import *
from gui_creator.library import InitProtocol
from gui_creator.elements import *
from gui_creator.types.app_types import SpacerFlag, _
import random

App = gc.App(app_type="pyqt6") 

dark = None

class MainView(View):
    def __init__(self, initProtocol: InitProtocol):
        super().__init__(initProtocol)

    def body(self):
        darknodeLabel = Text(text="You can't close this 😂", fontSize=30, fontColor="black")
        darknodeLabel.fontSize = 10
        darknodeLabel.align("top")
        darknodeLabel.setFixedSize(400, 100)
        darknodeLabel.setMargin(10)
        
        dark = darknodeLabel

        self.addElement(darknodeLabel)
        self.addElement(Spacer(SpacerFlag.Vertical))

initProtocol = InitProtocol(title="Darknode Test", 
                            width=800, 
                            height=600, 
                            backgroundColor="white", 
                            logo="https://darknode.dev/logo.png", 
                            hideTitleBar=True)

mainView = MainView(initProtocol=initProtocol)
mainViewController = ViewController(mainView)

App.rootViewController = mainViewController

App.launch()