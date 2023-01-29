from django.db import models


class BaseModelManager(models.Manager):

    def get_queryset(self):
        # TODO return queryset with respect to default language
        return super(BaseModelManager, self).get_queryset()
