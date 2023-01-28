from django.db import models
from myapp.managers.base import BaseModelManager

from django.contrib.postgres.fields import JSONField
from django.conf import settings


class BaseModel(models.Model):

    class Meta:
        abstract = True

    objects = BaseModelManager()
    translation = JSONField(default={})


class Article(BaseModel):

    class Meta:
        db_table = 'article'

    title = models.CharField(max_length=256)
    description = models.TextField()

    def __init__(self, *args, **kwargs):
        super(Article, self).__init__(*args, **kwargs)
        if not self.title:
            default_dict = {x[0]: [{field.name: '' for field in Article._meta.local_fields if field.name != 'translation'}] for x in settings.LANGUAGES}
            self.translation.update(default_dict)

    def __str__(self):
        return f'Title - {self.title}'
