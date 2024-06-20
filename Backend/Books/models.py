from django.db import models
from django.core.validators import MinValueValidator
from Backend.Books.validators import validateYearNotInFuture

class Book (models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    yearOfPublication = models.IntegerField(
        validators=[
            MinValueValidator(0, message="El año no puede ser negativo."),
            validateYearNotInFuture
        ]
    )
    genreChoices = [
        ("sci-fi", "Ciencia ficción"),
        ("action&adventure", "Acción y aventura"),
        ("horror", "Terror"),
        ("romance", "Romance"),
        ("history", "Historia"),
        ("philosophy", "Filosofía"),
        ("science", "Ciencia"),
        ("self-help", "Autoayuda"),
    ]
    genre = models.CharField(choices=genreChoices,max_length=30)
    stock = models.IntegerField(
        validators=[
            MinValueValidator(0, message="El stock no puede ser negativo."),
        ],
        default=0
    )
    image = models.CharField(max_length=200)
