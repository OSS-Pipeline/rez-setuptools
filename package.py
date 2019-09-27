name = "setuptools"

version = "41.2.0"

authors = [
    "Python Packaging Authority"
]

description = \
    """
    Easily download, build, install, upgrade, and uninstall Python packages.
    """

requires = [
    "cmake-3",
    "python-2.7"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

#TODO: Use the SHA1 of the archive instead.
uuid = "setuptools-41.2.0"

def commands():
    env.PYTHONPATH.prepend("{root}")
