from cx_Freeze import setup, Executable
import os.path
import sys


PYTHON_INSTALL_DIR = os.path.dirname(sys.executable)
# os.environ["TCL_LIBRARY"] = os.path.join(PYTHON_INSTALL_DIR, "tcl", "tcl8.6")
# os.environ["TK_LIBRARY"] = os.path.join(PYTHON_INSTALL_DIR, "tcl", "tk8.6")

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages=["numpy", "os", "sympy", "sys", "tkinter"],
    includes=[],
    excludes=[],
    include_files=[
        # "src/",
        # (
        #     os.path.join(PYTHON_INSTALL_DIR, "DLLs", "tk86t.dll"),
        #     os.path.join("lib", "tk86t.dll"),
        # ),
        # (
        #     os.path.join(PYTHON_INSTALL_DIR, "DLLs", "tcl86t.dll"),
        #     os.path.join("lib", "tcl86t.dll"),
        # ),
    ],
    # replace_paths=[("*", "")],
    path=sys.path + ["lib"],
)

base = "Win32GUI" if sys.platform == "win32" else None

executables = [Executable("main.py", base=base)]
setup(
    name="NR Method Solver",
    version="1.0",
    description="A calculator to solves equation(s) with one or two unknown variables.",
    options=dict(build_exe=buildOptions),
    executables=executables,
)
