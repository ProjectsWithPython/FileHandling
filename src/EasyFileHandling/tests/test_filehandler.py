import unittest
import os
import sys
import io
from EasyFileHandling.main import FileHandler


class FileHandlerTests(unittest.TestCase):
    test_filename = 'test.txt'

    def setUp(self):
        try:
            with open(self.test_filename, 'w') as f:
                f.write('This is a test file.\nThis is the second line.')
        except PermissionError:
            self.fail('Unable to write test file.')
        self.fh = FileHandler(self.test_filename)

    def tearDown(self):
        os.remove(self.test_filename)

    def test_does_file_exists_method(self):
        file_exists = self.fh.does_file_exist()
        self.assertTrue = file_exists

    def test_get_line_count(self):
        line_count = self.fh.get_line_count()
        self.assertEqual(line_count, 2)

    def test_get_longest_line(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.fh.get_longest_line()
        sys.stdout = sys.__stdout__
        self.assertEqual(
            capturedOutput.getvalue().rstrip('\n'),
            'Longest line is 24 at line index of [1]'
            )


if __name__ == '__main__':
    unittest.main()
