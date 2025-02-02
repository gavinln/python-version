"""
https://realpython.com/python312-new-features/
"""

import calendar
import logging
import pathlib
import sys
from itertools import batched
from typing import Sequence

from accounts import BankAccount, SavingsAccount

SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
log = logging.getLogger(__name__)


def better_f_strings():
    version = {"major": 3, "minor": 12}

    # double quotes in f-strings
    print(f"Python {version["major"]}.{version["minor"]}")

    names = ["Brett", "Emily", "Gregory", "Pablo", "Thomas"]

    # backslashes in f-strings
    print(f"Steering Council:\n {"\n ".join(names)}")

    # newlines in curly braces in f-strings
    print(
        f"Steering Council: {
        ", ".join(names)
    }"
    )


# type variable syntax
def first_list[T](elements: list[T]) -> T:
    return elements[0]


# type variable syntax
def first_sequence[T](elements: Sequence[T]) -> T:
    return elements[0]


def flip[T0, T1](pair: tuple[T0, T1]) -> tuple[T1, T0]:
    return (pair[1], pair[0])


def free_type[T](arg: T) -> T:
    print(f"{type(arg)=}")
    return arg


def constrained_type[T: (int, float, complex)](arg: T) -> T:
    print(f"{type(arg)=}")
    return arg


def bounded_type[T: str](arg: T) -> T:
    print(f"{type(arg)=}")
    return arg


class MyStr(str):
    def double(self):
        return self * 2


def calendar_constants():
    print(", ".join(mth for mth in calendar.month_abbr if mth))

    print(", ".join(calendar.day_name))

    print("name, value for months", "-" * 9)
    print(", ".join(m.name for m in calendar.Month))
    print(", ".join(str(m.value) for m in calendar.Month))

    print("name, value for days", "-" * 9)
    print(", ".join(d.name for d in calendar.Day))
    print(", ".join(str(d.value) for d in calendar.Day))


def itertools_batched():
    print("months in quarter", "-" * 9)
    for quarter in batched(calendar.Month, 3):
        print(", ".join(month.name for month in quarter))


def path_walk():
    for path, directories, files in pathlib.Path.cwd().walk():
        if any(part.startswith(".") for part in path.parts):
            continue
        elif any(part.startswith("_") for part in path.parts):
            continue
        print(path, directories, files)


def main():
    print(f"Hello from {sys.version}!")

    # better_f_strings()

    print(first_list([1, 2]))
    # Argument of type tuple[...] cannot be assigned to type list[T@first_list]
    print(first_list(("a", "b")))

    print(first_sequence([1, 2]))
    # no type checking error
    print(first_sequence(("a", "b")))

    print(flip(("a", "b")))

    print(free_type(1 + 2j))
    print(free_type("abc"))

    print(constrained_type(1 + 2j))
    # Literal['abc'] cannot be assigned to T@constrained_type
    print(constrained_type("abc"))

    print("abc")
    print(MyStr("abc").double())

    print(bounded_type("abc"))
    print(bounded_type(MyStr("abc")))

    ba = BankAccount.from_balance(1000)
    ba.withdraw(123.45)
    print(f"{ba=}")

    sa = SavingsAccount.from_balance(1000, 2)
    sa.withdraw(123.45)
    print(f"{sa=}")
    sa.add_interest()
    print(f"{sa=}")

    print(sa.withdraw.__override__)  # type: ignore

    calendar_constants()

    itertools_batched()

    path_walk()


if __name__ == "__main__":
    logging.basicConfig()
    main()
