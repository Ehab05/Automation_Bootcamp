import numbers
import unittest


from Library_Homework.Book import Book


class TestBookFunction(unittest.TestCase):
    def test_book_title(self):
        book = Book('ehab', 'hasan', '2024', 'drama')
        self.assertIs('ehab', book.title)

    def test_book_author(self):
        book = Book('ehab', 'hasan', '2024', 'drama')
        self.assertIs('hasan', book.author)

    def test_book_publication_year(self):
        book = Book('ehab', 'hasan', '2024', 'drama')
        self.assertIs('2024', book.publication_year)

    def test_book_genre(self):
        book = Book('ehab', 'hasan', '2024', 'drama')
        self.assertIs('drama', book.genre)

    def test_book_title_is_string(self):
        book = Book('ehab', 'hasan', '2024', 'drama')
        self.assertTrue(type(book.title) == str)

    def test_book_author_is_string(self):
        book = Book('ehab', 'hasan', '2024', 'drama')
        self.assertTrue(type(book.author) == str)

    def test_book_publication_year_is_positive_number(self):
        book = Book('ehab', 'hasan', '2024', 'drama')
        self.assertTrue(int(book.publication_year) > 0)

    def test_book_publication_year_is_number(self):
        book = Book('ehab', 'hasan', 'sdfs', 'drama')
        isnum = int(book.publication_year)
        self.assertIs(type(isnum),int)

    def test_book_genre_is_string(self):
        book = Book('ehab', 'hasan', '2024', 'drama')
        self.assertTrue(type(book.genre) == str)
