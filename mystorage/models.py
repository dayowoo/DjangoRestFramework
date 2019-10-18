from django.db import models
from django.conf import settings

class Essay(models.Model):
    # 작성자 / on_delete=models.CASCADE: 모델 지우면 다 지워지게 한다
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField()

class Album(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    desc = models.CharField(max_length=100)

class Files(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    myfile = models.FileField(blank=False, null=False, upload_to="fiels")
    desc = models.CharField(max_length=100)
