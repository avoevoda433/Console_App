import unittest
from degreesconv.converter import info


class TestStringMethods(unittest.TestCase):
    def test_command_overview(self):
        self.assertMultiLineEqual(info._command_overview('<command>'), '\033[1m<command>\033[0m'
                                                                       '\t\t- Format of the command:\033[3;34m '
                                                                       'degreesconv <command> [values ...]\n\033[0m'
                                                                       '\t\t- Get additional info about command:'
                                                                       '\033[3;34m degreesconv <command>\n\n\033[0m')

    def test_available_commands(self):
        self.assertMultiLineEqual(info._command_info('c2f'), '\033[1mc2f\033[0m - '
                                                             'convert temperature values from celsius to fahrenheit\n'
                                                             '\t- Format of the command:'
                                                             '\033[3;34m degreesconv c2f [values ...]\n\033[0m'
                                                             '\t-\033[3;34m [values ...]\033[0m '
                                                             'is numbers separated by space.\n')
        self.assertMultiLineEqual(info._command_info('f2c'), '\033[1mf2c\033[0m - '
                                                             'convert temperature values from fahrenheit to celsius\n'
                                                             '\t- Format of the command:'
                                                             '\033[3;34m degreesconv f2c [values ...]\n\033[0m'
                                                             '\t-\033[3;34m [values ...]\033[0m '
                                                             'is numbers separated by space.\n')

    def test_result_info(self):
        self.assertMultiLineEqual(info._result_info([1, 2], [3, 4], 'c2f'), 'Temperature in    celsius:'
                                                                            '\t\033[3;34m 1, 2\n\033[0m'
                                                                            'Temperature in fahrenheit:'
                                                                            '\t\033[3;34m 3, 4\n\033[0m')
        self.assertMultiLineEqual(info._result_info([1, 2], [3, 4], 'f2c'), 'Temperature in fahrenheit:'
                                                                            '\t\033[3;34m 1, 2\n\033[0m'
                                                                            'Temperature in    celsius:'
                                                                            '\t\033[3;34m 3, 4\n\033[0m')


if __name__ == '__main__':
    unittest.main()
