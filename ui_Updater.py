import subprocess
import os


file_dir = os.path.join(os.path.dirname(__file__))
blender_python_dir_path = os.path.abspath(os.__file__ + "/../..")
blender_python_path = blender_python_dir_path + "/bin/python.exe"

pyside2_path = blender_python_dir_path + "/lib/site-packages/PySide2"
pyside2_qtdesigner = pyside2_path + "/designer.exe"
pyside2_uic = blender_python_dir_path + "/Scripts/pyside2-uic.exe"

UI_NAME = "PySide2Template"
target_uipy = file_dir + f"/ui_{UI_NAME}.py"
target_ui = file_dir + f"/{UI_NAME}.ui"


def UpdateUI():
    try:
        cmd = " ".join([pyside2_uic, "-o " + target_uipy, target_ui])
        subprocess.call(cmd, shell=True)
        print("success")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    UpdateUI()
