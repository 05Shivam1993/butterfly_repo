from django.db import models

# Create your models here.
class GeneralKnowledge(models.Model):
    question = models.CharField(max_length = 100, null = False)
    answer = models.CharField(max_length = 100, null = False)

    def __str__(self):
        return self.question
