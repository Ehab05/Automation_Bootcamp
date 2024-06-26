import unittest

from Library_Homework import Library
from book import Book


class TestLibraryFunctions(unittest.TestCase):

    def setUp(self):
        self.book = Book('ehab', 'hasan', '2024', 'drama')

    def test_add_book(self):
        library1 = Library()
        library1.add_book(self.book)
        self.assertIn(self.book, library1.books)

    def test_stam(self):
        stam = self.book.stam()
        self.assertEqual(stam, 'hello world')
