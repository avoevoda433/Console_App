"""
In the parse.py file parse CLI arguments
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('command', nargs='?', type=str, default='', help='choice of conversion method')
parser.add_argument('values', nargs='*', type=float, default=[],
                    help='temperature values to conversion separated by space')


def get_args() -> tuple:
    args = parser.parse_args()
    return args.command, args.values
