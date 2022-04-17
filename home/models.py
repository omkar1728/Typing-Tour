from django.db import models

# Create your models here.
class level:
    level_text = models.CharField(max_length=100)
    level_description = models.CharField(max_length=20)
    def __str__(self):
        return self.level_description