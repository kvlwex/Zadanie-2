from django.db import models
from authors.models import Author

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL)
    isbn = models.CharField(max_length=20, unique=True)
    publication_year = models.IntegerField()
    genres = models.CharField(max_length=255, blank=True)
    co_authors = models.CharField(max_length=255, blank=True)
    summary = models.TextField(blank=True)

    def __str__(self):
        return self.title

