""" python deps for this project """

import config.shared

install_requires: list[str] = [
    "flask",
    "mysql-connector-python",
    "pyvardump",
    "requests",
]
build_requires: list[str] = config.shared.BUILD
test_requires: list[str] = config.shared.TEST
types_requires: list[str] = [
    "types-requests",
]
requires = install_requires + build_requires + test_requires + types_requires
