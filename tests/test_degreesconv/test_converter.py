import unittest
from degreesconv.converter.converter import _convert


class TestStringMethods(unittest.TestCase):
    def test_convert(self):
        self.assertListEqual(_convert(lambda x: float(x), [2, 3, 4]), [2.0, 3.0, 4.0])
        self.assertListEqual(_convert(lambda x: float(x), ['2', 3, 'd']), [])
        self.assertListEqual(_convert(lambda x, y: float(x) + y, [2, 3, 4]), [])
        self.assertListEqual(_convert(lambda x: float(x), 'not list'), [])
        self.assertListEqual(_convert(3, [2, 3, 4]), [])
        self.assertListEqual(_convert([3, 5], ['2', '3', '4']), [])
        self.assertListEqual(_convert(3, 'df'), [])


if __name__ == '__main__':
    unittest.main()
