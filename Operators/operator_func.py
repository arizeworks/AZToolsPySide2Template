from PySide2 import QtCore, QtGui
from collections import defaultdict
import inspect

try:
    import bpy
    from .. import data_path
    from .. import ui_PySide2Template
    DEBUG_MODE = False
except:
    import data_path
    import ui_PySide2Template
    DEBUG_MODE = True


def bpy_execute(bpy_cmd):

    area = defaultdict(dict)
    context = defaultdict(dict)
    # Blenderのメインウィンドウ取得
    with bpy.context.temp_override(window=bpy.context.window_manager.windows[0]):
        if "context['WINDOW']" in bpy_cmd:
            context['WINDOW'] = bpy.context.copy()
            print("context['WINDOW']")

        for a in bpy.context.screen.areas:
            if a.type == 'VIEW_3D':

                area['VIEW_3D'] = a
                try:
                    with bpy.context.temp_override(area=area['VIEW_3D']):
                        context['VIEW_3D'] = bpy.context.copy()
                        print("UPDATED: context['VIEW_3D']")
                except Exception as e:
                    print(e)

            if a.type == 'IMAGE_EDITOR':
                area['IMAGE_EDITOR'] = a
                try:
                    with bpy.context.temp_override(area=area['IMAGE_EDITOR']):
                        context['IMAGE_EDITOR'] = bpy.context.copy()
                        print("UPDATED: context['IMAGE_EDITOR']")
                except Exception as e:
                    print(e)

        # 実行
        try:
            exec(bpy_cmd)
            print("SUCCESS: " + bpy_cmd)
        except:
            print("ERROR: " + bpy_cmd)

        return context




def pushButton_bpy(pushButton, bpy_cmd: str, icon: str):
    pushButton.setIcon(QtGui.QIcon(icon))
    pushButton.setIconSize(QtCore.QSize(24, 24))
    pushButton.setToolTip(str(bpy_cmd))

    if DEBUG_MODE == False:
        pushButton.clicked.connect(lambda: bpy_execute(bpy_cmd))
    else:
        pushButton.setStyleSheet("background-color : green")
        pushButton.clicked.connect(lambda: print(str(bpy_cmd)))

    if bpy_cmd == "":
        pushButton.setEnabled(False)
        pushButton.setStyleSheet("background-color : rgba(0, 0, 0, 0.2)")
        pushButton.setStyleSheet("color : rgb(0, 0, 0)")
        


def pushButton_func(pushButton, func_cmd, icon):
    pushButton.setIcon(QtGui.QIcon(icon))
    pushButton.setIconSize(QtCore.QSize(24, 24))
    if func_cmd is not None or func_cmd != "":
        try:
            ToolTip = "".join(inspect.getsourcelines(func_cmd)[0][0].replace("lambda: ", "").split(",")[1:-1])
        except:
            ToolTip = None
    else:
        ToolTip = None
    pushButton.setToolTip(ToolTip)

    if DEBUG_MODE == False:
        pushButton.clicked.connect(func_cmd)
    else:
        pushButton.setStyleSheet("background-color : blue")
        pushButton.clicked.connect(lambda: print(ToolTip))

    if func_cmd is None or func_cmd == "":
        pushButton.setEnabled(False)
        pushButton.setStyleSheet("background-color : rgb(0, 0, 0,0.2)")
        pushButton.setStyleSheet("color : rgb(0, 0, 0)")


def checkBox_bpy(checkBox, bpy_cmd: str):
    checkBox.setToolTip(str(bpy_cmd))

    def isChecked():
        data_path.checkbox_state[bpy_cmd] = checkBox.isChecked()

    if DEBUG_MODE == False:
        # init
        bpy_execute(f"data_path.checkbox_state[{bpy_cmd}] = " + bpy_cmd)
        checkBox.setChecked(data_path.checkbox_state)

        checkBox.stateChanged.connect(lambda: [isChecked(),
                                               bpy_execute(bpy_cmd + f" = data_path.checkbox_state[{bpy_cmd}]"),
                                               checkBox.setChecked(data_path.checkbox_state[bpy_cmd]),
                                               print(data_path.checkbox_state[bpy_cmd])])

    else:
        checkBox.setStyleSheet("background-color : green")
        checkBox.clicked.connect(lambda: print(str(bpy_cmd)))

    if bpy_cmd == "":
        checkBox.setEnabled(False)
        checkBox.setStyleSheet("background-color : rgba(0, 0, 0, 0.2)")
        checkBox.setStyleSheet("color : rgb(0, 0, 0)")
        


def lineEdit_bpy(lineEdit, bpy_cmd: str):
    if DEBUG_MODE == False:
        bpy_execute("data_path.line_edit['" + bpy_cmd + "'] = " + bpy_cmd)
        lineEdit.setText(data_path.line_edit[bpy_cmd])

    if bpy_cmd == "":
        lineEdit.setEnabled(False)
        lineEdit.setStyleSheet("background-color : rgba(0, 0, 0, 0.2)")
        lineEdit.setStyleSheet("color : rgb(0, 0, 0)")
        
