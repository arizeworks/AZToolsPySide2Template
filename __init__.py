import bpy
import os
import subprocess

try:
    from PySide2 import QtWidgets, QtCore
    INSTALL_MODE = False
except:
    INSTALL_MODE = True

try:
    from .MainWindow import MainWindow
except:
    try:
        from MainWindow import MainWindow
    except:
        pass


bl_info = {
    "name": "AZTools PySide2 Template",
    "version": (0, 1),
    "blender": (3, 4, 0),
    "author": "Arizeworks",
    "location": "3D View > N-Panel / T-Panel > AZTools",
    "warning": "Warning: this addon is still developping",
    "description": "AZTools",
    "category": "AZTools",
    "url": "https://github.com/arizeworks/AZToolsPySide2Template",
}


# VAR ###################################################################################


file_dir = os.path.join(os.path.dirname(__file__))
blender_python_dir_path = os.path.abspath(os.__file__ + "/../..")
blender_python_path = blender_python_dir_path + "/bin/python.exe"

pyside2_path = blender_python_dir_path + "/lib/site-packages/PySide2"
pyside2_qtdesigner = pyside2_path + "/designer.exe"
pyside2_uic = blender_python_dir_path + "/Scripts/pyside2-uic.exe"

UI_NAME = "PySide2Template"
target_uipy = file_dir + f"/ui_{UI_NAME}.py"
target_ui = file_dir + f"/{UI_NAME}.ui"


# Blender UI ############################################################################


def AZToolsBlender(self, context):
    layout = self.layout
    box = layout.box()
    if INSTALL_MODE:
        # PySide2 インストールボタン
        box.label(text="PySide2")
        row = box.row(align=True)
        row.scale_y = 1.5
        row.operator("aztools.install_pyside2_template").install = True
    else:
        # PySide2 UIの表示ボタン
        box.label(text="AZTools PySide2 Template")
        row = box.row(align=True)
        row.scale_y = 1.5
        row.operator("aztools.display_window_pyside2_template")
        row = box.row(align=True)
        row.scale_y = 1.5
        row.operator("aztools.edit_ui_pyside2_template")
        row.operator("aztools.update_ui_pyside2_template")

        # PySide2 アンインストールボタン
        box.label(text="PySide2")
        row = box.row(align=True)
        row.scale_y = 1.5
        row.alert = True
        row.operator("aztools.install_pyside2_template", text="Uninstall PySide2").install = False


# Nボタンメニューに表示
class AZTOOLS_PT_NPanel_PySide2Template(bpy.types.Panel):
    bl_label = "AZTools PySide2 Template"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "AZTools"

    def draw(self, context):
        AZToolsBlender(self, context)


# Tボタンメニューに表示
class AZTOOLS_PT_TPanel_PySide2Template(bpy.types.Panel):
    bl_label = "AZTools PySide2 Template"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"

    def draw(self, context):
        AZToolsBlender(self, context)


# Blender Operator ############################################################################


class AZTOOLS_OT_DisplayWindow_PySide2Template(bpy.types.Operator):
    bl_idname = "aztools.display_window_pyside2_template"
    bl_label = "Display Window"
    bl_description = "Display Window"

    # 初期処理
    def __init__(self):
        print("hello init")
        self.app = QtWidgets.QApplication.instance()
        if not self.app:
            self.app = QtWidgets.QApplication(["blender"])

        # blender_app = BlenderApplication.instance()
        # blender_app = bqt.instantiate_application().blender_widget

        self.event_loop = QtCore.QEventLoop()
        self.widget = MainWindow(parent=None)

        # app = QtWidgets.QApplication.instance()
        # if app is None:
        #     app = QtWidgets.QApplication(sys.argv)
        # window = MainWindow()
        # window.show()
        # app.exec_()

    # 初期実行処理
    def invoke(self, context, event):
        print("hello invoke")
        self.execute(context)
        return {"RUNNING_MODAL"}

    # 実行
    def execute(self, context):
        print("hello AZToolsBlender")

        if context.area.type == "VIEW_3D":
            context.window_manager.modal_handler_add(self)
            return {"RUNNING_MODAL"}
        else:
            return {"CANCELLED"}
        return {"FINISHED"}

    # モーダル処理
    def modal(self, context, event):
        if event.type == "LEFTMOUSE":
            if event.value == "PRESS":
                return {"PASS_THROUGH"}

        return {"PASS_THROUGH"}

    # 終了処理
    def __del__(self):
        print("hello del")


class AZTOOLS_OT_InstallPySide2_PySide2Template(bpy.types.Operator):
    bl_label = "Install PySide2"
    bl_idname = "aztools.install_pyside2_template"
    bl_description = "Install PySide2"

    install: bpy.props.BoolProperty(default=True)

    def execute(self, context):
        moduleName = "PySide2"

        if self.install:
            if os.system('"' + blender_python_path + '" -m pip install ' + moduleName) == 0:
                print("Installed " + moduleName)
                bpy.ops.aztools.reload_aztools_pyside2template_gui()
            else:
                print("Installation Failed")
        else:
            if os.system('"' + blender_python_path + '" -m pip uninstall -y ' + moduleName) == 0:
                print("UnInstalled " + moduleName)
                bpy.ops.aztools.reload_aztools_pyside2template_gui()
            else:
                print("UnInstallation Failed")

        return {"FINISHED"}


class AZTOOLS_OT_EditUI_PySide2Template(bpy.types.Operator):
    bl_label = "Edit UI"
    bl_idname = "aztools.edit_ui_pyside2_template"
    bl_description = "Edit UI"

    install: bpy.props.BoolProperty(default=True)

    def execute(self, context):
        subprocess.Popen([pyside2_qtdesigner, target_ui])
        return {"FINISHED"}


class AZTOOLS_OT_UpdateUI_PySide2Template(bpy.types.Operator):
    bl_label = "Update UI"
    bl_idname = "aztools.update_ui_pyside2_template"
    bl_description = "Update UI"

    install: bpy.props.BoolProperty(default=True)

    def execute(self, context):
        try:
            cmd = " ".join([pyside2_uic, "-o " + target_uipy, target_ui])
            subprocess.call(cmd, shell=True)
            print("success")
        except Exception as e:
            print(e)
        return {"FINISHED"}


class AZTOOLS_OT_ReloadAZTools_PySide2Template(bpy.types.Operator):
    bl_label = "Reload"
    bl_idname = "aztools.reload_aztools_pyside2template_gui"

    def execute(self, context):
        bpy.ops.preferences.addon_disable(module="AZTools PySide2 Template")
        bpy.ops.preferences.addon_refresh()
        bpy.ops.preferences.addon_enable(module="AZTools PySide2 Template")
        bpy.ops.aztools.display_window()

        return {"FINISHED"}


# Blender register ############################################################################


CLASSES = (
    AZTOOLS_OT_DisplayWindow_PySide2Template,
    AZTOOLS_PT_NPanel_PySide2Template,
    AZTOOLS_PT_TPanel_PySide2Template,
    AZTOOLS_OT_InstallPySide2_PySide2Template,
    AZTOOLS_OT_EditUI_PySide2Template,
    AZTOOLS_OT_UpdateUI_PySide2Template,
    AZTOOLS_OT_ReloadAZTools_PySide2Template,
)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():
    for cls in CLASSES:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
