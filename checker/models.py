from django.db import models
from django.contrib.auth.models import User


class UrlChecker(models.Model):
    url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interval = models.IntegerField(default=5)  # time in seconds

    def __str__(self):
        return f"{self.id}. {self.url}"
