import os
from django.db import models
from django.conf import settings

ITEM_ORDER = [
#    ('author', 'author ascending'),
    ('title', 'title ascending'),
    ('created_date', 'created date ascending'),
    ('modified_date', 'modified date ascending'),
#    ('-author', 'author descending'),
    ('-title', 'title descending'),
    ('-created_date', 'created date descending'),
    ('-modified_date', 'modified date descending'),
]

class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True,
                               on_delete=models.CASCADE)
    order = models.CharField(max_length=15, choices=ITEM_ORDER,
                             blank=True, null=True)

    @property
    def ancestors(self):
        current = self
        while current.parent:
            yield current.parent
            current = current.parent

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

class Item(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                               blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class File(Item):
    data = models.FileField(upload_to='documents/')
    
    def filetype(self):
        return os.path.splitext(str(self.data))[1].upper()[1:]

class Document(Item):
    content = models.TextField()
