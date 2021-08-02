from django.conf import settings
from django.db import models


# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length=100, unique=True,)
    account_support = models.EmailField(null=True, blank=True, max_length=50,)
    tech_support = models.EmailField(null=True, blank=True, max_length=50,)
    url = models.URLField(null=True, blank=True, max_length=50,)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    address = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    hobby = models.CharField(max_length=50)
    name = models.CharField(max_length=50, unique=True)
    org = models.ForeignKey('Organization', related_name='users', on_delete=models.CASCADE,)
    phone_number = models.PositiveSmallIntegerField()
    pin = models.PositiveSmallIntegerField()
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
