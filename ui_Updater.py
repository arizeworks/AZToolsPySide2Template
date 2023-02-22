import subprocess
import os

UI_NAME = "PySide2Template"
os_python_path = os.path.expandvars("%LOCALAPPDATA%/Programs/Python/Python310")
pyside2_uic = os_python_path + "/Scripts/pyside2-uic.exe"
target_uipy = f"ui_{UI_NAME}.py"
target_ui = f"{UI_NAME}.ui"


def UpdateUI():
    try:
        cmd = " ".join([pyside2_uic, "-o " + target_uipy, target_ui])
        subprocess.call(cmd, shell=True)
        print("success")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    UpdateUI()
