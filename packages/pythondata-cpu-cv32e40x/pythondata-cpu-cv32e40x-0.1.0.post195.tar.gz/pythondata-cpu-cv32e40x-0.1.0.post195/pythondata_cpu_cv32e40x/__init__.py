import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.1.0.post195"
version_tuple = (0, 1, 0, 195)
try:
    from packaging.version import Version as V
    pversion = V("0.1.0.post195")
except ImportError:
    pass

# Data version info
data_version_str = "0.1.0.post69"
data_version_tuple = (0, 1, 0, 69)
try:
    from packaging.version import Version as V
    pdata_version = V("0.1.0.post69")
except ImportError:
    pass
data_git_hash = "a96ab271502c0a529689144e25bd239dca3ced0a"
data_git_describe = "0.1.0-69-ga96ab27"
data_git_msg = """\
commit a96ab271502c0a529689144e25bd239dca3ced0a
Merge: 584254b 5ce0692
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Thu Mar 17 10:39:55 2022 +0100

    Merge pull request #475 from silabs-oivind/sticky_tracer
    
    Make tracer sticky in between retired instructions. Makes it easier t…

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
