class Book:
    def __init__(self, title, author, publication_year, genre):
        self._title = title
        self._author = author
        self._publication_year = publication_year
        self._genre = genre

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self.author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def publication_year(self):
        return self._publication_year

    @publication_year.setter
    def publication_year(self, value):
        self._publication_year = value

    @property
    def genre(self):
        return self.author

    @genre.setter
    def genre(self, value):
        self._genre = value

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year}), Genre: {self.genre}"
