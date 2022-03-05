from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# Create your models here.
class BaseManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def archive(self):
        return super().get_queryset()


class BaseModel(models.Model):
    class Meta:
        abstract = True

    is_deleted = models.BooleanField(default=False)
    create_timestamp = models.DateTimeField(auto_now_add=True)
    modify_timestamp = models.DateTimeField(auto_now=True)
    delete_timestamp = models.DateTimeField(default=None, null=True, blank=True)

    objects = BaseManager()

    def logical_delete(self):
        self.is_deleted = True


class MyUserManager(UserManager):

    # def _create_user(self, username, email, password, **extra_fields):
    #     return super()._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_superuser(username, email, password, **extra_fields)

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    objects = MyUserManager()
    phone = models.CharField(max_length=13, unique=True)
    USERNAME_FIELD = 'phone'

    def save(self, *args, **kwargs):
        self.username = self.phone
        if User.objects.filter(id=self.id):
            self.set_password(self.password)
        super().save(*args, **kwargs)

