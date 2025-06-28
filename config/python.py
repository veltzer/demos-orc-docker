""" python deps for this project """

build_requires: list[str] = [
    "flask",
    "mysql-connector-python",
    "pyvardump",
    "requests",

    "pydmt",
    "pymakehelper",
    "pycmdtools",
    "pyclassifiers",

    "pylint",
    "pytest",
    "pytest-cov",
    "mypy",

    # types
    "types-requests",
]
requires = build_requires
