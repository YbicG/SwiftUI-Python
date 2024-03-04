# GUI Creator

UNDER HEAVY DEVELOPMENT! GUI Creator is a Python library for creating graphical user interfaces (GUIs) using PyQt6 and/or Tkinter. It provides a simple interface for building GUIs with various elements like labels, buttons, and spacers.

## Installation

You can install GUI Creator using pip:

```
pip install gui_creator
```

## Usage

Here's an example of how to create a simple GUI using GUI Creator:

```python
import gui_creator as gc
from gui_creator.library import *
from gui_creator.library import InitProtocol
from gui_creator.elements import *
from gui_creator.types.app_types import SpacerFlag

App = gc.App(app_type="pyqt6") 

# Define your main view class
class MainView(View):
    def __init__(self, initProtocol: InitProtocol):
        super().__init__(initProtocol)

    def body(self):
        darknodeLabel = Text(text="SwiftUI in Python", fontSize=30, fontColor="black")
        darknodeLabel.fontSize = 10
        darknodeLabel.align("top")
        darknodeLabel.setFixedSize(400, 100)
        darknodeLabel.setMargin(10)
        
        self.addElement(darknodeLabel)
        self.addElement(Spacer(SpacerFlag.Vertical))

# Initialize the application with the given parameters
initProtocol = InitProtocol(
                            title="This is an application title.", 
                            width=800, 
                            height=600, 
                            backgroundColor="white", 
                            logo="https://example.com/logo"
                            )

# Create the main view and view controller
mainView = MainView(initProtocol=initProtocol)
mainViewController = ViewController(mainView)

# Set the root view controller and launch the application
App.rootViewController = mainViewController
App.launch()
```

## Contributing

Contributions to GUI Creator are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request on GitHub.

## License

This project is licensed under the [MIT License](LICENSE)
