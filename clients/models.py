from django.db import models

# Create your models here.
class clients_model(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    globalScore = models.BigIntegerField()
    hoursPracticed = models.IntegerField()

    def __str__(self):
        return self.username 
    