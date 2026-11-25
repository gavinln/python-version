"""
https://realpython.com/python313-new-features/
"""

import copy
import dataclasses
import datetime
import logging
import pathlib
import sys
from collections import deque
from typing import NamedTuple, reveal_type
from zoneinfo import ZoneInfo

SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
log = logging.getLogger(__name__)


class QueueNoDefault[T]:
    def __init__(self):
        self.elements: deque[T] = deque()

    def push(self, element: T) -> None:
        self.elements.append(element)

    def pop(self) -> T:
        return self.elements.popleft()


class QueueDefault[T = str]:
    def __init__(self):
        self.elements: deque[T] = deque()

    def push(self, element: T) -> None:
        self.elements.append(element)

    def pop(self) -> T:
        return self.elements.popleft()


class Person(NamedTuple):
    name: str
    place: str
    version: str


@dataclasses.dataclass
class Person2:
    name: str
    place: str
    version: str


def main():
    print(f"Hello from {sys.version}!")

    str_queue = QueueNoDefault[str]()
    str_queue.push("one")
    str_queue.push("three")
    print(f"{str_queue=}")
    reveal_type(str_queue)

    int_queue = QueueNoDefault[int]()
    int_queue.push(1)
    int_queue.push(3)
    print(f"{int_queue=}")
    reveal_type(int_queue)

    str_queue2 = QueueDefault()
    str_queue2.push("one")
    str_queue2.push("three")
    print(f"{str_queue2=}")
    reveal_type(str_queue2)

    int_queue2 = QueueDefault[int]()
    int_queue2.push(1)
    int_queue2.push(3)
    print(f"{int_queue2=}")
    reveal_type(int_queue2)

    person = Person(name="Geir Arne", place="Oslo", version="3.12")
    print(person)
    person2 = copy.replace(person, version="3.13")
    print(person2)

    tz = ZoneInfo("America/Los_Angeles")
    dt1 = datetime.datetime.now(tz)
    print(f"dt1={dt1.isoformat()}")

    dt2 = dt1.replace(month=3, day=3)
    print(f"dt2={dt2.isoformat()}")

    person3 = Person2(name="Geir Arne", place="Oslo", version="3.12")
    print(person3)
    person4 = dataclasses.replace(person3, version="3.13")
    print(person4)


if __name__ == "__main__":
    logging.basicConfig()
    main()
