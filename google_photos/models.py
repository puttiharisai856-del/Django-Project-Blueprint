from django.db import models

# Create your models here.
class Google_ph(models.Model):
    title=models.CharField(max_length=100)
    mb=models.IntegerField(default=0)

    def __str__(self):
        return self.title
