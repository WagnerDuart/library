from django.db import models
from uuid import uuid4


# Create your models here.

class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)  # id do livro
    title = models.CharField(max_length=255)  # título do livro
    author = models.CharField(max_length=255)  # autor
    release_year = models.IntegerField()  # ano de lamçamento
    state = models.CharField(max_length=50)  # estado do livro
    pages = models.IntegerField()  # quantidade de paginas
    create_at = models.DateField(auto_now_add=True)  # o dia de criação na base de dados
    publishing_conpany = models.CharField(max_length=255)  # editora
    