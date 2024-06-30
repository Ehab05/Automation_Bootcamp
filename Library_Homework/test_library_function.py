import unittest

from Library import Library
from Book import Book


class TestLibraryFunctions(unittest.TestCase):

    def setUp(self):
        self.library1 = Library("library.json")
        self.book1 = Book('ehab', 'hasan', '2024', 'drama')

    def test_book_title(self):
        self.library1.add_book(self.book1)
        titles = list(map(lambda book1: book1.title, self.library1.list_books()))
        self.assertIn('ehab', titles)

    def test_add_book(self):
        self.library1.add_book(self.book1)
        self.assertIn(self.book1, self.library1.books)

    def test_delete_book(self):
        self.library1.add_book(self.book1)
        self.library1.delete_book(self.book1.title)
        self.assertNotIn(self.book1, self.library1.books)


