import unittest

from Library import Library
from Book import Book


class TestLibraryFunctions(unittest.TestCase):

    def setUp(self):
        self.library1 = Library("library.json")
        self.book = Book('ehab', 'hasan', '2024', 'drama')

    def test_book_title(self):
        self.assertIs('ehab', self.library1.list_books())

    def test_add_book(self):
        self.library1.add_book(self.book)
        self.assertIn(self.book, self.library1.books)

    def test_delete_book(self):
        self.library1.delete_book(self.book.title)
        self.assertNotIn(self.book, self.library1.books)


