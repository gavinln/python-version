"""
https://realpython.com/python310-new-features/
"""

import enum
import sys

from random_user import get_age, get_user


def pattern_matching():
    print("Hello from py3-10!")
    user1 = get_user("1.3")
    user2 = get_user("1.1")

    print(f"{user1['dob']=}")
    print(f"{user2['dob']=}")

    age1 = get_age(user1)
    age2 = get_age(user2)
    print(f"{age1=}")
    print(f"{age2=}")


def sum_list(numbers):
    match numbers:
        case []:
            return 0

        case [first, *rest]:
            return float(first) + sum_list(rest)

        case _:
            wrong_type = numbers.__class__.__name__
            raise ValueError(f"Can only sum lists, not {wrong_type!r}")


def greet(name):
    match name:
        case "Guido":
            return "Hi, Guido!"
        case _:
            return "Howdy, stranger!"


class Pythonista(str, enum.Enum):
    BDFL = "Guido"
    FLUFL = "Barry"


def greet2(name):
    match name:
        case Pythonista.BDFL:
            return "Hi, Guido!"
        case _:
            return "Howdy, stranger!"


def fizzbuzz(number):
    mod_3 = number % 3
    mod_5 = number % 5

    if mod_3 == 0 and mod_5 == 0:
        return "fizzbuzz"
    elif mod_3 == 0:
        return "fizz"
    elif mod_5 == 0:
        return "buzz"
    else:
        return str(number)


def fizzbuzz2(number):
    mod_3 = number % 3
    mod_5 = number % 5

    match (mod_3, mod_5):
        case (0, 0):
            return "fizzbuzz"
        case (0, _):
            return "fizz"
        case (_, 0):
            return "buzz"
        case (_, _):
            return str(number)


names = ["Louvre", "Diagon Alley", "Saturn V", "Millennium Falcon", "NYC"]
set_numbers = ["21024", "75978", "92176", "75192", "21028"]
num_pieces = [695, 5544, 1969, 7541, 598]
num_pieces2 = [695, 5544, 1969, 7541]


def zip_equal():
    return zip(names, set_numbers, num_pieces, strict=True)


def zip_unequal():
    return zip(names, set_numbers, num_pieces2)


def newer_python():
    if sys.version_info > (3, 6):
        return True
    return False


def main():
    print(f"Hello from {sys.version}!")
    pattern_matching()

    assert sum_list([]) == 0
    assert sum_list([3, 4, 2]) == 9
    assert sum_list(["3", "4", "2"]) == 9

    assert greet("Guido") == "Hi, Guido!"
    assert greet("John") == "Howdy, stranger!"

    assert greet2("Guido") == "Hi, Guido!"
    assert greet2("John") == "Howdy, stranger!"

    assert fizzbuzz(3) == "fizz"
    assert fizzbuzz(14) == "14"
    assert fizzbuzz(15) == "fizzbuzz"
    assert fizzbuzz(65) == "buzz"

    assert fizzbuzz2(3) == "fizz"
    assert fizzbuzz2(14) == "14"
    assert fizzbuzz2(15) == "fizzbuzz"
    assert fizzbuzz2(65) == "buzz"

    print(list(zip_equal()))
    print(list(zip_unequal()))

    print(f"{newer_python()=}")


if __name__ == "__main__":
    main()
