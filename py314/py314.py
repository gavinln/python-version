"""
https://realpython.com/python314-new-features/
"""

import logging
import pathlib
import sys

SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
log = logging.getLogger(__name__)


def main():
    print(f"Hello from {sys.version}!")


if __name__ == "__main__":
    logging.basicConfig()
    main()
