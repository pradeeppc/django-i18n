from django.db import models


class BaseModelManager(models.Manager):

    def get_queryset(self):
        return super(BaseModelManager, self).get_queryset()
