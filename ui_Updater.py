import os
try:
    from .data_path import datapath
except:
    from data_path import datapath


def UpdateUI():
    cmd = fr'"{datapath["pyside2"]["uic"]}" -o {datapath["pyside2"]["uipy"]} {datapath["pyside2"]["ui"]}'
    print(cmd)
    if os.system(cmd) == 0:
        print("success")
    else:
        print("failed")


if __name__ == "__main__":
    UpdateUI()
