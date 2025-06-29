""" python deps for this project """

build_requires: list[str] = [
    "flask",
    "mysql-connector-python",
    "pyvardump",
    "requests",

    "pydmt",
    "pymakehelper",
    "pycmdtools",

    "pylint",
    "pytest",
    "mypy",
    "ruff",

    # types
    "types-requests",
]
requires = build_requires
