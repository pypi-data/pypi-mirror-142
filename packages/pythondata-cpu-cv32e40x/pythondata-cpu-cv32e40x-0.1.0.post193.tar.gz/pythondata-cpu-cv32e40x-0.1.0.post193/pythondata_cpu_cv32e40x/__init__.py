import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.1.0.post193"
version_tuple = (0, 1, 0, 193)
try:
    from packaging.version import Version as V
    pversion = V("0.1.0.post193")
except ImportError:
    pass

# Data version info
data_version_str = "0.1.0.post67"
data_version_tuple = (0, 1, 0, 67)
try:
    from packaging.version import Version as V
    pdata_version = V("0.1.0.post67")
except ImportError:
    pass
data_git_hash = "584254b061e77f989b2db36e5e820420a9bfc922"
data_git_describe = "0.1.0-67-g584254b"
data_git_msg = """\
commit 584254b061e77f989b2db36e5e820420a9bfc922
Merge: f6656cd b807fa3
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Tue Mar 15 11:08:14 2022 +0100

    Merge pull request #474 from Silabs-ArjanB/ArjanB_preempt
    
    Increased SMCLIC_ID_WIDTH range. Removed wrong preemption example cod…

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_cv32e40x."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_cv32e40x".format(f))
    return fn
