import bpy
import os
import subprocess

try:
    from .data_path import datapath
except:
    from data_path import datapath

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
    "description": "AZTools PySide2 Template",
    "category": "AZTools",
    "url": "https://github.com/arizeworks/AZToolsPySide2Template",
}


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

        box.label(text="Edit")
        row = box.row(align=True)
        row.scale_y = 1.5
        row.operator("aztools.open_dir_pyside2_template")
        # row.operator("aztools.reload_aztools_pyside2_template")
        row = box.row(align=True)
        row.scale_y = 1.5
        row.operator("aztools.edit_ui_pyside2_template")
        # row.operator("aztools.update_ui_pyside2_template")

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
            if os.system('"' + datapath["python"]["exe"] + '" -m pip install ' + moduleName) == 0:
                print("Installed " + moduleName)

            else:
                print("Installation Failed")
        else:
            if os.system('"' + datapath["python"]["exe"] + '" -m pip uninstall -y ' + moduleName) == 0:
                print("UnInstalled " + moduleName)

            else:
                print("UnInstallation Failed")

        return {"FINISHED"}


class AZTOOLS_OT_EditUI_PySide2Template(bpy.types.Operator):
    bl_label = "Edit UI"
    bl_idname = "aztools.edit_ui_pyside2_template"
    bl_description = "Edit UI"

    install: bpy.props.BoolProperty(default=True)

    def execute(self, context):
        subprocess.Popen([datapath["pyside2"]["qtdesigner"], datapath["pyside2"]["ui"]])
        return {"FINISHED"}


class AZTOOLS_OT_UpdateUI_PySide2Template(bpy.types.Operator):
    bl_label = "Update UI"
    bl_idname = "aztools.update_ui_pyside2_template"
    bl_description = "Update UI"

    install: bpy.props.BoolProperty(default=True)

    def execute(self, context):
        from .ui_Updater import UpdateUI
        UpdateUI()

        return {"FINISHED"}


class AZTOOLS_OT_ReloadAZTools_PySide2Template(bpy.types.Operator):
    bl_label = "Reload"
    bl_idname = "aztools.reload_aztools_pyside2_template"
    bl_description = "Reload"

    def execute(self, context):
        bpy.ops.preferences.addon_disable(module="AZToolsPySide2Template")

        bpy.ops.preferences.addon_refresh()

        bpy.ops.preferences.addon_enable(module="AZToolsPySide2Template")

        return {"FINISHED"}


class AZTOOLS_OT_OpenDir_PySide2Template(bpy.types.Operator):
    bl_idname = "aztools.open_dir_pyside2_template"
    bl_label = "Open PySide2 Folder"
    bl_description = "Open PySide2 Folder"

    dir: bpy.props.StringProperty(default=datapath["file"]["dir"])

    def execute(self, context):
        open_path = str(self.dir)
        if open_path[-1:] == "\\":
            open_path = open_path[:-1]
        subprocess.Popen(["explorer", open_path])
        print(open_path)
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
    AZTOOLS_OT_OpenDir_PySide2Template,
)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():
    for cls in CLASSES:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
