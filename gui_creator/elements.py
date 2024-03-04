from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy, QVBoxLayout, QMainWindow, QStackedLayout, QStackedWidget
from PyQt6.QtCore import QSize, Qt
from .types.app_types import SpacerFlag

class Text(QLabel):
    widthConstant = 41/7
    heightConstant = 12/7

    def __init__(self, text, fontSize, fontColor="white", backgroundColor="transparent"):
        super().__init__()
        self.setText(text)
        self.setFont(QFont("Arial", fontSize))
        self.setStyleSheet(f"color: {fontColor}; background-color: {backgroundColor};")

        self.backgroundColor = backgroundColor
        self.text = text
        self.fontColor = fontColor
        self.fontSize = fontSize

        print(chr(0x200b).__len__())
        
        self.widthConstant *= chr(0x200b).__len__()

        self.setFixedSize(self.fontSize * self.widthConstant, self.fontSize * self.heightConstant)

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, text):
        self._text = text
        self.setText(text)

    @property
    def fontColor(self):
        return self._fontColor
    
    @fontColor.setter
    def fontColor(self, fontColor):
        self._fontColor = fontColor
        self.setStyleSheet(f"color: {fontColor}; background-color: {self.backgroundColor};")
    
    @property
    def fontSize(self):
        return self._fontSize
    
    @fontSize.setter
    def fontSize(self, fontSize):
        self._fontSize = fontSize
        self.setFont(QFont("Arial", fontSize))
        self.setFixedSize(self.fontSize * self.widthConstant, self.fontSize * self.heightConstant)
    
    def size(self, width, height):
        self.setFixedSize(width * self.widthConstant, height * self.heightConstant)
        return self
        
    def frame(self, height=None, width=None):
        self.frame.height = height
        self.frame.width = width
        self.setFixedSize(self.frame.width, self.frame.height)
        return self
    
    def padding(self, edges, padding_value):
        edges_mapping = {
            "top": self.set_padding_top,
            "bottom": self.set_padding_bottom,
            "leading": self.set_padding_leading,
            "trailing": self.set_padding_trailing
        }

        if type(edges) is not list:
            if edges not in edges_mapping:
                raise ValueError("Invalid padding edge")
            else:
                edges_mapping[edges](padding_value)
        else:  
            for edge in edges:
                if edge not in edges_mapping:
                    raise ValueError("Invalid padding edge")

                edges_mapping[edge](padding_value)
            
            
            return self

    def set_padding_top(self, padding_value):
        self.setContentsMargins(self.contentsMargins().left(), padding_value, self.contentsMargins().right(), self.contentsMargins().bottom())

    def set_padding_bottom(self, padding_value):
        self.setContentsMargins(self.contentsMargins().left(), self.contentsMargins().top(), self.contentsMargins().right(), padding_value)

    def set_padding_leading(self, padding_value):
        self.setContentsMargins(padding_value, self.contentsMargins().top(), self.contentsMargins().right(), self.contentsMargins().bottom())

    def set_padding_trailing(self, padding_value):
        self.setContentsMargins(self.contentsMargins().left(), self.contentsMargins().top(), padding_value, self.contentsMargins().bottom())

    def align(self, alignment):
        layout = self.layout()
        if layout is not None:
            if alignment == "leading":
                layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
            elif alignment == "trailing":
                layout.setAlignment(Qt.AlignmentFlag.AlignRight)
            elif alignment == "center":
                layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            elif alignment == "top":
                layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            elif alignment == "bottom":
                layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
            elif alignment == "fill":
                layout.setAlignment(Qt.AlignmentFlag.AlignJustify)
            else:
                raise ValueError("Invalid alignment value")
            
class Button(QPushButton):
    def __init__(self, text, fontSize, fontColor="white", backgroundColor="transparent"):
        super().__init__()
        self.setText(text)
        self.setFont(QFont("Arial", fontSize))
        self.setStyleSheet(f"color: {fontColor}; background-color: {backgroundColor};")\
        
    def onClick(self, callback, *args):
        self.clicked.connect(lambda: callback(*args))
        return self
    
    def frame(self, height=None, width=None):
        self.frame.height = height
        self.frame.width = width
        self.setFixedSize(self.frame.width, self.frame.height)
        return self
    
    def padding(self, edges, padding_value):
        edges_mapping = {
            "top": self.set_padding_top,
            "bottom": self.set_padding_bottom,
            "leading": self.set_padding_leading,
            "trailing": self.set_padding_trailing
        }

        if type(edges) is not list:
            if edges not in edges_mapping:
                raise ValueError("Invalid padding edge")
            else:
                edges_mapping[edges](padding_value)
        else:  
            for edge in edges:
                if edge not in edges_mapping:
                    raise ValueError("Invalid padding edge")

                edges_mapping[edge](padding_value)
            
            
            return self

    def set_padding_top(self, padding_value):
        self.setContentsMargins(self.contentsMargins().left(), padding_value, self.contentsMargins().right(), self.contentsMargins().bottom())

    def set_padding_bottom(self, padding_value):
        self.setContentsMargins(self.contentsMargins().left(), self.contentsMargins().top(), self.contentsMargins().right(), padding_value)

    def set_padding_leading(self, padding_value):
        self.setContentsMargins(padding_value, self.contentsMargins().top(), self.contentsMargins().right(), self.contentsMargins().bottom())

    def set_padding_trailing(self, padding_value):
        self.setContentsMargins(self.contentsMargins().left(), self.contentsMargins().top(), padding_value, self.contentsMargins().bottom())

    def align(self, alignment):
        layout = self.layout()
        if layout is not None:
            if alignment == "leading":
                layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
            elif alignment == "trailing":
                layout.setAlignment(Qt.AlignmentFlag.AlignRight)
            elif alignment == "center":
                layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            elif alignment == "top":
                layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            elif alignment == "bottom":
                layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
            elif alignment == "fill":
                layout.setAlignment(Qt.AlignmentFlag.AlignJustify)
            else:
                raise ValueError("Invalid alignment value")
    
    def setCornerRadius(self, radius):
        self.setStyleSheet(f"border-radius: {radius};")
        return self
    
class Group(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        
        layout = QVBoxLayout()
        
        for widget in args:
            layout.addWidget(widget)
        
        self.setLayout(layout)
    
    def frame(self, height=None, width=None):
        self.frame.height = height
        self.frame.width = width
        self.setFixedSize(self.frame.width, self.frame.height)
        return self
    
    def padding(self, edges, padding_value):
        edges_mapping = {
            "top": self.set_padding_top,
            "bottom": self.set_padding_bottom,
            "leading": self.set_padding_leading,
            "trailing": self.set_padding_trailing
        }

        if type(edges) is not list:
            if edges not in edges_mapping:
                raise ValueError("Invalid padding edge")
            else:
                edges_mapping[edges](padding_value)
        else:  
            for edge in edges:
                if edge not in edges_mapping:
                    raise ValueError("Invalid padding edge")

                edges_mapping[edge](padding_value)
            
            
            return self
    
    def set_padding_top(self, padding_value):
        layout = self.layout()
        if layout is not None:
            layout.setContentsMargins(layout.contentsMargins().left(), padding_value, layout.contentsMargins().right(), layout.contentsMargins().bottom())
    
    def set_padding_bottom(self, padding_value):
        layout = self.layout()
        if layout is not None:
            layout.setContentsMargins(layout.contentsMargins().left(), layout.contentsMargins().top(), layout.contentsMargins().right(), padding_value)
    
    def set_padding_leading(self, padding_value):
        layout = self.layout()
        if layout is not None:
            layout.setContentsMargins(padding_value, layout.contentsMargins().top(), layout.contentsMargins().right(), layout.contentsMargins().bottom())
    
    def set_padding_trailing(self, padding_value):
        layout = self.layout()
        if layout is not None:
            layout.setContentsMargins(layout.contentsMargins().left(), layout.contentsMargins().top(), padding_value, layout.contentsMargins().bottom())
    
    def align(self, alignment):
        layout = self.layout()
        if layout is not None:
            if alignment == "leading":
                layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
            elif alignment == "trailing":
                layout.setAlignment(Qt.AlignmentFlag.AlignRight)
            elif alignment == "center":
                layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            elif alignment == "top":
                layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            elif alignment == "bottom":
                layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
            elif alignment == "fill":
                layout.setAlignment(Qt.AlignmentFlag.AlignJustify)
            else:
                raise ValueError("Invalid alignment value")

class HStack(QHBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__()

        for widget in args:
            self.addWidget(widget)

        if kwargs.get("spacing"):  
            self.setSpacing(kwargs.get("spacing"))
            
    def align(self, alignment):
        layout = self
        if layout is not None:
            if alignment == "leading":
                layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
            elif alignment == "trailing":
                layout.setAlignment(Qt.AlignmentFlag.AlignRight)
            elif alignment == "center":
                layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            elif alignment == "top":
                layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            elif alignment == "bottom":
                layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
            elif alignment == "fill":
                layout.setAlignment(Qt.AlignmentFlag.AlignJustify)
            else:
                raise ValueError("Invalid alignment value")
            
    def padding(self, edges, padding_value):
        edges_mapping = {
            "top": self.set_padding_top,
            "bottom": self.set_padding_bottom,
            "leading": self.set_padding_leading,
            "trailing": self.set_padding_trailing
        }

        if type(edges) is not list:
            if edges not in edges_mapping:
                raise ValueError("Invalid padding edge")
            else:
                edges_mapping[edges](padding_value)
        else:  
            for edge in edges:
                if edge not in edges_mapping:
                    raise ValueError("Invalid padding edge")

                edges_mapping[edge](padding_value)
            
            
            return self
    
    def set_padding_top(self, padding_value):
        layout = self.layout()
        if layout is not None:
            layout.setContentsMargins(layout.contentsMargins().left(), padding_value, layout.contentsMargins().right(), layout.contentsMargins().bottom())
    
    def set_padding_bottom(self, padding_value):
        layout = self.layout()
        if layout is not None:
            layout.setContentsMargins(layout.contentsMargins().left(), layout.contentsMargins().top(), layout.contentsMargins().right(), padding_value)
    
    def set_padding_leading(self, padding_value):
        layout = self.layout()
        if layout is not None:
            layout.setContentsMargins(padding_value, layout.contentsMargins().top(), layout.contentsMargins().right(), layout.contentsMargins().bottom())
    
    def set_padding_trailing(self, padding_value):
        layout = self.layout()
        if layout is not None:
            layout.setContentsMargins(layout.contentsMargins().left(), layout.contentsMargins().top(), padding_value, layout.contentsMargins().bottom())

class VStack(QVBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__()

        for widget in args:
            self.addWidget(widget)
    
        if kwargs.get("spacing"):
            self.setSpacing(kwargs.get("spacing"))
    
    def align(self, alignment):
        layout = self
        if layout is not None:
            if alignment == "leading":
                layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
            elif alignment == "trailing":
                layout.setAlignment(Qt.AlignmentFlag.AlignRight)
            elif alignment == "center":
                layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            elif alignment == "top":
                layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            elif alignment == "bottom":
                layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
            elif alignment == "fill":
                layout.setAlignment(Qt.AlignmentFlag.AlignJustify)
            else:
                raise ValueError("Invalid alignment value")
    
    def padding(self, edges, padding_value):
        edges_mapping = {
            "top": self.set_padding_top,
            "bottom": self.set_padding_bottom,
            "leading": self.set_padding_leading,
            "trailing": self.set_padding_trailing
        }

        if type(edges) is not list:
            if edges not in edges_mapping:
                raise ValueError("Invalid padding edge")
            else:
                edges_mapping[edges](padding_value)
        else:  
            for edge in edges:
                if edge not in edges_mapping:
                    raise ValueError("Invalid padding edge")

                edges_mapping[edge](padding_value)
            
            
            return self
    
    def set_padding_top(self, padding_value):
        layout = self.layout()
        if layout is not None:
            layout.setContentsMargins(layout.contentsMargins().left(), padding_value, layout.contentsMargins().right(), layout.contentsMargins().bottom())
    
    def set_padding_bottom(self, padding_value):
        layout = self.layout()
        if layout is not None:
            layout.setContentsMargins(layout.contentsMargins().left(), layout.contentsMargins().top(), layout.contentsMargins().right(), padding_value)
    
    def set_padding_leading(self, padding_value):
        layout = self.layout()
        if layout is not None:
            layout.setContentsMargins(padding_value, layout.contentsMargins().top(), layout.contentsMargins().right(), layout.contentsMargins().bottom())
    
    def set_padding_trailing(self, padding_value):
        layout = self.layout()
        if layout is not None:
            layout.setContentsMargins(layout.contentsMargins().left(), layout.contentsMargins().top(), padding_value, layout.contentsMargins().bottom())

class ZStack(QStackedLayout):
    def __init__(self, *args, **kwargs):
        super().__init__()

        for widget in args:
            self.addWidget(widget)  
        
        if kwargs.get("spacing"):
            self.setSpacing(kwargs.get("spacing"))
    
    def align(self, alignment):
        layout = self
        if layout is not None:
            if alignment == "leading":
                layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
            elif alignment == "trailing":
                layout.setAlignment(Qt.AlignmentFlag.AlignRight)
            elif alignment == "center":
                layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            elif alignment == "top":
                layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            elif alignment == "bottom":
                layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
            elif alignment == "fill":
                layout.setAlignment(Qt.AlignmentFlag.AlignJustify)
            else:
                raise ValueError("Invalid alignment value")
            
    def padding(self, edges, padding_value):
        edges_mapping = {
            "top": self.set_padding_top,
            "bottom": self.set_padding_bottom,
            "leading": self.set_padding_leading,
            "trailing": self.set_padding_trailing
        }

        if type(edges) is not list:
            if edges not in edges_mapping:
                raise ValueError("Invalid padding edge")
            else:
                edges_mapping[edges](padding_value)
        else:  
            for edge in edges:
                if edge not in edges_mapping:
                    raise ValueError("Invalid padding edge")

                edges_mapping[edge](padding_value)
            
            
            return self
    
    def set_padding_top(self, padding_value):
        layout = self.layout()
        if layout is not None:
            layout.setContentsMargins(layout.contentsMargins().left(), padding_value, layout.contentsMargins().right(), layout.contentsMargins().bottom())
    
    def set_padding_bottom(self, padding_value):
        layout = self.layout()
        if layout is not None:
            layout.setContentsMargins(layout.contentsMargins().left(), layout.contentsMargins().top(), layout.contentsMargins().right(), padding_value)
    
    def set_padding_leading(self, padding_value):
        layout = self.layout()
        if layout is not None:
            layout.setContentsMargins(padding_value, layout.contentsMargins().top(), layout.contentsMargins().right(), layout.contentsMargins().bottom())
    
    def set_padding_trailing(self, padding_value):
        layout = self.layout()
        if layout is not None:
            layout.setContentsMargins(layout.contentsMargins().left(), layout.contentsMargins().top(), padding_value, layout.contentsMargins().bottom())
    
            
class Spacer(QWidget):
    def __init__(self, spacerType: SpacerFlag = SpacerFlag.All):
        super().__init__()

        if spacerType == SpacerFlag.Horizontal:
            self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        elif spacerType == SpacerFlag.Vertical:
            self.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding)
        else:
            self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            

LAYOUTS = [HStack, VStack]