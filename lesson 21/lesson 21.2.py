import unittest
from lesson_task1 import Open_file

class TestOpen_file(unittest.TestCase):

    def test_file_open_and_close(self):
        with Open_file('test lesson 21.txt', 'w') as file:
            self.assertFalse(file.closed)

    def test_file_write(self):
        with Open_file('test lesson 21.txt', 'w') as file:
            file.write('Hello, world!')
        with Open_file('test lesson 21.txt', 'r') as file:
            content = file.read()
        self.assertEqual(content, 'Hello, world!')


if __name__ == '__main__':
    unittest.main()