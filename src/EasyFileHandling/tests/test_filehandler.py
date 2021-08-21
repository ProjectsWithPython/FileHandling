import unittest
import os
from EasyFileHandling.main import FileHandler

class FileHandlerTests(unittest.TestCase):
    test_filename = 'test.txt'

    def setUp(self):
        try:
            with open(self.test_filename, 'w') as f:
                f.write('This is a test file.\nThis is the second line.')
        except PermissionError as err:
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

if __name__ == '__main__':
    unittest.main()