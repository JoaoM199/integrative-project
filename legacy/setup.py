import sys
from cx_Freeze import setup, Executable

# Bibliotecas externas depois de "includes"
# "package":["os"],
build_exe_options = {"includes":["tkinter","webbrowser","math","numpy","scipy","matplotlib"]}


base = None
if sys.platform == "win32":
    base = "win32GUI"

setup(
    name="ACQAC",
    version="0.1",
    description = "Advanced Calculator for Quantitative Analytical Calculations",
    options={"build_exe": build_exe_options},
    executables=[Executable("init.py", base=base, icon="Icon.ico")]
)