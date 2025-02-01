"""
https://realpython.com/python311-new-features/
"""

import logging
import pathlib
import sys
import tomllib

import units_lib

SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
log = logging.getLogger(__name__)


def exception_notes():
    err = ValueError(678)
    err.add_note("Enriching Exceptions with Notes")
    err.add_note("Python 3.11")

    print(err.__notes__)


def exception_groups():
    # both exceptions triggered
    try:
        raise ExceptionGroup("twice", [TypeError("int"), ValueError(654)])
    except* ValueError as err:
        print(f"handling ValueError: {err.exceptions}")
    except* TypeError as err:
        print(f"handling TypeError: {err.exceptions}")

    try:
        raise ExceptionGroup("twice", [TypeError("int"), ValueError(654)])
    except* ValueError as err:
        print(f"handling ValueError: {err.exceptions}")


def main():
    print(f"Hello from {sys.version}!")

    base_units = units_lib.get_base_units()
    units = units_lib.get_units(base_units)
    if len(units) > 0:
        print(units_lib.to_baseunit(units, 7, "s"))
        print(units_lib.to_baseunit(units, 3.11, "minutes"))
        print(units_lib.to_baseunit(units, 14, "days"))
        print(units_lib.to_baseunit(units, 1 / 12, "yr"))

    exception_notes()
    exception_groups()


if __name__ == "__main__":
    logging.basicConfig()
    main()
