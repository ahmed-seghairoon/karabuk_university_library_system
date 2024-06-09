from django.db import models
from uuid import uuid4

class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self) -> str:
        return self.name


def image_path(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = 'books/' + str(uuid4()) + '.' +str(extension)
    return new_filename

def file_path(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = 'books/' + str(uuid4()) + '.' +str(extension)
    return new_filename

class Book(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to=image_path)
    file = models.FileField(upload_to=file_path, null=True, blank=True, default=None)
    author = models.ManyToManyField(Author, related_name="books")
    stock = models.PositiveIntegerField(default=0)
    edition = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name

