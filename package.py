name = "setuptools"

version = "44.1.1"

authors = [
    "Python Packaging Authority"
]

description = \
    """
    Easily download, build, install, upgrade, and uninstall Python packages.
    """

requires = [
    "cmake-3+",
    "pip-19+",
    "python-2.7+"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "setuptools-{version}".format(version=str(version))

def commands():
    env.PYTHONPATH.prepend("{root}")

    # Helper environment variables.
    env.SETUPTOOLS_BINARY_PATH.set("{root}/bin")
