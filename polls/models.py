import datetime
from email.policy import default

from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    excerpt = models.TextField(max_length=300)
    num_lessons = models.PositiveSmallIntegerField(default=0)
    picture = models.ImageField(upload_to='polls', default="saknd")


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        from django.utils import timezone
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
