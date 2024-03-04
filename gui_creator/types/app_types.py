class AppType:
    TYPE_PYQT6 = "pyqt6"
    TYPE_TKINTER = "tkinter"

    def __init__(self, app_type: str = None):
        if app_type != self.TYPE_PYQT6 and app_type != self.TYPE_TKINTER:
            raise ValueError("Invalid app type")    
        self.app_type = app_type

class CGFloat(float):
    def __init__(self, value):
        super().__init__()
        self.value = value

class FontSize(CGFloat):
    def __init__(self, value):
        super().__init__(value)

class Color(str):
    def __init__(self, value):
        super().__init__()
        self.value = value

class SpacerFlag():
    Horizontal = "hspacer"
    Vertical = "vspacer"
    All = "all"

    def __init__(self, spacer_type: str = None):
        if spacer_type != self.Horizontal and spacer_type != self.Vertical and spacer_type != self.All:
            raise ValueError("Invalid spacer flag")    
        self.spacer_type = spacer_type

class _():
    center = "center"
    top = "top"
    bottom = "bottom"
    leading = "leading"
    trailing = "trailing"
    fill = "fill"

    def __init__(self, alignment_type: str = None):
        if alignment_type != self.center and alignment_type != self.top and alignment_type != self.bottom and alignment_type != self.leading and alignment_type != self.trailing and alignment_type != self.fill:
            raise ValueError("Invalid alignment flag")    
        self.alignment_type = alignment_type
        