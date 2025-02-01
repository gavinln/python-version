"""
https://realpython.com/python311-new-features/
"""

import logging
import pathlib
import tomllib
from pprint import pprint as pp

SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
log = logging.getLogger(__name__)


def get_base_units() -> dict | None:
    units_file = SCRIPT_DIR / "units.toml"

    base_units = None

    with units_file.open(mode="rb") as f:
        base_units = tomllib.load(f)

    return base_units


def get_units(base_units: dict | None) -> dict:
    units = {}
    if base_units:
        for unit, unit_info in base_units.items():
            units[unit] = unit_info
            for alias in unit_info["aliases"]:
                units[alias] = unit_info
    return units


def to_baseunit(units, value, from_unit):
    from_info = units[from_unit]
    if "multiplier" not in from_info:
        return (
            value,
            from_info["label"]["singular" if value == 1 else "plural"],
        )

    return to_baseunit(units, value * from_info["multiplier"], from_info["to_unit"])


def main():
    base_units: dict | None = get_base_units()
    if base_units:
        units = get_units(base_units)
        pp(units)


if __name__ == "__main__":
    logging.basicConfig()
    main()
