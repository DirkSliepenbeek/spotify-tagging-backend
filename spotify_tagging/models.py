from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField


class User(AbstractUser):
    pass

    def __str__(self):
        return self.get_full_name() or self.username


class Project(models.Model):
    name = models.CharField(max_length=250)
    users = models.ManyToManyField(User)


class Tag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)


class Track(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    uri = models.CharField(max_length=50)
    name = models.CharField(max_length=250)
    tags = models.ManyToManyField(Tag)
    album = models.CharField(max_length=250)
    artists = ArrayField(models.CharField(max_length=250))


