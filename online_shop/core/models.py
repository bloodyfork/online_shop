from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class BaseManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def archive(self):
        return super().get_queryset()


class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    create_timestamp = models.DateTimeField(auto_now_add=True)
    modify_timestamp = models.DateTimeField(auto_now=True)
    delete_timestamp = models.DateTimeField(default=None, null=True, blank=True)

    objects = BaseManager()

    class Meta:
        abstract = True

    def logical_delete(self):
        self.is_deleted = True


# class User(AbstractUser):
#
#     def __str__(self):
#         return self.get_username()
