from django.db import models

# Create your models here.



class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    box = models.PositiveIntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    def delete_card(self):
        self.delete()