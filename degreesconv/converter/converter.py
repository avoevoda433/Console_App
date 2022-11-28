"""
The converter.py file contains the degreesconv module logic
"""
from typing import Callable
from degreesconv.converter.info import get_result, info_about_command, available_commands
from enum import Enum


class Commands(Enum):
    C2F = 'c2f'
    F2C = 'f2c'


formulas = {Commands.C2F.value: lambda x: round(x * 9 / 5 + 32, 2),
            Commands.F2C.value: lambda x: round((x - 32) * 5 / 9, 2)}


def _convert(modifier: Callable[[float], float], temperature_values: list) -> list:
    """ This function takes a modifier and a list of temperature values, returns a list of modified values """
    try:
        return list(map(modifier, temperature_values))
    except (TypeError, ValueError):
        return []


def selection(command: str, values: list) -> str:
    """ This function takes and checked command and temperature values, after - run needed functions """
    try:
        return get_result(values, _convert(formulas[command], values), command) \
            if Commands(command) and values else info_about_command(command)
    except ValueError:
        return available_commands(list(formulas.keys()))
