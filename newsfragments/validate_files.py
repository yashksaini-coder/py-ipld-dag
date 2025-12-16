import pathlib
import sys

ALLOWED_EXTENSIONS = {
    ".breaking.rst",
    ".bugfix.rst",
    ".deprecation.rst",
    ".docs.rst",
    ".feature.rst",
    ".internal.rst",
    ".misc.rst",
    ".performance.rst",
    ".removal.rst",
}

ALLOWED_FILES = {
    "validate_files.py",
    "README"
}

dir = pathlib.Path(__file__).parent

num_args = len(sys.argv) - 1
assert num_args in {0, 1}
if num_args == 1:
    assert sys.argv[1] in ("is-empty",)

for file in dir.iterdir():
    if file in ALLOWED_FILES:
        continue
    elif num_args == 0:
        full_extension = "".join(file.suffixes)
        if full_extension not in ALLOWED_EXTENSIONS:
            raise Exception(f"Unexpected file:{file}")
    elif sys.argv[1] == "is-empty":
        raise Exception(f"Unexpected file: {file}")
    else:
        raise RuntimeError(f"Invalid Arguments: {sys.argv} given. Not Found")
