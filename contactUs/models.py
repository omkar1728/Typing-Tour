from django.db import models

# Create your models here.
class feedback(object):
    title = models.TextField(max_length=30)
    body = models.TextField(max_length=500)
    def __init__(self):
       return self.title