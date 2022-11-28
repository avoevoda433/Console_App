from degreesconv.converter.converter import selection
from degreesconv.parser.parser import get_args


def main():
    command, values = get_args()
    print(selection(command, values))


if __name__ == '__main__':
    main()
