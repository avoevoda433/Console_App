"""
The info.py file contains functions for the showing info about the degreesconv module work
"""

from enum import Enum


class Headers(Enum):
    AVAILABLE_COMMANDS = '\n\033[1;33mList of available commands:\n\033[0m'
    COMMANDS_INFO = '\n\033[1;33mInfo about command:\n\033[0m'
    RESULT = '\n\033[1;33mResult:\n\033[0m'


def _command_overview(command: str) -> str:
    """ Contains overview info about commands """
    return (f'\033[1m{command}\033[0m'
            f'\t\t- Format of the command:\033[3;34m degreesconv {command} [values ...]\n\033[0m'
            f'\t\t- Get additional info about command:\033[3;34m degreesconv {command}\n\n\033[0m')


def _command_info(command: str) -> str:
    """ Contains detailed info about commands """
    return (f'\033[1m{command}\033[0m'
            f' - convert temperature values from '
            f'{"celsius to fahrenheit" if command=="c2f" else "fahrenheit to celsius"}\n'
            f'\t- Format of the command:\033[3;34m degreesconv {command} [values ...]\n\033[0m'
            f'\t-\033[3;34m [values ...]\033[0m is numbers separated by space.\n')


def _result_info(list1: list, list2: list, command: str) -> str:
    """ Forms data for result output """
    return (f'Temperature in {"   celsius" if command=="c2f" else "fahrenheit"}:'
            f'\t\033[3;34m {", ".join(list(map(str, list1)))}\n\033[0m'
            f'Temperature in {"fahrenheit" if command=="c2f" else "   celsius"}:'
            f'\t\033[3;34m {", ".join(list(map(str, list2)))}\n\033[0m')


def available_commands(commands: list) -> str:
    """ Shows information about available commands """
    return "".join([Headers.AVAILABLE_COMMANDS.value, "".join([_command_overview(command) for command in commands])])


def info_about_command(command: str) -> str:
    """ Shows information about the selected command """
    return "".join([Headers.COMMANDS_INFO.value, _command_info(command)])


def get_result(values_before: list, values_after: list, command: str) -> str:
    """ Shows temperature values before and after calculation """
    return "".join([Headers.RESULT.value, _result_info(values_before, values_after, command)])
