import os
from collections import defaultdict


checkbox_state = defaultdict(dict)
line_edit = defaultdict(dict)
line_edit["lineEdit"] = ""

datapath = defaultdict(dict)

datapath["file"]["dir"] = os.path.join(os.path.dirname(__file__))

datapath["python"]["dir"] = os.path.abspath(os.__file__ + "\\..\\..")
datapath["python"]["exe"] = datapath["python"]["dir"] + "\\bin\\python.exe"

datapath["pyside2"]["dir"] = datapath["python"]["dir"] + "\\lib\\site-packages\\PySide2"
datapath["pyside2"]["qtdesigner"] = datapath["pyside2"]["dir"] + "\\designer.exe"

datapath["pyside2"]["uic"] = datapath["python"]["dir"] + "\\Scripts\\pyside2-uic.exe"

UI_NAME = "PySide2Template"
datapath["pyside2"]["uipy"] = datapath["file"]["dir"] + f"\\ui_{UI_NAME}.py"
datapath["pyside2"]["ui"] = datapath["file"]["dir"] + f"\\{UI_NAME}.ui"
