
class Book:
    def __init__(self, title, author, publication_year, genre):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year}), Genre: {self.genre}"
