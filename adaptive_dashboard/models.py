from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
    gender = (
        ('male',"Male"),
        ('female',"Female"),
        ('other',"Other"),
    )

    topics = (
        ('music', "Music"),
        ('sport', "Sport"),
        ('movie', "Movie"),
        ('book', "Book"),
        ('drama', "Drama"),
        ('dance', "Dance"),
    )
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    sex = models.CharField(max_length=32, choices=gender, default='Male')
    interest = models.CharField( max_length=128 )
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ["-create_time"]
        verbose_name = "user"
        verbose_name_plural = "user"
class Attitude(models.Model):
    name = models.CharField(max_length=128)
    weight = models.FloatField(max_length=128)

class PageId(models.Model):
    pageid = models.IntegerField

class Topics(models.Model):
    """"""
    name = models.CharField(max_length=128)

class Keywords(models.Model):
    """"""
    name = models.CharField(max_length=128)
    topic = models.ForeignKey(
        Topics,
        on_delete=models.CASCADE,
    )

class Page(models.Model):
    """"""
    userid = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    pageid = models.ForeignKey(
        PageId,
        on_delete=models.CASCADE,
    )
    keyword = models.ForeignKey(
        Keywords,
        on_delete=models.CASCADE,
    )
    opinion = models.ForeignKey(
        Attitude,
        on_delete=models.CASCADE,
    )


class Records(models.Model):
    """"""
    username = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    pageid = models.ForeignKey(
        PageId,
        on_delete=models.CASCADE,
    )
    totallink = models.IntegerField(max_length=128)
    effectivelink = models.IntegerField(max_length=128)
    weight = models.FloatField(max_length=128)


