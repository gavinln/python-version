"""
https://realpython.com/python311-new-features/
"""

import logging
import pathlib
import sys

import units_lib

SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
log = logging.getLogger(__name__)


def exception_notes():
    """Demonstrate enriching exceptions with notes (PEP 678).

    Attaches two notes to a ``ValueError`` using ``add_note()`` and prints
    the resulting ``__notes__`` list.
    """
    err = ValueError(678)
    err.add_note("Enriching Exceptions with Notes")
    err.add_note("Python 3.11")

    print(err.__notes__)


def exception_groups_both_caught():
    """Demonstrate exception groups and the ``except*`` syntax (PEP 654).

    Raises an ``ExceptionGroup`` containing a ``TypeError`` and a
    ``ValueError``. The block handles both members with separate
    ``except*`` clauses.
    """
    try:
        raise ExceptionGroup("twice", [TypeError("int"), ValueError(654)])
    except* ValueError as err:
        print(f"handling ValueError: {err.exceptions}")
    except* TypeError as err:
        print(f"handling TypeError: {err.exceptions}")


def exception_groups_one_caught():
    """Demonstrate exception groups and the ``except*`` syntax (PEP 654).

    Raises an ``ExceptionGroup`` containing a ``TypeError`` and a
    ``ValueError``. Only the  ``ValueError`` is handled, so the
    unmatched ``TypeError`` subgroup is re-raised.
    """
    try:
        raise ExceptionGroup("twice", [TypeError("int"), ValueError(654)])
    except* ValueError as err:
        print(f"handling ValueError: {err.exceptions}")


def main():
    """Run the demo script.

    Prints the running interpreter version, exercises unit conversion via
    ``units_lib``, and then showcases the Python 3.11 exception features.
    """
    print(f"Hello from {sys.version}!")

    base_units = units_lib.get_base_units()
    units = units_lib.get_units(base_units)
    if len(units) > 0:
        print(units_lib.to_baseunit(units, 7, "s"))
        print(units_lib.to_baseunit(units, 3.11, "minutes"))
        print(units_lib.to_baseunit(units, 14, "days"))
        print(units_lib.to_baseunit(units, 1 / 12, "yr"))

    exception_notes()

    exception_groups_both_caught()

    try:
        exception_groups_one_caught()
    except* TypeError as err:
        print(f"handing {err.exceptions} outside function")
    # except* Exception as err:
    #     print(err)


if __name__ == "__main__":
    logging.basicConfig()
    main()
