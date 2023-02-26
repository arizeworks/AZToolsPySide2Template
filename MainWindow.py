import sys
import os


from PySide2 import QtWidgets, QtCore

try:
    from .data_path import datapath
except:
    from data_path import datapath

try:
    from . import ui_PySide2Template
    from .Operators import operator_func as func
    DEBUG_MODE = False
except:
    import ui_PySide2Template
    from Operators import operator_func as func
    DEBUG_MODE = True



# PySide2 UI ############################################################################

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # UIセットアップ
        self.ui = ui_PySide2Template.Ui_MainWindow()
        self.ui.setupUi(self)

        # 現状Blenderのウィンドウ取得方法が不明なため、最前面表示
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowStaysOnTopHint)
        self.loadSettings()


        func.pushButton_bpy(self.ui.pushButton, bpy_cmd="bpy.ops.mesh.primitive_monkey_add(context['VIEW_3D'])", icon="")
        self.ui.pushButton.setText("Add Monkey")



        # ウィンドウを表示
        self.show()



    def loadSettings(self):
        setting = QtCore.QSettings((datapath["file"]["dir"] + "\\Settings.ini"), QtCore.QSettings.IniFormat)
        # lineEdit.setText(setting.value(lineEdit.objectName()))
        self.restoreGeometry(setting.value("geometry"))


    def saveSettings(self):
        setting = QtCore.QSettings((datapath["file"]["dir"] + "\\Settings.ini"), QtCore.QSettings.IniFormat)
        # setting.setValue(self.ui.lineEdit_import_fbx.objectName(), self.ui.lineEdit_import_fbx.text())
        setting.setValue("geometry", self.saveGeometry())


    def closeEvent(self, event):
        self.saveSettings()
        print('Window closed')


if DEBUG_MODE:
    app = QtWidgets.QApplication(sys.argv)
    event_loop = QtCore.QEventLoop()
    AZTools = MainWindow()
    AZTools.show()

    sys, exit(app.exec_())
