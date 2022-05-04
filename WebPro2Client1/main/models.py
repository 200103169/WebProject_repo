from django.contrib.auth.models import User
from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Module1(models.Model):
     title = models.CharField('Названия', max_length=80)
     news = models.TextField('Описания', blank=False)

     def __str__(self):
         return self.title

     def get_absolute_url(self):
         return f'/news/{self.id}'

     def get_num(self):
         return 15



class Module2(models.Model):
        name = models.CharField(max_length=50)
        gold = models.IntegerField()
        silver = models.IntegerField()
        bronze = models.IntegerField()
        overall = models.IntegerField()

        def __str__(self):
            return self.name


class Module3(models.Model):
    name = models.CharField(max_length=50)
    gold = models.IntegerField()
    silver = models.IntegerField()
    bronze = models.IntegerField()
    overall = models.IntegerField()

    def __str__(self):
        return self.name




