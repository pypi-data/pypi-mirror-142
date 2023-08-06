import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.1.0.post197"
version_tuple = (0, 1, 0, 197)
try:
    from packaging.version import Version as V
    pversion = V("0.1.0.post197")
except ImportError:
    pass

# Data version info
data_version_str = "0.1.0.post71"
data_version_tuple = (0, 1, 0, 71)
try:
    from packaging.version import Version as V
    pdata_version = V("0.1.0.post71")
except ImportError:
    pass
data_git_hash = "861d72eead19a40ba42c4e6080f3c9e8795f58dd"
data_git_describe = "0.1.0-71-g861d72e"
data_git_msg = """\
commit 861d72eead19a40ba42c4e6080f3c9e8795f58dd
Merge: a96ab27 7a4c03b
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Thu Mar 17 12:18:16 2022 +0100

    Merge pull request #476 from silabs-oivind/doc_typo_fix
    
    Fix typo in doc

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
