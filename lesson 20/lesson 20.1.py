import lesson_Library
import unittest

class LibraryTestCase(unittest.TestCase):
    def setUp(self):
        self.library = lesson_Library.Library('hogwarts library')
        self.author = lesson_Library.Author('J.K. Rowling','UK',1965)

    def test_book(self):
        self.assertIsInstance(self.library.new_book('J.K. Rowling',1965, self.author),lesson_Library.Book)


if __name__ == "__main__":
    unittest.main()