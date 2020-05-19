from cx_Freeze import setup, Executable
import os.path
import sys


# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages=[],
    includes=["numpy", "os", "sympy", "sys", "tkinter"],
    excludes=[],
    include_files=["src/",],
    replace_paths=[("*", "")],
    path=sys.path + ["src"],
)

import sys

base = "Win32GUI" if sys.platform == "win32" else None

executables = [Executable("main.py", base=base)]
setup(
    name="NR Method Solver",
    version="1.0",
    description="A calculator to solves equation(s) with one or two unknown variables.",
    options=dict(build_exe=buildOptions),
    executables=executables,
)
