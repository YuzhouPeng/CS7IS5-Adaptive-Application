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
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    sex = models.CharField(max_length=32, choices=gender, default='Male')
    create_time = models.DateTimeField(auto_now_add=True)
    last_visited_page = models.IntegerField(default=1)
    new_user = models.IntegerField(default=1)

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


class Page(models.Model):
    """"""
    topics = models.ForeignKey(
        Topics,
        on_delete=models.CASCADE,
    )
    page_name = models.CharField(max_length=128)
    content = models.TextField()


class Keywords(models.Model):
    """"""
    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=128)
    start_index = models.IntegerField(null=True)
    end_index = models.IntegerField(null=True)
    similarity = models.FloatField()
    summary = models.TextField()

class UserTopic(models.Model):
    """"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    topic = models.ForeignKey(
        Topics,
        on_delete=models.CASCADE
    )
    total_count = models.IntegerField(default=0)
    last_page_count = models.IntegerField(default=0)
    last_page_id_of_topic = models.IntegerField(default=0)
    model_updated = models.IntegerField(default=0)
    topic_score = models.FloatField(default=0.5)




