from django.db import models


# Create your models here.
class BaseManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def archive(self):
        return super().get_queryset()
