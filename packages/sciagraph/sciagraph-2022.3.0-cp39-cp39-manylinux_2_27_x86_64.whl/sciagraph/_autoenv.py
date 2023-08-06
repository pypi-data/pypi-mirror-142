"""
Infrastructure for automatically running sciagraph based on an environment
variable.
"""

import os
import sys

variable = "SCIAGRAPH_AUTO_RUN"


def _check():
    value = os.environ.pop("SCIAGRAPH_AUTO_RUN", None)
    if value is None:
        return
    if value != "1":
        raise RuntimeError("SCIAGRAPH_AUTO_RUN can only be set to the string '1'")

    import ctypes

    # TODO: Python 3.10 and later have sys.orig_argv.
    _argv = ctypes.POINTER(ctypes.c_wchar_p)()
    _argc = ctypes.c_int()
    ctypes.pythonapi.Py_GetArgcArgv(ctypes.byref(_argc), ctypes.byref(_argv))
    argv = _argv[: _argc.value]
    args = ["python", "-m", "sciagraph", "run"] + argv[1:]

    os.execv(sys.executable, args)


_check()
